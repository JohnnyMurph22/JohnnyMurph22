from fileinput import filename
from django.shortcuts import render
from .models import Website
from .forms import *
from multiprocessing import context
# from django.contrib import messages

def index(request):
    return render(request, 'organizer_app/index.html')

def pokemon(request):
    return render(request, 'organizer_app\poke.html' )