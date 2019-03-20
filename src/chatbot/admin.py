# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Chatbot admin"""

from django.contrib import admin
from .models import TemplateCategory, TemplateContent, TemplateCategoryContent, PricePlan, \
    PricePayment, PriceFeature, PricePlanFeature, SpUser, UserPricePayment, UserTemplateContent


class TemplateCategoryAdmin(admin.ModelAdmin):
    """Template category admin module"""
    list_display = ('id', 'name', 'order_number')


class TemplateContentAdmin(admin.ModelAdmin):
    """Template content admin"""
    list_display = ('id', 'title', 'image', 'description')


class TemplateCategoryContentAdmin(admin.ModelAdmin):
    """Template category content admin"""
    list_display = ('id', 'template_category', 'template_content')


class PricePlanAdmin(admin.ModelAdmin):
    """Price plan admin"""
    list_display = ('id', 'name', 'short_description', 'long_description')


class PricePaymentAdmin(admin.ModelAdmin):
    """Price payment admin"""
    list_display = ('id', 'price_plan', 'price_type', 'value', 'duration')


class PriceFeatureAdmin(admin.ModelAdmin):
    """Price feature admin"""
    list_display = ('id', 'name', 'description')


class PricePlanFeatureAdmin(admin.ModelAdmin):
    """Price plan feature admin"""
    list_display = ('id', 'price_plan', 'price_feature')


class SpUserAdmin(admin.ModelAdmin):
    """Price plan feature admin"""
    list_display = (
        'id', 'username', 'first_name', 'last_name', 'email', 'phone', 'company', 'company_url',
        'avatar', 'activated', 'whitelisting')


class UserPricePaymentAdmin(admin.ModelAdmin):
    """User price payment admin"""
    list_display = ('id', 'sp_user', 'price_payment', 'start_at', 'end_at')


class UserTemplateContentAdmin(admin.ModelAdmin):
    """User price payment admin"""
    list_display = ('id', 'sp_user', 'template_content')


admin.site.register(TemplateCategory, TemplateCategoryAdmin)
admin.site.register(TemplateContent, TemplateContentAdmin)
admin.site.register(TemplateCategoryContent, TemplateCategoryContentAdmin)
admin.site.register(PricePlan, PricePlanAdmin)
admin.site.register(PricePayment, PricePaymentAdmin)
admin.site.register(PriceFeature, PriceFeatureAdmin)
admin.site.register(PricePlanFeature, PricePlanFeatureAdmin)
admin.site.register(SpUser, SpUserAdmin)
admin.site.register(UserPricePayment, UserPricePaymentAdmin)
admin.site.register(UserTemplateContent, UserTemplateContentAdmin)
