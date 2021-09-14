from typing import Text
import requests
from bs4 import BeautifulSoup
from datetime import date


headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

baseUrl = 'https://11sigma.breezy.hr'
url = "https://11sigma.breezy.hr/"

r = requests.get(url, headers= headers)
c = r.content
soup = BeautifulSoup(c,"html.parser")

table = []
results = soup.find_all("a",{"title":"Apply"})
# print(results)

[table.append(x) for x in results if x not in table]
# print(table)

def jobScan(link):
    the_job = {}
    jobUrl = '{}{}'.format(baseUrl, link['href'])
    the_job['urlLink'] = jobUrl
    print(jobUrl)

    job = requests.get(jobUrl, headers=headers)
    jobC = job.content
    jobSoup = BeautifulSoup(jobC, "html.parser")

    to_test = jobSoup.find_all("div", {"class":"header"})
    

    if to_test == []:
      return None
    else:
      title = jobSoup.find_all("h1")[0].text
      print(title)
      the_job['title'] = title 
      the_divs = jobSoup.find_all("div", {"class":"header"})      
      #country = the_divs[1].find_all("span")[0].text
      #print(country)
      #the_job['location'] = country
      #date_posted = the_divs[1].find_all("span")[3].text
      #print(date_posted)
      #the_job['date_posted'] = date_posted
           
      
      
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

the_company = Company.objects.get(uniqueId='3519b5ad')

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
    

  )






