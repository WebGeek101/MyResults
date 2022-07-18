import email
from os import uname_result
import time
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from website.models import *;

# Create your views here.
def signup(request):
    if request.method == 'POST':
        uname=request.POST['username']
        pwd=request.POST['password']
        pwd2=request.POST['password2']

        if pwd==pwd2:
            user=User.objects.create_user(username=uname, password=pwd)
            
            print("Signup successful")
            return redirect('/website/login')
        else:
            print("Wrong password")
        
    else:
        return render(request,'signup.html')     

def login(request):
    if request.method == 'POST':
        uname=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=uname,password=password)

        if user is not None:
            auth.login(request,user)
            request.session["username"] = uname 
            return redirect('/website/home')
        
        else:
            messages.warning(request, "Login failed") #not this above line
            return redirect('/website/login')

    else:
        return render(request,'login.html')

def home(request):
    return render(request,'home.html', {
        "username": request.session["username"]
    })

def insertmarks(request):
    if request.method == 'POST':
        score=markscard()
        score.sem=request.POST.get('sem')
        score.subcode=request.POST.get('subcode')
        score.sub=request.POST.get('sub')  
        score.marks=request.POST.get('marks')   
        score.save()
        print("Score saved successfully")
        return render(request, 'home.html')
    else :
        print("Score not saved successfully ")
        return render(request, 'insertmarks.html')
        
def viewmarks(request):
    return render(request, 'viewmarks.html')   

def display(request):
	mc=markscard.objects.all().filter(sem=7) # Collect all records from table 
	return render(request,'display.html',{'mc':mc})            
    