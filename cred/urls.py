from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse
from .views import *
urlpatterns = [
    path('', home, name="home"),
    path('add_details/', add_details, name="add_details"),
    path('form/', form, name="form"),
    path('remove_cart_items/<str:stu_uid>/', remove_cart_items, name="remove_cart_items"),
    path('update/<str:stu_uid>/', update, name="update"),
    path('update_form/<str:stu_uid>/', update_form, name="update_form"),  # Corrected
]