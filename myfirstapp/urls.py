from django.urls import path 
from . import views 

# routes URLs to views function index()
urlpatterns = [ 
    path('myfirst/', views.index, name='index'), 
] 