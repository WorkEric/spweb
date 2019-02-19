# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Chatbot admin"""

from django.contrib import admin
from .models import TemplateCategory, TemplateContent, TemplateCategoryContent, PricePlan, \
    PricePayment, PriceFeature, PricePlanFeature, SpUser, UserPricePayment


class TemplateCategoryAdmin(admin.ModelAdmin):
    """Template category admin module"""
    list_display = ('name', 'order_number')


class TemplateContentAdmin(admin.ModelAdmin):
    """Template content admin"""
    list_display = ('title', 'image', 'description')


class TemplateCategoryContentAdmin(admin.ModelAdmin):
    """Template category content admin"""
    list_display = ('template_category', 'template_content')


class PricePlanAdmin(admin.ModelAdmin):
    """Price plan admin"""
    list_display = ('name', 'short_description', 'long_description')


class PricePaymentAdmin(admin.ModelAdmin):
    """Price payment admin"""
    list_display = ('price_plan', 'price_type', 'value', 'start_at', 'end_at')


class PriceFeatureAdmin(admin.ModelAdmin):
    """Price feature admin"""
    list_display = ('name', 'description')


class PricePlanFeatureAdmin(admin.ModelAdmin):
    """Price plan feature admin"""
    list_display = ('price_plan', 'price_feature')


class SpUserAdmin(admin.ModelAdmin):
    """Price plan feature admin"""
    list_display = (
        'username', 'first_name', 'last_name', 'email', 'phone', 'company', 'company_url', 'avatar',
        'activated', 'whitelisting')


class UserPricePaymentAdmin(admin.ModelAdmin):
    """User price payment admin"""
    list_display = ('sp_user', 'price_payment', 'start_at', 'end_at')


admin.site.register(TemplateCategory, TemplateCategoryAdmin)
admin.site.register(TemplateContent, TemplateContentAdmin)
admin.site.register(TemplateCategoryContent, TemplateCategoryContentAdmin)
admin.site.register(PricePlan, PricePlanAdmin)
admin.site.register(PricePayment, PricePaymentAdmin)
admin.site.register(PriceFeature, PriceFeatureAdmin)
admin.site.register(PricePlanFeature, PricePlanFeatureAdmin)
admin.site.register(SpUser, SpUserAdmin)
admin.site.register(UserPricePayment, UserPricePaymentAdmin)
