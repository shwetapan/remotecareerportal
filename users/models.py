from django.db import models
from django.db.models.base import Model
from django.template.defaultfilters import default, slugify
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from uuid import uuid4
import random
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Resume(models.Model):
  
  BLACK = 'Black'
  WHITE = 'White'
  COLOURED = 'Coloured'
  INDIAN = 'Indian' 
  CHINESE = 'Chinese'
  Other ='Other'

  MALE = 'Male'
  FEMALE = 'Female'
  OTHER = 'Other'
  MARRIED = 'Married'
  SINGLE = 'Single'
  WIDOWED = 'Widowed'
  DIVORCED = 'Divorced'

  Singapore = ' Singapore'
  Hong_Kong = ' Hong-Kong'
  India = 'India'
  United_Arab_Emirates = 'United_Arab_Emirates'
  LIMPOPO = 'Limpopo'
  WESTERN_CAPE = 'Western-cape'
  NORTHERN_CAPE = 'Northern-cape'
  EASTERN_CAPE = 'Estern-cape'
  KWAZULU_NATAL = 'Kwazulu-natal'
  USA ='Usa'
  Other = 'Other'


  ETHNIC_CHOICES = [
  (BLACK, 'Black'),
  (WHITE, 'White'),
  (COLOURED, 'Coloured'),
  (INDIAN, 'Indian'),
  (CHINESE, 'Chinese'),
  (OTHER, 'Other'),
  ]
  
  SEX_CHOCES = [
  (MALE, 'Male'),
  (FEMALE, 'Female'),
  (OTHER, 'Other'),
  ]

  MARITAL_CHOICES = [
  (MARRIED, 'Married'),
  (SINGLE, 'Single'),
  (WIDOWED, 'Widowed'),
  (DIVORCED, 'Divorced'),
  ]

  PROVINCE_CHOICES = [
    (India,'India'),
    (Singapore, ' Singapore'),
    ( Hong_Kong, ' Hong-Kong'),
    ( United_Arab_Emirates, ' United_Arab_Emirates'),
    (LIMPOPO, 'Limpopo'),
    (WESTERN_CAPE,'Western-cape'),
    (NORTHERN_CAPE,'Northern-cape'),
    (EASTERN_CAPE,'Estern-cape'),
    (KWAZULU_NATAL,'Kwazulu-natal'),
    (USA,'Usa'),
    (Other,'Other'),
  ]

  ETHNIC_CHOICES = [
    (BLACK, 'Black'),
    (WHITE, 'White'),
    (COLOURED, 'Coloured'),
    (INDIAN, 'Indian'),
    (CHINESE, 'Chinese'),
    (Other,'Other'),

  ]

  SEX_CHOICES = [
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (OTHER, 'Other'),
  ]

  IMAGES = [
    'profile1.jpg','profile2.jpg','profile3.jpg','profile4.jpg','profile5.jpg',
    'profile6.jpg','profile7.jpg','profile8.jpg','profile9.jpg','profile10.jpg',
  ]

  user = models.OneToOneField(User, on_delete=models.CASCADE)
  uniqueId = models.CharField(null=True,blank=True, max_length=100)
  image  = models.ImageField(default='default.jpg', upload_to = 'media')
  email_confirmed = models.BooleanField(default=False)
  date_birth = models.DateField()
  ethnicity = models.CharField(choices=ETHNIC_CHOICES, default=BLACK, max_length=200)
  sex = models.CharField(choices=SEX_CHOCES, default=OTHER, max_length=100)
  marital_status = models.CharField(choices=MARITAL_CHOICES,default=SINGLE, max_length=100)
  addressLine1 = models.CharField(null=True,blank=True, max_length=100)
  addressLine2 = models.CharField(null=True,blank=True, max_length=100)
  suburb = models.CharField(null=True,blank=True, max_length=100)
  city = models.CharField(null=True,blank=True, max_length=100)
  province = models.CharField(choices=PROVINCE_CHOICES,default=India, max_length=200)
  phonenumber = models.CharField(null=True,blank=True, max_length=100)
  slug = models.SlugField(max_length=500, unique=True,blank=True,null=True)
  date_created = models.DateTimeField(default=timezone.now)
  last_updated = models.DateTimeField(null=True,blank=True)
  cover_letter = models.FileField(upload_to = 'resumes', null=True,blank=True)
  cv = models.FileField(upload_to = 'resumes',null=True,blank=True)

  def __str__(self):
    return '{} {} {}'.format(self.user.first_name, self.user.last_name, self.uniqueId)

  def get_absolute_url(self):
    return reverse('resume-detail', kwargs={'slug': self.slug})

  def save(self, *args, **kwargs):
    # creating unique self identifier for resume(useful for other things in future)
    if self.uniqueId is None:
      self.uniqueId = str(uuid4()).split('-')[0]
      self.slug = slugify('{} {} {}'.format(self.user.first_name, self.user.last_name, self.uniqueId))

    # assign default profile image
    if self.image == 'default.jpg':
      self.image = random.choice(self.IMAGES)

    # keep track of everytime someone updates resume, everytime the imstance is saved-this should update
    self.slug = slugify('{} {} {}'.format(self.user.first_name, self.user.last_name, self.uniqueId))

    super(Resume,self).save(*args, **kwargs)


