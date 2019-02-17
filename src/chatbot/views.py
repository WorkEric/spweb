# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Chatbot app view"""

from django.shortcuts import render

HOME_PAGE = 'home.html'
TEMPLATE_PAGE = 'chatbot_template.html'


def index(request):
    """home page"""
    return render(request, HOME_PAGE)


def chatbot_template(request):
    """chatbot template page"""
    return render(request, TEMPLATE_PAGE)

