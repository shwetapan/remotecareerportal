from django.template.defaultfilters import title
import requests
from bs4 import BeautifulSoup
from datetime import date


headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

baseUrl = 'https://careers.vodafone.com'
url = "https://careers.vodafone.com/Vodacom/search/?createNewAlert=false&q="

r = requests.get(url, headers= headers)
c = r.content
soup = BeautifulSoup(c,"html.parser")

table = []
results = soup.find_all("a",{"class":"jobTitle-link"})
[table.append(x) for x in results if x not in table]

def jobScan(link):
    the_job = {}
    jobUrl = '{}{}'.format(baseUrl, link['href'])
    the_job['urlLink'] = jobUrl

    job = requests.get(jobUrl, headers=headers)
    jobC = job.content
    jobSoup = BeautifulSoup(jobC, "html.parser")

    to_test = jobSoup.find_all("div", {"class":"joblayouttoken displayDTM"})

    if to_test == []:
      return None
    else:
      title = jobSoup.find_all("h1")[0].text
      the_job['title'] = title 
      the_divs = jobSoup.find_all("div", {"class":"joblayouttoken displayDTM"})
      country = the_divs[1].find_all("span")[1].text
      the_job['location'] = country
      date_posted = the_divs[2].find_all("span")[1].text
      the_job['date_posted'] = date_posted
      full_part_time = the_divs[3].find_all("span")[1].text
      the_job['full_part_time'] = full_part_time
      the_job['type'] = 'Full Time'
      contract_type = the_divs[4].find_all("span")[1].text
      the_job['contract_type'] = contract_type  
      body = the_divs[5].find_all("span",{"class":"jobdescription"})
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



the_user = User.objects.get(email = ' ')
the_company = Company.objects.get(uniqueId='fbdf810d')

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
    location = test_job['location'],
    type = test_job['type'],
    contract_type = test_job['contract_type'],
    urlLink = test_job['urlLink'],
    date_posted = date.today(),
    description = test_job['description'],
    company = the_company,
    owner = the_user,

  )













