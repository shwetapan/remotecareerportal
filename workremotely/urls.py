"""workremotely URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.contrib import admin
from django.urls import path
from jobs import views as job_views
from users import views as users_views
from blog import views as blog_views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',job_views.home,name='home_page'),
    path('register/',users_views.register, name='register'),
    path('profile/',users_views.user_profile, name='profile'),
    path('users/create/', users_views.create_resume,name='create-resume'),
    path('users/view/<slug:slug>/', users_views.resume_detail,name='resume-detail'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('jobs/',job_views.job_list, name='job-list'),
    path('jobs/<slug:slug>/',job_views.job_detail, name='job-detail'),
    path('jobs/category/<slug:slug>/',job_views.category_detail,name='category-detail'),
    path('forgot-password/',users_views.forgot,name='forgot'),
    path('password-change/',auth_views.PasswordChangeView.as_view(template_name='password-change.html'),name='password-change'),
    path('password-change-done/',auth_views.PasswordChangeView.as_view(template_name='password-change-done.html'),name='password-change-done'),
    path('download/<str:foldername>/<str:filename>/',users_views.download,name='download'),
    path('blog_homepage/', blog_views.home, name='blog_home'),
    path('blog/about/', blog_views.about, name='about'),
    path('blog/contact/', blog_views.contact, name='contact'),
    path('blog/dashboard/', blog_views.dashboard, name='dashboard'),
    path('blog/addpost/', blog_views.add_post, name='addpost'),
    path('blog/updatepost/<int:id>/', blog_views.update_post, name='updatepost'),
    path('blog/delete/<int:id>/', blog_views.delete_post, name='deletepost'),
    re_path(r'^uploads/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
