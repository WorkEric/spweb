from ..models import SpUser, UserPricePayment, UserTemplateContent
from ..exceptions import UserNotFoundError
from datetime import datetime


class PaymentInfo(object):
    """
    Representation of a payment record with plan information
    """
    def __init__(self, price_name, short_des, long_des, price_type,
                 value, duration, start_at, end_at):
        self.price_name = price_name
        self.short_description = short_des
        self.long_description = long_des
        self.price_type = price_type
        self.value = value
        self.duration = duration
        self.start_at = start_at
        self.end_at = end_at

    def __str__(self):
        return "product: " + self.price_name + \
                " price type: " + self.price_type + \
                " start date: " + str(self.start_at) + \
                " end date" + str(self.end_at)


class TemplateInfo(object):
    """
    Representation of a template record
    """
    def __init__(self, title, image, description):
        self.title = title
        self.image = image
        self.description = description

    def __str__(self):
        return "title: " + self.title + \
                " image: " + self.image.url + \
                " description: " + self.description


def update_user_basic_info(user_dict, email):
    """update user basic info function"""
    sp_user = SpUser.objects.get(email=email)
    sp_user.username = user_dict['username']
    sp_user.first_name = user_dict['firstName']
    sp_user.last_name = user_dict['lastName']
    sp_user.phone = user_dict['phoneNumber']
    sp_user.company_url = user_dict['url']
    sp_user.save()
    return sp_user


def get_user_full_info(email):
    """get user full info function"""
    if not SpUser.objects.filter(email=email).exists():
        raise UserNotFoundError("user {} not found!".format(email))
    sp_user = __get_user_basic_info(email)
    payments = __get_user_payments(email)
    templates = __get_user_templates(email)
    payments = sorted(payments, key=lambda x: x.end_at, reverse=True)
    current_plan = None
    if payments and payments[0].price_name.lower() != "free" and payments[0].end_at >= datetime.now():
        current_plan = payments[0]
    if not payments:
        payments = None
    elif len(payments) >1 and payments[0].end_at >= datetime.now():
        payments = payments[1:]
    return sp_user, current_plan, payments, templates


def __get_user_basic_info(email):
    """inner function to get user basic info"""
    return SpUser.objects.get(email=email)


def __get_user_payments(email):
    """inner function to get user payment"""
    query_set = UserPricePayment.objects.filter(sp_user__email=email)
    return list(map(lambda price:
                    PaymentInfo(price.price_payment.price_plan.name,
                                price.price_payment.price_plan.short_description,
                                price.price_payment.price_plan.long_description,
                                price.price_payment.price_type,
                                price.price_payment.value,
                                price.price_payment.duration,
                                price.start_at,
                                price.end_at), query_set))


def __get_user_templates(email):
    """inner function to get user templates"""
    query_set = UserTemplateContent.objects.filter(sp_user__email=email)
    return map(lambda ut: TemplateInfo(ut.template_content.title,
                                       ut.template_content.image,
                                       ut.template_content.description
                                       ), query_set)
