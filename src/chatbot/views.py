# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Chatbot app view"""

from django.shortcuts import render

HOME_PAGE = 'home.html'
TEMPLATE_PAGE = 'chatbot_template.html'
TEMPLATE_DETAIL_PAGE = 'chatbot_template_detail.html'
PRICE_PAGE = 'price.html'
CAREER_PAGE = 'career.html'
LOGIN_PAGE = 'login.html'
SIGNUP_PAGE = 'signup.html'


def login(request):
    """Login page"""
    return render(request, LOGIN_PAGE)


def signup(request):
    """Sign up page"""
    return render(request, SIGNUP_PAGE)


def index(request):
    """home page"""
    return render(request, HOME_PAGE)


def chatbot_template(request):
    """chatbot template page"""
    return render(request, TEMPLATE_PAGE)


def chatbot_template_detail(request):
    """Chatbot template detail"""
    return render(request, TEMPLATE_DETAIL_PAGE)


def price(request):
    """Chatbot service price"""
    return render(request, PRICE_PAGE)


def career(request):
    """Career page"""
    return render(request, CAREER_PAGE)
