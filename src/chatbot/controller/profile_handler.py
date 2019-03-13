from ..models import SpUser


def get_user_basic_info(email):
    return SpUser.objects.get(email=email)


def update_user_basic_info(user_dict, email):
    sp_user = SpUser.objects.get(email=email)
    sp_user.username = user_dict['username']
    sp_user.first_name = user_dict['firstName']
    sp_user.last_name = user_dict['lastName']
    sp_user.phone = user_dict['phoneNumber']
    sp_user.company_url = user_dict['url']
    sp_user.save()
    return sp_user



