from django.contrib import admin
from django.urls import path

from . import views

app_name = "user"
urlpatterns = [
    path('register/',views.register,name = "register"),
    path('loginuser/',views.loginuser,name = "loginuser"),
    path('logoutuser/',views.logoutuser,name = "logoutuser"),
    
    
]
