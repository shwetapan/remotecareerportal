from django import forms
from .models import *


class SearchForm(forms.ModelForm):
  Remote = 'Remote'
  Full_Time = 'Full Time'
  Part_Time = 'Part Time'
  Contract = 'Contract'
  

  JOBTYPE_CHOICES = [
  (Remote, 'Remote'),
  (Full_Time, 'Full_Time'),
  (Part_Time,'Part_Time'),
  (Contract, 'Contract'),
   ('Internship', 'Internship'),
  
  ]

  title = forms.CharField(
    required=False,
    widget=forms.TextInput(attrs={'class':'form-control rounded registration-input-box','placeholder':'Enter Job title, keyword or company name'})
  )
  typeofjob = forms.CharField(
    required=False,
    widget= forms.Select(choices = JOBTYPE_CHOICES, attrs={'class':'form-control rounded registration-input-box'}),
  )
 

  class Meta:
    model = Jobs
    fields = ['title','typeofjob'] 


    
  
