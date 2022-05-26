from django.urls import path
from . import views

app_name = 'Login'
urlpatterns = [
    path('login_user/', views.login_user, name="login"),
    path('captcha/', views.captcha, name ='captcha')
    
]