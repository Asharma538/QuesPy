from xml.etree.ElementInclude import include
from django import views
from django.contrib import admin
from django.urls import path,include
from QuesPy import views
urlpatterns = [
    path('',views.index,name="Home"),
    path('signup',views.signup,name="Sign Up"),
    path('uploadq',views.uploadq,name="Upload Question")
]
