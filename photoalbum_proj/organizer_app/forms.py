from django import forms 
from captcha.fields import CaptchaField 

class MyForm(forms.Form):
    captcha = CaptchaField()

class Directory(forms.Form):
    path = forms.CharField(label="Enter directory path")