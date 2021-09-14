from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.forms import fields
from django.utils.translation import gettext, gettext_lazy as _
from .models import Resume, Education, Experience

class DateInput(forms.DateInput):
  input_type = 'date'

class RegisterForm(UserCreationForm):
  email = forms.EmailField(
    max_length=100,required=True,help_text='Enter Email Address',
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
    )

  first_name = forms.CharField(
    max_length=100,required=True,help_text='Enter First Name',
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
    )
  
  last_name = forms.CharField(
    max_length=100,required=True,help_text='Enter Last Name',
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
    )

  username = forms.CharField(
    max_length=200,required=True,help_text='Enter UserName',
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
    )
  
  password1 = forms.CharField(
    help_text='Enter Password', required=True,
    widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
    )

  password2 = forms.CharField(
    help_text='Enter Password Again', required=True,
    widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password Again'}),
    )
  check = forms.BooleanField(required=True)

  class Meta:
    model = User
    fields = [
      'username','email','first_name','last_name','password1','password2','check',
    ]


class LoginForm(AuthenticationForm):
  username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class':'form-control'}))
  password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control'}))
 



  
class ResumeForm(forms.ModelForm):
  BLACK = 'Black'
  WHITE = 'White'
  COLOURED = 'Coloured'
  INDIAN = 'Indian'
  CHINESE = 'Chinese'

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
  ]

  SEX_CHOICES = [
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (OTHER, 'Other'),
  ]


  image  = forms.ImageField(
    required=False,
    widget=forms.FileInput(attrs={'class':'form-control'})
  )
  
  date_birth = forms.DateField(
     required=True,
    widget=DateInput(attrs={'class':'form-control','placeholder':'Enter a date: '},)
  )
  ethnicity = forms.ChoiceField(
    choices=ETHNIC_CHOICES, 
    widget=forms.Select(attrs={'class':'nice-select rounded'}),
  )

  sex = forms.ChoiceField(
    choices=SEX_CHOICES, 
    widget=forms.Select(attrs={'class':'nice-select rounded'}),
  )

  marital_status = forms.ChoiceField(
    choices=MARITAL_CHOICES, 
    widget=forms.Select(attrs={'class':'nice-select rounded'}),
  )
  addressLine1 = forms.CharField(
    required=True,
    widget=forms.TextInput(attrs={'class':'form-control resume','placeholder':'Enter Address Line1: '}),
  )
  addressLine2 = forms.CharField(
    required=False,
    widget=forms.TextInput(attrs={'class':'form-control resume','placeholder':'Enter Address Line2: '}),
  )
  suburb = forms.CharField(
    required=True,
    widget=forms.TextInput(attrs={'class':'form-control resume','placeholder':'Enter Suburb: '}),
  )
  city = forms.CharField(
    required=True,
    widget=forms.TextInput(attrs={'class':'form-control resume','placeholder':'Enter City: '}),
  )
  
  province = forms.ChoiceField(
    choices = PROVINCE_CHOICES, 
    widget = forms.Select(attrs={'class':'nice-select rounded'}),
  )

  phonenumber = forms.CharField(
    required=False,
    widget=forms.TextInput(attrs={'class':'form-control resume','placeholder':'Enter Phone Number'}),
  )

  cover_letter = forms.FileField(
    required=False,
    widget=forms.FileInput(attrs={'class':'form-control'})
  )
  cv = forms.FileField(
    required=False,
    widget=forms.FileInput(attrs={'class':'form-control'})
  )

  class Meta:
    model = Resume
    fields = [
      'image',
      'date_birth',
      'ethnicity',
      'sex',
      'marital_status',
      'addressLine1',
      'addressLine2',
      'suburb',
      'city',
      'province',
      'phonenumber',
      'cover_letter',
      'cv',
    ]
    
class EducationForm(forms.ModelForm):
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

  institution = forms.CharField(
    required=True,
    widget=forms.TextInput(attrs={'class':'form-control resume','placeholder':'Name of Institution'}),
  )
  qualification = forms.CharField(
    required=True,
    widget=forms.TextInput(attrs={'class':'form-control resume','placeholder':'Name of Qualification'}),
  )
  level = forms.ChoiceField(
    choices=LEVEL_CHOICES,
    widget=forms.Select(attrs={'class':'nice-select rounded'}),
  )
  start_date = forms.DateField(
    required=True,
    widget=DateInput(attrs={'class':'form-control','placeholder':'Enter a Date:'}),
  )
  graduated = forms.DateField(
    required=True,
    widget=DateInput(attrs={'class':'form-control','placeholder':'Enter a Date:'}),
  )
  major_subject = forms.CharField(
    required=False,
    widget=forms.TextInput(attrs={'class':'form-control resume','placeholder':'Major Subjects'}),
  )

  class Meta:
    model = Education
    fields = [
      'institution',
      'qualification',
      'level',
      'start_date',
      'graduated',
      'major_subject',

    ]





class ExperienceForm(forms.ModelForm):
  company = forms.CharField(
    required=True,
    widget=forms.TextInput(attrs={'class':'form-control resume','placeholder':'Company Worked For'}),
  )

  position = forms.CharField(
    required=True,
    widget=forms.TextInput(attrs={'class':'form-control resume','placeholder':'Position/Role'}),
  )
  start_date = forms.DateField(
    required=True,
    widget=DateInput(attrs={'class':'form-control','placeholder':'Enter a date:'}),
  )
  end_date = forms.DateField(
    required=True,
    widget=DateInput(attrs={'class':'form-control','placeholder':'Enter a date:'}),
  )
  experience = forms.CharField(
    required=True,
    widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Experience'}),
  )

  skills = forms.CharField(
    required=False,
    widget=forms.TextInput(attrs={'class':'form-control resume','placeholder':'Enter Skill seperated by '}),
  )

  class Meta:
    model = Experience
    fields = [
      'company',
      'position',
      'start_date',
      'end_date',
      'skills',
      ]

class ForgotForm(forms.ModelForm):
  email = forms.EmailField(
    max_length=100,
    required=True,
    help_text='Enter Email Address',
    widget=forms.TextInput(attrs={'class':'form-control','  placeholder':'Enter Email'}),
    )

  class Meta:
    model = User
    fields = ['email']

  

