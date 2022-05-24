from django.shortcuts import render, redirect
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
            login(request, user)
            return redirect('index')
            # redirect to a success page.
        else: 
            # return an 'invalid login' error
            messages.success(request, ("Unsuccessful login attempt, please try again..."))
            return redirect('login')
    
    else:
        return render(request, 'authentication/login.html', {})


def captcha(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            messages.success(request, "Success!")
        else:
            messages.error(request, "Wrong Captcha")
    form = MyForm()
    return render(request, 'authentication/login.html', {'form': form})

