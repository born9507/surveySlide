from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect

def signup(request):
    if request.method=='POST':
        if request.POST['password1'] == request.POST['password2']:
            user=User.objects.create_user(username=request.POST['username'], password=request.POST['password1'], email=request.POST['email'], first_name=request.POST['first_name'], last_name=request.POST['last_name'])
            auth.login(request,user)
            return redirect('index')
    return render(request, 'index')