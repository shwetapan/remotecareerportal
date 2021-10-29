import users
from django.shortcuts import render,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
from .functions import *
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from datetime import datetime
from django.contrib.auth.models import User
from uuid import uuid4




# Create your views here.
def register(request):
  if request.method=='GET':
    form = RegisterForm()
    context = {'form': form}
    return render(request,'register.html',context)
  
  
  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
      form.save()

        # send email to user
      to_email = form.cleaned_data.get('email')
      welcome = WelcomeEmail()
      sendEmail(welcome.email,welcome.subject,welcome.subject,to_email)

        # send success message to user
      user = form.cleaned_data.get('username')
      messages.success(request,'Account was created for user: ' + user + ' Please Login now:')
      return redirect('login')
    else:
      messages.error(request,'Error Processing Your Request')
      context = {'form':form}
      return render(request,'register.html',context)

  return render(request,'register.html',{})

@login_required
def user_profile(request):
  return render(request,'profile.html',{})

@login_required
def create_resume(request):
    if request.method == 'POST':
      form = ResumeForm(request.POST, request.FILES)
      if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        context = {'form':form}
        messages.success(request,'Resume Created Successfully')
        return redirect('profile')
      else:
        messages.error(request,'Error Processing Your Request')
        context = {'form':form}
        return render(request,'create-resume.html', context)

    if request.method == 'GET':
      form = ResumeForm()
      context = {'form':form}    
      return render(request,'create-resume.html',context)

    return render(request,'create-resume.html',{})


@login_required
def resume_detail(request, slug):
  obj = Resume.objects.get(slug=slug)
  educations = Education.objects.filter(resume=obj)
  experiences = Experience.objects.filter(resume=obj)
  context = {}
  context['object'] = obj
  context['educations'] = educations
  context['experiences'] = experiences

  if request.method == 'POST':
    edu_form = EducationForm(request.POST)
    exp_form = ExperienceForm(request.POST)
    
    if edu_form.is_valid():
      o = edu_form.save(commit=False)
      o.resume = obj
      o.save()

      messages.success(request,'Resume Updated Successfully ')
      return redirect('resume-detail',slug=slug)
      
    
   
    if exp_form.is_valid():
      o = exp_form.save(commit=False)
      o.resume = obj
      o.save()

      messages.success(request,'Resume Updated Successfully ')
      return redirect('resume-detail',slug=slug)

    else:
      messages.error(request,'Error Processing Your Request')
      context['exp_form'] = exp_form
      return render(request,'resume-detail.html',context)

  if request.method == 'GET':
    edu_form = EducationForm()
    exp_form = ExperienceForm()
    context['edu_form'] = edu_form
    context['exp_form'] = exp_form
    return render(request,'resume-detail.html',context)
  
  return render(request,'resume-detail.html',context)


def download(request, foldername, filename):
  file_path = settings.MEDIA_ROOT +'/'+foldername+'/'+filename
  return serve(request, os.path.basename(file_path),os.path.dirname(filename))


def forgot(request):
  if request.method == 'POST':
    form = ForgotForm(request.POST)
    if form.is_valid:
      user_email = request.POST['email'].lower().replace(' ','')

      u = User.objects.get(email = user_email)
      if u is not None:

        new_pass = str(uuid4()).split('-')[4]

        forgot = ForgotEmail(new_pass)

        # send the forgot email...
        to_email = u.email
        e_mail = forgot.email()
        sendEmail(e_mail, forgot.subject, [to_email])

        u.set_password(new_pass)
        u.save()

        messages.success(request, 'Your password has been reset, check your email for more details')
        return redirect('login')
      
      else:
        messages.error(request,"we could not find user with matching email ")
        return redirect('home_page')
      
    else: 
      messages.error(request,'Error processing your request')
      context = {'form':form}
      return render(request, 'forgot.html',context)

  if request.method == 'GET':
    form = ForgotForm()
    context = {'form':form}
    return render(request, 'forgot.html',context)

  return render(request, 'forgot.html',{})


      


