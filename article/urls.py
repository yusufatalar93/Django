from django.contrib import admin
from django.urls import path

from . import views

app_name = "article"
urlpatterns = [
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('addarticle/',views.addarticle,name = "addarticle"),
    path('detail/<int:id>',views.detail,name = "detail"),
    path('update/<int:id>',views.ArticleUpdate,name = "update"),
    path('delete/<int:id>',views.ArticleDelete,name = "delete"),
    path('',views.articless,name = "articless"),
    path('comment/<int:id>',views.AddComment,name = "comment"),
    

    
    
    
    
]
