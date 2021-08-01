from django.db.models import query
from django.shortcuts import redirect, render
from AdminApp.models import Product,Categories
from Accounts.models import ContactUs, UserInfo, EmailUsers
from UserApp.models import CustBuild, MyCart
from django.contrib import messages
from Accounts.views import login,logout,register
from django.conf import settings
import requests

# Create your views here.

def home(request):
    pro=Product.objects.all()
    cat=Categories.objects.all()
    return render(request,"Home.html",{"pro":pro,"cat":cat})

def showCategories(request,cid):
    cat=Categories.objects.all()
    pro=Product.objects.filter(category_id=cid)
    return render(request,"Home.html",{"pro":pro,"cat":cat})

def filterByPrice_hl(request):
    pro=Product.objects.all().order_by("-price")
    cat=Categories.objects.all()
    return render(request,"Home.html",{"pro":pro,"cat":cat})

def filterByPrice_lh(request):
    pro=Product.objects.all().order_by("price")
    cat=Categories.objects.all()
    return render(request,"Home.html",{"pro":pro,"cat":cat})

def filterByName_AZ(request):
    pro=Product.objects.all().order_by("name")
    cat=Categories.objects.all()
    return render(request,"Home.html",{"pro":pro,"cat":cat})

def filterByName_ZA(request):
    pro=Product.objects.all().order_by("-name")
    cat=Categories.objects.all()
    return render(request,"Home.html",{"pro":pro,"cat":cat})

def searchProduct(request):
    query = request.GET["q"]
    pro = Product.objects.filter(name__icontains=query)
    cat=Categories.objects.all()
    return render(request,"Home.html",{"pro":pro,"cat":cat})

def showProduct(request,pid):
    cat=Categories.objects.all()
    product=Product.objects.get(id=pid)
    cat_id=product.category_id
    cats=Product.objects.filter(category_id=cat_id)
    return render(request,"ShowProduct.html",{"product":product,"cat":cat,"cats":cats,"pid":pid})

def addToCart(request):
    if("uname" in request.session):
        u = UserInfo.objects.get(username=request.session["uname"])
        p = Product.objects.get(id=request.POST["pid"])
        c = Categories.objects.get(id=request.POST["cid"])
        qty = request.POST["qty"]

        action = request.POST["action"]
        if(action == "add_to_cart"):
            try:
                cart = MyCart.objects.get(user=u,product=p)
                messages.error(request,"Product is already in Cart")
            except:
                cart = MyCart()
                cart.user=u
                cart.product=p
                cart.qty=qty
                cart.save()
                messages.success(request,"Product is successfully added in Cart")
            return redirect(showCart)
        else:
            try:
                build = CustBuild.objects.get(user=u,category=c)
                messages.error(request,"Component already selected")
            except:
                build = CustBuild()
                build.user=u
                build.product=p
                build.category=c
                build.save()
                messages.success(request,"Component added successfull")
            return redirect(showBuild)

    else:
        return redirect(login)

def showCart(request):
    if(request.method=="GET"):
        if("uname" in request.session):
            cart = MyCart.objects.filter(user = request.session["uname"])
            cat = Categories.objects.all()
            total = 0
            for item in cart:
                total += item.qty * item.product.price
            request.session["total"] = total
            return render(request,"ShowCart.html",{"cart":cart,"cat":cat}) 
        else:
            return redirect(login)
    else:
        action = request.POST["action"]
        pid= request.POST["pid"]
        item = MyCart.objects.get(user = request.session["uname"],
                                product = Product.objects.get(id=pid))

        if(action == "update"):
            qty  = request.POST["cart_qty"]
            item.qty = qty
            item.save()
        else:
            item.delete()
        return redirect(showCart)

def showBuild(request):
    if(request.method=="GET"):
        if("uname" in request.session):
            build = CustBuild.objects.filter(user_id=request.session["uname"])
            cat = Categories.objects.all()
            return render(request,"custom_build.html",{"build":build,"cat":cat})
        else:
            return redirect(login)
    else:
        action = request.POST["action"]
        bid= request.POST["bid"]
        item = CustBuild.objects.get(user_id = request.session["uname"], product_id = Product.objects.get(id=bid))

        if(action == "update"):
            qty  = request.POST["cart_qty"]
            item.qty = qty
            item.save()
        else:
            item.delete()
        return redirect(showBuild)
    
def showProfile(request):
    if(request.method=="GET"):
        if("uname" in request.session):
            profile=UserInfo.objects.get(username=request.session["uname"])
            return render(request,"profile.html",{"profile":profile})

def editProfile(request):
    if(request.method=="GET"):
        if("uname" in request.session):
            profile=UserInfo.objects.get(username=request.session["uname"])
            return render(request,"profile-edit.html",{"profile":profile})
        else:
            redirect(login)
    else:
        if(UserInfo.objects.get(username=request.session["uname"])):
            profile1=UserInfo.objects.get(username=request.session["uname"])
            profile1.first_name=request.POST["first_name"]
            profile1.last_name=request.POST["last_name"]
            profile1.email=request.POST["email"]
            profile1.phone=request.POST["mobile"]
            profile1.address=request.POST["address"]
            profile1.occupation=request.POST["occupation"]
            profile1.save()
            return redirect(showProfile)
        else:
            pass
    
def contactUS(request):
    if(request.method=="GET"):
        return render(request,"contact_us.html",{})
    else:
        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,'response': recaptcha_response}
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        ''' End reCAPTCHA validation '''

        if result['success']:
            c=ContactUs()
            c.name=request.POST["name"]
            c.email=request.POST["email"]
            c.message=request.POST["message"]
            c.save()
            messages.success(request, 'New comment added with success!')
        else:
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')
        return redirect(contactUS)