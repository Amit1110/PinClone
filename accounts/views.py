from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from . models import Image, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #log the user in
            login(request, user)
            return redirect('/accounts/pref')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/accounts/post')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/about')

def userPost(request):
    userprofile = UserProfile.objects.get(user=request.user)
    images = []
    for img in Image.objects.all():
        if img.tag in userprofile.choices.all():
            images.append(img)
    return render(request, 'accounts/wall.html', {'userprofile':userprofile, 'images':images})

@login_required(login_url = '/accounts/login/')
def selectPref(request):
    if request.method == 'POST':
        form = forms.SelectPreferences(request.POST, request.FILES)
        if form.is_valid():
            #save preferences
            instance = form.save()
            instance.save()
            return redirect('/accounts/post')
    else:
        form = forms.SelectPreferences()
    return render(request, 'accounts/select_preferences.html', {'form': form})
