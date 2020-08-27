from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from .models import Profile
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate as django_authenticate
from django.http import JsonResponse

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user=User.objects.create_user(username=request.POST['username'], password=request.POST['password1'], email=request.POST['email'], first_name=request.POST['first_name'], last_name=request.POST['last_name'])
            auth.login(request,user)
            return render(request, 'pages/index.html')
    return render(request, 'pages/index.html')

def change_profile(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        User.objects.filter(id=id).update(username=request.POST['username'], first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
        Profile.objects.filter(user=user).update(college=request.POST['college'], major=request.POST['major'])
        user.refresh_from_db()
        return render(request, 'accounts/profile.html')
    else:
        return render(request, 'accounts/change_profile.html')

def profile(request, id):
    user = User.objects.get(id=id)
    return render(request, 'accounts/profile.html')

def charge(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
       point = user.profile.point
       chargedpoint = user.profile.chargedpoint
       Profile.objects.filter(user=user).update(point=point+int(request.POST['chargepoint']), chargedpoint=chargedpoint+int(request.POST['chargepoint']))
       return render(request, 'accounts/charge.html')
    else:
        return render(request, 'accounts/charge.html')

def change(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
       point = user.profile.point
       changedpoint = user.profile.changedpoint
       Profile.objects.filter(user=user).update(point=point-int(request.POST['changepoint']),changedpoint=changedpoint+int(request.POST['changepoint']))
       return render(request, 'accounts/charge.html')
    else:
        return render(request, 'accounts/charge.html')

def firstsetting1(request):
    user = request.user
    if request.method == 'POST':
        Profile.objects.filter(user=user).update(college=request.POST['college'])
        return redirect('/')


def firstsetting2(request):
    user = request.user
    if request.method == 'POST':
        Profile.objects.filter(user=user).update(major=request.POST['major'])
        return redirect('/')

def firstsetting3(request):
    user = request.user
    if request.method == 'POST':
        Profile.objects.filter(user=user).update(grade=request.POST['grade'])
        return redirect('/')

def firstsetting4(request):
    user = request.user
    if request.method == 'POST':
        Profile.objects.filter(user=user).update(gender=request.POST['gender'])
        return redirect('/')