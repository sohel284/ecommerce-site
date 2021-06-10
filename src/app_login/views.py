from django import forms
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse

# authentication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

#models and forms
from app_login.models import CustomUser, Profile
from app_login.forms import ProfileForm, SignupForm



def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Create Successfully', )
            return redirect('login')
    return render(request, 'login_app/signup.html', {'form': form})

def login_user(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            return HttpResponse('username is not found ')    
    return render(request, 'login_app/login.html', {'form': form})

@login_required

def logout_user(request):
    logout(request)
    messages.warning(request, 'You are logged out')
    return redirect('home')

def user_profile_change(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST,instance=profile, )
        if form.is_valid():
            form.save()
            messages.success(request, "Profile changed saved ")
            form = ProfileForm(instance=profile)
    return render(request, 'login_app/profile_change.html', {'form': form, })
