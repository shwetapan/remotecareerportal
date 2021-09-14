from typing import Counter
import requests
from bs4 import BeautifulSoup
from datetime import date


headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

baseUrl = 'https://anka.breezy.hr'
url = "https://anka.breezy.hr/"

r = requests.get(url, headers= headers)
c = r.content
soup = BeautifulSoup(c,"html.parser")

table = []
results = soup.find_all("a",{"title":"Apply"})
[table.append(x) for x in results if x not in table]
# print(table)

def jobScan(link):
    the_job = {}
    jobUrl = '{}{}'.format(baseUrl, link['href'])
    the_job['urlLink'] = jobUrl
    # print(jobUrl)

    job = requests.get(jobUrl, headers=headers)
    jobC = job.content
    jobSoup = BeautifulSoup(jobC, "html.parser")
    # print(jobSoup)

    to_test = jobSoup.find_all("div", {"class":"banner"})
    # print(to_test)

    if to_test == []:
      return None
    else:
      title = jobSoup.find_all("h1")[0].text
      # print(title)
      the_job['title'] = title 
      # the_divs = jobSoup.find_all("div", {"class":"banner"})
      # country = the_divs[0].find_all("span")[0].text
      # print(country)
      # the_job['location'] = country
    #   date_posted = the_divs[2].find_all("span")[1].text
    #   the_job['date_posted'] = date_posted
      # full_part_time = the_divs[0].find_all("span")[2].text
      # print(full_part_time)
      # the_job['full_part_time'] = full_part_time
    #   the_job['type'] = 'Full Time'
    #   contract_type = the_divs[4].find_all("span")[1].text
    #   the_job['contract_type'] = contract_type  
      body = jobSoup.find_all("div",{"class":"description"})
      the_body = body[0]
      paragraphs = the_body.find_all("p")
      
      description = ''
    
      for p in paragraphs:
        description += p.text

      the_job['description'] = description
    return the_job 






# import model
from jobs.models import *
from django.contrib.auth.models import User

final_jobs = []

for x in table:
  job = jobScan(x)
  final_jobs.append(job)



# # the_user = User.objects.get(username='admin')
the_company = Company.objects.get(uniqueId='1b8a7f5a')

for test_job in final_jobs:

  if 'Director' in test_job['title']:
    the_category = Category.objects.get(title='Director')
  elif 'Engineer' in test_job['title']:
    the_category = Category.objects.get(title='Engineer')
  elif 'Developer' in test_job['title']:
    the_category = Category.objects.get(title='Developer')
  elif 'Databases' in test_job['title']:
    the_category = Category.objects.get(title='Databases')
  elif 'Business Analyst' in test_job['title']:
    the_category = Category.objects.get(title='Business Analyst')
  elif 'Technology' in test_job['title']:
    the_category = Category.objects.get(title='Technology')
  elif 'Research' in test_job['title']:
    the_category = Category.objects.get(title='Research')
  elif 'Trainee' in test_job['title']:
    the_category = Category.objects.get(title='Trainee')
  elif 'Specialist' in test_job['title']:
    the_category = Category.objects.get(title='Specialist')
  elif 'Manager' in test_job['title']:
    the_category = Category.objects.get(title='Manager')
  else:
    the_category = Category.objects.get(title='Uncategorised')
    


  newjob = Jobs.objects.create(

    title = test_job['title'],
   
    urlLink = test_job['urlLink'],
    date_posted = date.today(),
    description = test_job['description'],
    company = the_company,
    category = the_category,
    # owner = the_user,

  )













