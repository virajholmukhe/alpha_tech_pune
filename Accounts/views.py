from hmac import new
from django.contrib.auth.models import User
from django.db.models.fields import EmailField
from django.shortcuts import redirect, render
from AdminApp.models import Product, Categories
from Accounts.models import UserInfo
from UserApp.models import MyCart
from django.contrib import messages
from UserApp.views import *
from .send_email import send_forget_pass_mail,send_activation_mail
import uuid
from .models import EmailUsers

def register(request):
    if(request.method=="GET"):
        request.session.clear()
        cat=Categories.objects.all()
        return render(request,"Register.html",{"cat":cat})
    else:
        username=request.POST["uname"]
        email=request.POST["uemail"]
        password=request.POST["upass"]
        firstname=request.POST["fname"]
        lastname=request.POST["lname"]

        if UserInfo.objects.filter(username=username).exists():
            return render(request,"Register.html",{"exist":"username: "+username+" is already exist"})
        elif UserInfo.objects.filter(email=email).exists():
            return render(request,"Register.html",{"exist":"email ID: "+email+" is already exist"})
        else:
            new_user=UserInfo()
            new_user.first_name = firstname
            new_user.last_name = lastname
            new_user.username = username
            new_user.email=email
            new_user.password=password
            new_user.save()
            return redirect(login)

def login(request):
    if(request.method=="GET"):
        request.session.clear()
        return render(request,"Login.html",{})
    else:
        username=request.POST["uname"]
        password=request.POST["upass"]
        try:
            u1 = UserInfo.objects.get(username=username,password=password)
            request.session["uname"]=username
        except:
            messages.error(request, 'invalid username or password')
            return render(request,"Login.html")
        return redirect("home")

def logout(request):
    request.session.clear()
    return redirect(login)

def forgetPass(request):
    if request.method=="GET":
        return render(request,"pass_reset.html")
    else:
        email=request.POST["email"]
        try:
            UserInfo.objects.get(email=email)
            try:
                EmailUsers.objects.get(email=email)
                token = str(uuid.uuid4())
                obj = EmailUsers.objects.get(email=email)
                obj.token = token
                obj.save()
            except:
                obj = EmailUsers.all()
                token = str(uuid.uuid4())
                obj.email = email
                obj.token = token
                obj.save()
            send_forget_pass_mail(email,token)
            return render(request,"pass_reset_done.html")
        except:
            messages.error(request, 'Entered email id is not registered.')
            return render(request,"pass_reset.html")

def checkToken(request,token):
    if request.method=="GET":
        try:
            obj=EmailUsers.objects.get(token=token)
            print(obj)
            email=obj.email
            return render(request,"pass_reset_confirm.html",{"email":email})
        except:
            messages.error(request, 'Un-Authorized link or invalid link... try again')
            return render(request,"pass_reset.html")
    else:
        email = request.POST["email"]
        pass1 = request.POST["upass1"]
        pass2 = request.POST["upass2"]
        if(pass1==pass2):
            obj=UserInfo.objects.get(email=email)
            obj.password=pass1
            obj.save()
            return render(request,"pass_reset_complete.html")
        else:
            messages.error(request, 'Password did not matched ')
            redirect(checkToken)

def changePass(request):
    pass
