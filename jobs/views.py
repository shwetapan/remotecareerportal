from django.contrib import messages

from django.shortcuts import render
from .models import *
from .forms import *
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
from datetime import datetime, timedelta
import operator
from django.db.models import Q
from functools import reduce


# Create your views here.
def home(request):
   form = SearchForm()
   
   job_list=Jobs.objects.order_by('-date_posted')  
   voda_jobs = Jobs.objects.filter(company__title='Vodacom')
   signma_jobs = Jobs.objects.filter(company__title='11sigma')
   anka_jobs = Jobs.objects.filter(company__title='anka')
   automattic_jobs = Jobs.objects.filter(company__title='automattic')
  
  
   
   
   context = {}
  
   
  
   context['voda_jobs'] = voda_jobs
   context['signma_jobs'] = signma_jobs
   context['anka_jobs'] = anka_jobs
   context['automattic_jobs'] = automattic_jobs

   context['director'] = Category.objects.get(title='Director')
   context['manager'] = Category.objects.get(title='Manager')
   context['engineer'] = Category.objects.get(title='Engineer'  )
   context['specialist'] = Category.objects.get(title='Specialist')
   context['technology'] = Category.objects.get(title='Technology')
   context['consultant'] = Category.objects.get(title='Consultant')
   context['businessAnalyst'] = Category.objects.get(title='Business Analyst')
   context['projectManager'] = Category.objects.get(title='Project Manager')
   job_list=Jobs.objects.order_by('-date_posted')
   context['jobs'] = job_list
 

  #------------Query for software developer jobs-------------------------#
   # qs = Jobs.objects.all()
   # for search_term in ('Developer', 'Engineer', 'Software'):
   #    software_jobs = qs.filter(title__contains=search_term)
   # context['software_jobs']=software_jobs
  
   paginator_method(request, context)



   
  
   #-------------------- Handling Paginator -----------------------------#

   
   
   #-------------------- Handling The Post Request on The Form ----------#
   
   context['form'] = form

   if request.method == 'POST':
      form = SearchForm(request.POST)
      if form.is_valid():

         # send email to user
         search = form.cleaned_data.get('title')
         search_typeofjob = form.cleaned_data.get('typeofjob')
         print(search)
         print(search_typeofjob)

         

         jobs=[]
         if len(search.split())>1:
            search_list = search.split()
            item_list = []
            for item in search_list:
               a_list = Jobs.objects.filter(title__icontains=item)
               for x in a_list:
                  item_list.append(x)
            [jobs.append(x) for x in item_list if x not in jobs]
            
            return render(request,'job-list.html',{'jobs':jobs})
         else:
            # query the database for search term in title
            if(search or search_typeofjob):
               jobs = Jobs.objects.filter(title__icontains=search)
            elif(search_typeofjob):
               jobs = Jobs.objects.filter(job_type__icontains=search_typeofjob)
            elif(search_typeofjob=='Remote'):
               jobs = Jobs.objects.filter(location__icontains=search_typeofjob)
               print(jobs)
            elif(search & search_typeofjob):
               jobs = Jobs.objects.filter(Q(title__icontains=search) | Q(job_type__icontains=search_typeofjob ))
               # return the job list HTML with this query set only..
            return render(request,'job-list.html',{'jobs':jobs})

      else:
         messages.error(request,'Error Processing Your Request')
         context['form'] = form
         return render(request,'home.html',context)
       
   return render(request,'home.html',context)

def pagination_filter(context, request, software_jobs):
   job_list_var = software_jobs
   page = request.GET.get('page', 1)
   paginator = Paginator(job_list_var, 10)
   try:
      job_var = paginator.page(page)
   except PageNotAnInteger:
      job_var = paginator.page(1)
   except EmptyPage:
      job_var = paginator.page(paginator.num_pages)
   context['jobs'] = job_var



   

def job_list(request):
      
   #------------ Pagination ---------------#
   job_list_var = Jobs.objects.order_by('-date_posted')
   page = request.GET.get('page', 1)

   paginator = Paginator(job_list_var, 30)
   try:
      job_var = paginator.page(page)
   except PageNotAnInteger:
      job_var = paginator.page(1)
   except EmptyPage:
      job_var = paginator.page(paginator.num_pages)

   return render(request,'job-list.html',{'jobs':job_var})

def job_detail(request, slug):
   the_job = Jobs.objects.get(slug=slug)

   return render(request, 'job-detail.html', {'object':the_job})

def category_detail(request, slug):
   the_category = Category.objects.get(slug=slug)
   context = {}

   jobs = Jobs.objects.filter(category__slug = slug)[:20]
   context['jobs'] = jobs
   context['the_category'] = the_category
   return render(request, 'category-detail.html', context)

def paginator_method(request, context):
   job_list_var = Jobs.objects.order_by('-date_posted')
   page = request.GET.get('page', 1)

   paginator = Paginator(job_list_var, 10)
   try:
      job_var = paginator.page(page)
   except PageNotAnInteger:
      job_var = paginator.page(1)
   except EmptyPage:
      job_var = paginator.page(paginator.num_pages)
   context['jobs'] = job_var



