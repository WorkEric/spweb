# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""handler file for the price module"""


from ..models import PriceFeature, PriceFeature_PricePlan, PricePlanFeature 


def get_feature_info():
    """
    get feature info
    """
    features = PriceFeature.objects.all()
    # test = TemplateCategory(name='test')
    # test.full_clean()
    # test.save()
    return features 

def get_plan_feature_info():
    plan_features = PricePlanFeature.objects.all()
    return plan_features

def get_plan_info():
    plan_infos = PriceFeature_PricePlan.objects.all()
    return plan_infos