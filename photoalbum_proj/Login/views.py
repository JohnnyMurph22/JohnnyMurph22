from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from .forms import MyForm
# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('goes to captcha')
            login(request, user)
            return render(request,'authentication/captcha.html')
            # redirect to a success page.
        else: 
            print('returns to login')
            # return an 'invalid login' error
            messages.success(request, ("Unsuccessful login attempt, please try again..."))
            return render(request,'authentication/login.html')
    
    else:
        print('go to authentication html')
        return render(request, 'authentication/login.html', {})


def captcha(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            messages.success(request, "Success!")
            return render(request, 'organizer_app\poke.html',{})
        else:
            messages.error(request, "Wrong Captcha")
    form = MyForm()
    return render(request, 'authentication/captcha.html', {'form': form})

