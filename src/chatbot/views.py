# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Chatbot app view"""

from django.shortcuts import render

HOME_PAGE = 'home.html'


def index(request):
    """home page"""
    return render(request, HOME_PAGE)


