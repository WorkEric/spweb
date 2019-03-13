# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Model file

Tasks:
1. Build the models foundation
2. write the CRUD function for each model by getting and setting
3. add the validation in the class

Validation note:
Note that validators will not be run automatically when you save a model, but if you are using
a ModelForm, it will run your validators on any fields that are included in your form.
"""

from django.db import models
from django.core.validators import validate_email, validate_integer, MaxLengthValidator


PRICE_TYPE = (
    ('Monthly', 'Monthly'),
    ('Yearly', 'Yearly'),
)


class TimeStampedModel(models.Model):
    """
    This is abstract base class model that provides self updating created and modified fields.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta class for timestamp model"""
        abstract = True


class TemplateCategory(TimeStampedModel):
    """Template category class"""
    name = models.CharField(max_length=255, unique=True, null=True,
                            validators=[MaxLengthValidator(255)])
    data_type = models.CharField(max_length=255, null=True, default='',
                                 validators=[MaxLengthValidator(255)])
    order_number = models.IntegerField(default=0, validators=[validate_integer])

    class Meta:
        """Meta class for template category"""
        db_table = 'template_category'


class TemplateContent(TimeStampedModel):
    """Template content class"""
    title = models.CharField(max_length=255, blank=True, null=True,
                             validators=[MaxLengthValidator(255)])
    image = models.ImageField(default='static/img/minibot-logo.png',
                              upload_to='static/img/templatecontent/')
    description = models.TextField(null=True)

    template_categories = models.ManyToManyField(TemplateCategory,
                                                 through='TemplateCategoryContent')

    class Meta:
        """Meta class for template content"""
        db_table = 'template_content'


class TemplateCategoryContent(TimeStampedModel):
    """Template category content"""
    template_category = models.ForeignKey(TemplateCategory, on_delete=models.CASCADE)
    template_content = models.ForeignKey(TemplateContent, on_delete=models.CASCADE)

    class Meta:
        """Meta class for template category content"""
        db_table = 'template_category_content'
        unique_together = (('template_category', 'template_content'),)


class PricePlan(TimeStampedModel):
    """Price plan"""
    name = models.CharField(max_length=255, unique=True, null=True,
                            validators=[MaxLengthValidator(255)])  # Free, Lite, Standard, Plus
    short_description = models.TextField(null=True)
    long_description = models.TextField(null=True)

    class Meta:
        """Meta class for price plan"""
        db_table = 'price_plan'


class PricePayment(TimeStampedModel):
    """Price payment class"""
    price_plan = models.ForeignKey(PricePlan, on_delete=models.CASCADE)
    price_type = models.CharField(max_length=40, choices=PRICE_TYPE, default='Monthly')
    value = models.IntegerField(default=0, validators=[validate_integer])
    duration = models.IntegerField(default=0, validators=[validate_integer])

    class Meta:
        """Meta class for price payment"""
        db_table = 'price_payment'


class PriceFeature(TimeStampedModel):
    """Price feature class"""
    name = models.CharField(max_length=255, blank=True, validators=[MaxLengthValidator(255)])
    description = models.TextField(null=True)
    price_plans = models.ManyToManyField(PricePlan, through='PricePlanFeature')

    class Meta:
        """Meta class for price feature"""
        db_table = 'price_feature'


class PricePlanFeature(TimeStampedModel):
    """Price plan feature class"""
    price_plan = models.ForeignKey(PricePlan, on_delete=models.CASCADE)
    price_feature = models.ForeignKey(PriceFeature, on_delete=models.CASCADE)
    value = models.CharField(max_length=255, blank=True, validators=[MaxLengthValidator(255)])

    class Meta:
        """Meta class for price plan feature"""
        db_table = 'price_plan_feature'


class SpUser(TimeStampedModel):
    """Spweb user class"""
    username = models.CharField(max_length=255, unique=True, null=True,
                                validators=[MaxLengthValidator(255)])
    first_name = models.CharField(max_length=255, blank=True, null=True,
                                  validators=[MaxLengthValidator(255)])
    last_name = models.CharField(max_length=255, blank=True, null=True,
                                 validators=[MaxLengthValidator(255)])
    email = models.CharField(max_length=255, unique=True, validators=[validate_email])
    phone = models.CharField(max_length=255, unique=True, null=True,
                             validators=[MaxLengthValidator(255)])
    company = models.CharField(max_length=255, blank=True, null=True,
                               validators=[MaxLengthValidator(255)])
    company_url = models.CharField(max_length=1024, blank=True, null=True,
                                   validators=[MaxLengthValidator(1024)])
    avatar = models.ImageField(default='', upload_to='static/img/spuser', blank=True, null=True)
    activated = models.BooleanField(default=False)  # user status
    whitelisting = models.BooleanField(default=False)  # user is admin or not

    class Meta:
        """Meta class for spweb user"""
        db_table = 'sp_user'


class UserPricePayment(TimeStampedModel):
    """User price payment class"""
    sp_user = models.ForeignKey(SpUser, on_delete=models.DO_NOTHING)
    price_payment = models.ForeignKey(PricePayment, on_delete=models.DO_NOTHING)
    start_at = models.DateTimeField(null=True)  # each time user make payment, record it
    end_at = models.DateTimeField(null=True)  # user can cancel on the next time, then not available

    class Meta:
        """Meta class for user price payment"""
        db_table = 'user_price_payment'


class UserTemplateContent(TimeStampedModel):
    """user and template content table """
    sp_user = models.ForeignKey(SpUser, on_delete=models.DO_NOTHING)
    template_content = models.ForeignKey(TemplateContent, on_delete=models.DO_NOTHING)

    class Meta:
        """Meta class for user template content"""
        db_table = 'user_template_content'
