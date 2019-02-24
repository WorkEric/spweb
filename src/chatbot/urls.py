# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Chatbot app urls"""

from django.urls import path
from . import views

app_name = 'chatbot'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('templates/', views.chatbot_template, name='chatbot_template'),
    path('template/detail', views.chatbot_template_detail, name='chatbot_template_detail'),
    path('price/', views.price, name='price'),
    path('career/', views.career, name='career'),
    path('profile/', views.profile, name='profile'),
]
