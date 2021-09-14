import requests
from bs4 import BeautifulSoup
from datetime import date


headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

baseUrl = 'https://automattic.com/work-with-us/'
url = "https://automattic.com/work-with-us/"

r = requests.get(url, headers= headers)
c = r.content
soup = BeautifulSoup(c,"html.parser")

table = []
results = soup.find_all("a",{"class":"position-listing"})
[table.append(x) for x in results if x not in table]
# print(table)

def jobScan(link):
    the_job = {}
    jobUrl = link['href']
    # print(jobUrl)
    the_job['urlLink'] = jobUrl

    job = requests.get(jobUrl, headers=headers)
    jobC = job.content
    jobSoup = BeautifulSoup(jobC, "html.parser")
    # print(jobSoup)

    to_test = jobSoup.find_all("main", {"class":"tier"})
    # print(to_test)

    if to_test == []:
      return None
    else:
      title = jobSoup.find_all("h2")[0].text
      the_job['title'] = title 
      print(title)
      
      
      
     
      paragraphs = jobSoup.find_all("p")
      # print(paragraphs)
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
  # print(job)
  final_jobs.append(job)



# the_user = User.objects.get(username='admin')
the_company = Company.objects.get(uniqueId='e67103e4')

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













