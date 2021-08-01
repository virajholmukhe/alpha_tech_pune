from django.core.mail import message, send_mail
from django.conf import settings

def send_activation_mail(email,token):
    
    subject = "Email Verification Process"
    message = f'click on link to Verify your Account: http://127.0.0.1:8000/change-password/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message,email_from,recipient_list)
    return True

def send_forget_pass_mail(email,token):
    
    subject = "Email Verification Process"
    message = f'click on link to Verify your Account: http://127.0.0.1:8000/change-password/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message,email_from,recipient_list)
    return True
