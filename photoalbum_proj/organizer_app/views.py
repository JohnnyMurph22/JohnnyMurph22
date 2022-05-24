from fileinput import filename
from django.shortcuts import render
from .models import Website
from .forms import *
from multiprocessing import context
# from django.contrib import messages

def index(request):
    return render(request, 'organizer_app/index.html')


def home_view(request):
    name = ""

    obj = Website.objects.get(id=1)
    context = {
        'name': name,
        'obj': obj,
    }

    return render(request, 'home.html', context)

# def home(request):
#     if request.method == "POST":
#         form = MyForm(request.POST)
#         if form.is_valid():
#             messages.success(request, "Success!")
#         else:
#             messages.error(request, "Wrong Captcha")
#     form = MyForm()
#     return render(request, 'organizer_app\home.html', {'form': form})

def fileorg(request):
    import os
    import shutil

    # from pathlib import Path

    # create a varible called path that takes the input of the directory to organize
    path = Directory()
    # create a variable called files consisting of a list of files 
    files = os.listdir(path)
    #  using for loop, we travel through every file, split the file name and extension of the files 
    for file in files: 
        filename,extension = os.path.splitext(file)
        extension = extension[1:]
    # if the extension directory already exists move the file to that directory 
        if os.path.exists(path+'/'+extension):
            shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
            message = 'files moved to appropriate directory'
    # if not make new directory and move the file into it 
        else:
            os.makedirs(path+'/'+extension)
            shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
            message = 'new directories created as required'
    return render(request, {'path': path}, message)