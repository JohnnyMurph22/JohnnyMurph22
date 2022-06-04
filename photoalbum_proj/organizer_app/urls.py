from django.urls import path
from .import views 

app_name = 'organizer_app'
urlpatterns = [
    path('', views.index, name="home"),
    path('pokemon/', views.pokemon, name="pokemon"),
]