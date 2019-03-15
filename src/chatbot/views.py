# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Chatbot app view"""

from django.shortcuts import render, redirect

from .controller.authentication_handler import add_new_user, user_login, user_logout
from .controller.profile_handler import get_user_full_info, update_user_basic_info
from .controller.template_handler import get_template_info
from .exceptions import UserNotFoundError


HOME_PAGE = 'home.html'
TEMPLATE_PAGE = 'chatbot_template.html'
TEMPLATE_DETAIL_PAGE = 'chatbot_template_detail.html'
PRICE_PAGE = 'price.html'
CAREER_PAGE = 'career.html'
LOGIN_PAGE = 'login.html'
SIGNUP_PAGE = 'signup.html'
PROFILE_PAGE = 'profile.html'


def login(request):
    """Login page"""
    return_page = request.GET.get('next', '/')
    try:
        response = user_login(request, return_page)
    except UserNotFoundError as unf:
        return render(request, LOGIN_PAGE,  {'errors': unf.message})
    else:
        if response:
            return response
        else:
            return render(request, LOGIN_PAGE)


def logout(request):
    user_logout(request)
    return redirect('/')


def signup(request):
    """Sign up page"""
    return_page = request.GET.get('next', '/')
    form = add_new_user(request)
    if form is not None:
        context = {'form': form}
        return render(request, SIGNUP_PAGE, context)
    else:
        return redirect(return_page)


def index(request):
    """home page"""
    return render(request, HOME_PAGE)


def chatbot_template(request):
    """chatbot template page"""
    categories, contents = get_template_info()
    context = {
        'categories': categories,
        'contents': contents
    }
    return render(request, TEMPLATE_PAGE, context)


def chatbot_template_detail(request):
    """Chatbot template detail"""
    return render(request, TEMPLATE_DETAIL_PAGE)


def price(request):
    """Chatbot service price"""
    return render(request, PRICE_PAGE)


def career(request):
    """Career page"""
    return render(request, CAREER_PAGE)


def profile(request):
    """Profile page"""
    if request.user.is_anonymous:
        return redirect("/")
    email = request.user.username
    sp_user, current_plan, payments, templates = get_user_full_info(email)
    if request.method == 'POST':
        sp_user = update_user_basic_info(request.POST, email)
    context = {
        'username': sp_user.username,
        'first_name': sp_user.first_name,
        'last_name': sp_user.last_name,
        'phone_number': sp_user.phone,
        'email': sp_user.email,
        'url': sp_user.company_url,
        'payments': payments,
        'current_plan': current_plan,
        'templates': templates
    }
    return render(request, PROFILE_PAGE, context)

