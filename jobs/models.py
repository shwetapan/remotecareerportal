from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from uuid import uuid4
from django.db.models.fields import NOT_PROVIDED
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField


class Company(models.Model):
  title = models.CharField(max_length=500,null=True,blank=True)
  description = models.TextField(null=True,blank=True)
  uniqueId = models.CharField(null=True,blank=True,max_length=100)
  companyLogo = models.ImageField(default = 'default.png',upload_to = 'media')
  slug = models.SlugField(max_length=500,unique=True,blank=True,null=True)
  seoDescription = models.CharField(max_length=500,null=True,blank=True)
  seoKeywords = models.CharField(max_length=500, null=True,blank=True)

  def __str__(self):
      return '{} - {}'.format(self.title, self.uniqueId)

  def get_absolute_url(self):
      return reverse("company-detail", kwargs={"slug": self.slug})

  def save(self, *args, **kwargs):
    
    if self.uniqueId is None:
      self.uniqueId = str(uuid4()).split('-')[0]
      self.slug = slugify('Company {} {}'.format(self.title, self.uniqueId))

    self.slug = slugify('Company {} {}'.format(self.title, self.uniqueId))
    self.seoDescription = 'Apply for {} jobs on Work Remotely, start your career journey today'.format(self.title)
    self.seoKeywords = '{} Jobs, Work Remotely, Apply Jobs'.format(self.title)
    
    super(Company, self).save(*args, **kwargs)

class Category(models.Model):
  title = models.CharField(max_length=500,null=True,blank=True)
  description = models.TextField(null=True,blank=True)
  uniqueId = models.CharField(null=True,blank=True,max_length=100)
  categoryImage = models.ImageField(default = 'category.png',upload_to = 'media')
  slug = models.SlugField(max_length=500,unique=True,blank=True,null=True)
  seoDescription = models.CharField(max_length=500,null=True,blank=True)
  seoKeywords = models.CharField(max_length=500, null=True,blank=True)

  def __str__(self):
      return '{} - {}'.format(self.title, self.uniqueId)

  def get_absolute_url(self):
      return reverse("category-detail", kwargs={'slug': self.slug})

  def save(self, *args, **kwargs):  
    if self.uniqueId is None:
      self.uniqueId = str(uuid4()).split('-')[0]
      self.slug = slugify('Category {} {}'.format(self.title, self.uniqueId))

    self.slug = slugify('Category {} {}'.format(self.title, self.uniqueId))
    self.seoDescription = 'Apply for {} Jobs online, start your career journey today'.format(self.title)
    self.seoKeywords = '{} Jobs, Work Remotely, Apply Jobs'.format(self.title)
    super(Category, self).save(*args, **kwargs)
  


#Create your models here.
class Jobs(models.Model):
  FULL_TIME = 'FT'
  PART_TIME = 'PT'
  REMOTE = 'RT'
  TIER1 ='t1'
  TIER2 = 't2'
  TIER3 = 't3'
  TIER4 = 't4'
  TIER5 = 't5'

  TYPE_CHOICES = [
    (FULL_TIME,'Full Time'),
    (PART_TIME, 'Part Time'),
    (REMOTE, 'Remote'),
  ]

  EXP_CHOICES = [
    (TIER1,'Less than 2 yrs'),
    (TIER2,'2yrs - 5yrs'),
    (TIER3,'5yrs - 10yrs'),
    (TIER4,'10yrs - 15yrs'),
    (TIER5,'More than 15 yrs'),

  ]
 
  title = models.CharField(max_length=1000, null=True,blank=True)
  company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True,blank=True)
  category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True,blank=True)
  location = models.CharField(max_length=1000, null=True,blank=True)
  salary = models.CharField(max_length=1000, null=True,blank=True)
  uniqueId = models.CharField( null=True,blank=True, max_length=100)
  job_type = models.CharField(max_length=100,choices=TYPE_CHOICES,default=NOT_PROVIDED)
  type = models.CharField(max_length=100,choices=TYPE_CHOICES,default=NOT_PROVIDED)
  salary = models.CharField(max_length=30, null=True, blank=True)
  company_description = RichTextField(blank=True, null=True)
  experience = models.CharField(max_length=100,choices=EXP_CHOICES,default=NOT_PROVIDED)
  summary = models.TextField( null=True,blank=True)
  description = RichTextField(null=True,blank=True)
  requirements = models.TextField(null=True,blank=True)
  duties = models.TextField(null=True,blank=True)
  enquiries = models.TextField(null=True,blank=True)
  applications = models.TextField(null=True,blank=True)
  note = models.TextField(null=True,blank=True)
  closing_date = models.DateField(null=True,blank=True)
  date_posted = models.DateField(null=True,blank=True)
  valid_until = models.CharField(max_length=100, null=True,blank=True)
  contract_type = models.CharField(max_length=1000,null=True,blank=True)
  date_created = models.DateTimeField(default=timezone.now)
  owner = models.ForeignKey(User,on_delete=models.CASCADE, null=True,blank=True)
  slug = models.SlugField(max_length=1000,unique=True,blank=True,null=True)
  seoDescription = models.CharField(max_length=1000,null=True,blank=True)
  seoKeywords = models.CharField(max_length=1000, null=True,blank=True)
  urlLink = models.CharField(max_length=1000, null=True,blank=True)
  last_date = models.DateField(null=True,blank=True)
  is_published = models.BooleanField(default=False,null=True,blank=True)
  is_closed = models.BooleanField(default=False,null=True,blank=True)
  timestamp = models.DateTimeField(auto_now=True,null=True,blank=True)
  


 

  def __str__(self):
      return '{} - {} - {}'.format(self.company, self.title,self.location)

  def get_absolute_url(self):
      return reverse("job-detail", kwargs={"slug": self.slug})

  def save(self, *args, **kwargs):
    
    if self.uniqueId is None:
      self.uniqueId = str(uuid4()).split('-')[0]
      self.slug = slugify('{} {} {}'.format( self.title, self.location, self.uniqueId))

    self.slug = slugify('{} {} {}'.format( self.title, self.location, self.uniqueId))
    self.seoKeywords = 'Work Remotely, Careers Portal, Online job application, full time jobs, part time jobs, get a job, apply for job, remote job, worldwide jobs, work from anywhere jobs, work remotely jobs, remote work jobs,  {}'.format( self.title)
    self.seoDescription = '{}'.format('Work Remotely {} Job application. Apply for job: , online today'.format( self.title, self.location ))
    super(Jobs, self).save(*args, **kwargs)
    