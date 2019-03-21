# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""handler file for the price module"""


from ..models import PricePlanFeature, PricePlan, PriceFeature, PricePayment


class Plan(object):
    """
    Representation of a row in price table
    """
    def __init__(self, name, monthly_cost, yearly_cost):
        self.name = name
        self.monthly_cost = monthly_cost
        self.yearly_cost = yearly_cost

    def __str__(self):
        return "row header: " + self.name + \
                " monthly_cost: " + self.monthly_cost + \
                " yearly_cost: " + self.yearly_cost


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
    price_plans = PricePlan.objects.all()
    price_payments = PricePayment.objects.all()
    plans = __get_plan(price_payments, price_plans)
    rows = []
    for feature in features:
        fields = []
        for plan in plans:
            value = __get_table_value(query_set, plan.name, feature.name)
            fields.append(value)
        row = PriceRow(feature.name, fields)
        rows.append(row)
    return plans, rows


def __get_plan(price_payments, price_plans):
    plans = []
    for price_plan in price_plans:
        value1 = list(filter(lambda p: p.price_plan == price_plan and
                                       p.price_type == 'Monthly', price_payments))
        value2 = list(filter(lambda p: p.price_plan == price_plan and
                                       p.price_type == 'Yearly', price_payments))
        plan = Plan(price_plan.name, value1[0].value, value2[0].value)
        plans.append(plan)
    return plans


def __get_table_value(query_set, plan_name, plan_feature_name):
    values = list(filter(lambda p:
                         p.price_plan.name == plan_name
                         and p.price_feature.name == plan_feature_name,
                         query_set))
    return "Unlimited" if not values else values[0].value
