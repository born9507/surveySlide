from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from .models import Profile
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate as django_authenticate
from django.http import JsonResponse

def signup(request):
    if request.method=='POST':
        if request.POST['password1'] == request.POST['password2']:
            user=User.objects.create_user(username=request.POST['username'], password=request.POST['password1'], email=request.POST['email'], first_name=request.POST['first_name'], last_name=request.POST['last_name'])
            auth.login(request,user)
            return redirect('index')
    return render(request, 'index')

def changeinfo(request, id):
    user=User.objects.get(id=id)
    if request.method=='POST':
        User.objects.filter(id=id).update(username=request.POST['username'])
        Profile.objects.filter(user=user).update(college=request.POST['college'], major=request.POST['major'])
        user.refresh_from_db()
        return render(request, 'account/myinfo.html')
    else:
        return render(request, 'account/changeinfo.html')

def myinfo(request, id):
    user=User.objects.get(id=id)
    return render(request, 'account/myinfo.html')

def login(request):
    return render(request, 'account/login.html')

def logout(request):
    return render(request, 'account/logout.html')