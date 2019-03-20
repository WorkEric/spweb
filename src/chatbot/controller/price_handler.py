# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""handler file for the price module"""


from ..models import PricePlanFeature, PricePlan, PriceFeature


class PriceRow(object):
    """
    Representation of a row in price table
    """
    def __init__(self, row_header, fields):
        self.row_header = row_header
        self.fields = fields

    def __str__(self):
        return "row header: " + self.row_header + \
                " fields: " + self.fields


def get_plan_and_feature():
    """
    get a table of column header list , row header list and fields
    :return: a list of price rows
    """
    features = PriceFeature.objects.all()
    query_set = PricePlanFeature.objects.all()
    plans = PricePlan.objects.all()
    rows = []
    for feature in features:
        fields = []
        for plan in plans:
            value = __get_table_value(query_set, plan.name, feature.name)
            fields.append(value)
        row = PriceRow(feature.name, fields)
        rows.append(row)
    return plans, rows


def __get_table_value(query_set, plan_name, plan_feature_name):
    values = list(filter(lambda p:
                         p.price_plan.name == plan_name
                         and p.price_feature.name == plan_feature_name,
                         query_set))
    return "Unlimited" if not values else values[0].value
