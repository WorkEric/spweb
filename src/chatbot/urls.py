# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Chatbot app urls"""

from django.urls import path
from . import views

app_name = 'chatbot'

urlpatterns = [
    path('', views.index, name='index'),

]
