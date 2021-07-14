from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('mask_feed', views.mask_feed, name='mask_feed'),


    path('resources/', views.resources, name='resources'),
    path('vaccine/', views.vaccine, name='vaccine'),

]
