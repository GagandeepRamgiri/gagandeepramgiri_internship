from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.main, name="main"),
    path('index',views.index, name="index"),
    path('create',views.create, name="create"),
    path('addusers',views.addusers, name="addusers"),
    path('view/<int:id>', views.view, name="view"),
    path('edit/<int:id>',views.edit, name="edit"),
    path('updateuser/<int:id>',views.updateuser, name="updateuser"),
    path('delete/<int:id>',views.deleteuser, name="deleteuser"),
    path('generate',views.generate,name="generate")
]