
#-*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from agency.models import Acount
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request,'home.html')


def registre(request):
    if request.method=='POST':
        username=request.POST.get('name')
        if username=='' or len(username)<=3:
            messages.success(request, ("check your name"))
            return redirect('registre')
        lastname=request.POST.get('lastname')
        if  lastname=='' or len(lastname)<=3:
            messages.success(request, ("check your lastname"))
            return redirect('registre')
        email=request.POST.get('email')
        if email=='':
            messages.success(request, ("empty email"))
            return redirect('registre')
        if len(email)<6:
            messages.success(request, ("email lower then 6 character"))
            return redirect('registre')

        for acounte in Acount.objects.all():
            if email==acounte.email:
                messages.success(request, ("this email is already existe"))
                return redirect('registre')
        pass1=request.POST.get('pass1')
        if pass1=='':
            messages.success(request, ("empty password "))
            return redirect('registre')

        pass2=request.POST.get('pass2')
        if pass2=='':
            messages.success(request, ("empty password confirme"))
            return redirect('registre')
        
        if pass2!=pass1:
            return HttpResponse("verify your password !")
        my_user=Acount(name=username,lastname=lastname,email=email,password=pass1)
        my_user.save()
        return redirect("login")
    return render(request, 'login&logout/registre.html')

def loginp(request):
    if request.method=='POST':
        email=request.POST.get('email')
        if email=='':
            messages.success(request, ("empty email"))
            return redirect('login')
        pass1=request.POST.get('pass')
        if  pass1=='':
            messages.success(request, ("empty password or password lower then 6"))
            return redirect('login')
        for acounte in Acount.objects.all():
            if email==acounte.email and pass1==acounte.password:
                return HttpResponse("<h1><center>congratulation you are login </center></h1>")
        messages.success(request, ("email or password is not correct"))       
    return render(request,'login&logout/login.html')

def propos(request):  
    return render(request, 'propos.html')

