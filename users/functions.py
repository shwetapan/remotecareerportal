from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.views.static import serve
import os
from django.shortcuts import render

class ForgotEmail():
  def __init__(self,new_pass):
    self.new_pass = new_pass

  subject = '[Remote Careers Portal] Forgot your password'

  def email(self):
    return{
      "title" : "Your password has been reset",
      "shortDescription" : "You have requested a new password",
      "subtitle" : "Please find your new password attached for remote career portal",
      "message" : "Your new password is: {}, If you did not request new password, please contact admin@remotecareerportal.com immediately. Otherwise, kindly login to your profile with your new password and change it online.".format(self.new_pass)
      }

class WelcomeEmail():
  subject = '[Remote Careers Portal] Welcome to Remote Careers Portal'
  email= {
    "title" : "Thankyou for registering with Remote Careers Portal",
    "shortDescription" : "Welcome to Remote Careers Portal, World's leading job search engine. These are the next steps.",
   
    "message" : "You have successfully registered with Remote Careers Portal. You can login to your porfile and start creating a profile. We have thousands of jobs just waiting for you to apply. If you experience any difficulties with our portal, simply email our admin team at admin@remotecareerportal.com. Good luck "
    }



def sendEmail(email, subject, to_email):
 
   from_email = settings.EMAIL_HOST_USER
   to_email = ['7spandey@gmail.com']
   text_content = """
   {}

   {}

   {}

   regards,
   Remote Career's Portal
   """. format(email['shortDescription'],email['subtitle'],email['message'])

   html_c = get_template('basic-email.html')
   d = {'email':email}
   html_content = html_c.render(d)

   msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
   msg.attach_alternative(html_content,'text/html')
   msg.send()

   




   
    