class Education(models.Model):
  LEVEL5A = 'NQF 5 - Certificate'
  LEVEL5B = 'NQF 5 - Higher Certificate'
  LEVEL5C = 'NQF 5 - First Diploma'
  LEVEL6A = 'NQF 6 - Bachelors Degree'
  LEVEL6B = 'NQF 6 - Professional First Degree Postgraduate'
  LEVEL6C = 'NQF 6 - General First Degree'
  LEVEL7A = 'NQF 7 - Postgraduate Diploma'
  LEVEL7B = 'NQF 7 - Honours Degree'
  LEVEL7C = 'NQF 7 - Masters Degree'
  LEVEL8 = 'NQF 8 - Doctors Degree'

  LEVEL_CHOICES = [
  (LEVEL5A , 'NQF 5 - Certificate'),
  (LEVEL5B , 'NQF 5 - Higher Certificate'),
  (LEVEL5C , 'NQF 5 - First Diploma'),
  (LEVEL6A , 'NQF 6 - Bachelors Degree'),
  (LEVEL6B , 'NQF 6 - Professional First Degree Postgraduate'),
  (LEVEL6C , 'NQF 6 - General First Degree'),
  (LEVEL7A , 'NQF 7 - Postgraduate Diploma'),
  (LEVEL7B , 'NQF 7 - Honours Degree'),
  (LEVEL7C , 'NQF 7 - Masters Degree'),
  (LEVEL8 , 'NQF 8 - Doctors Degree'),
  ]

  institution = models.CharField(null=True,blank=True, max_length=200)
  qualification = models.CharField(null=True,blank=True, max_length=200)
  level = models.CharField(choices=LEVEL_CHOICES, default=LEVEL5A, max_length=200)
  start_date = models.DateField(null=True,blank=True)
  graduated = models.DateField(null=True,blank=True)
  major_subject = models.CharField(null=True,blank=True, max_length=200)
  date_created = models.DateTimeField(default=timezone.now)
  resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
  

  def __str__(self):
    return '{} for {}{}'.format(self.qualification, self.resume.user.first_name, self.resume.user.last_name)


class Experience(models.Model):
  company = models.CharField(null=True, blank=True, max_length=200)
  position = models.CharField(null=True, blank=True, max_length=200)
  start_date = models.DateField(null=True, blank=True)
  end_date = models.DateField(null=True, blank=True)
  experience = models.TextField(null=True, blank=True)
  skills = ArrayField(models.CharField(null=True, blank=True, max_length=100))
  date_created = models.DateTimeField(default=timezone.now)
  resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

  def __str__(self):
      return '{} at {}'.format(self.position, self.company)
  





  







  
  
  



 