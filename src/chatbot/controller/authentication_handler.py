from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django import forms
from ..models import SpUser
from ..exceptions import UserNotFoundError


class SignUpForm(UserCreationForm):
    url = forms.CharField(max_length=254, label='url', required=False)

    class Meta:
        model = User
        fields = ('username', 'url', 'password1', 'password2', )


def add_new_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user_obj = form.cleaned_data
            url = user_obj['url']
            email = user_obj['username']
            password = user_obj['password1']
            if not __validate_email(email):
                form.add_error('username', "email format is not valid")
                return form
            form.save()
            user = authenticate(username=email, password=password)
            username = email.rsplit('@', 1)[0]
            sp_user = SpUser(email=email, company_url=url,
                             activated=True, username=username)
            if SpUser.objects.filter(email=email):
                SpUser.objects.filter(email=email).delete()
            sp_user.save()
            login(request, user)
            return None
    else:
        form = UserCreationForm()
    return form


def user_login(request, return_page):
    if request.method == 'POST':
        user_obj = request.POST
        input_username = user_obj['username']
        password = user_obj['password']
        username = input_username
        if '@' not in input_username:
            if SpUser.objects.filter(username=input_username).exists():
                sp_user = SpUser.objects.get(username=input_username)
            else:
                raise UserNotFoundError("user {} not exist or password is not "
                                        "correct!".format(input_username))
            username = sp_user.email
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(return_page)
        else:
            raise UserNotFoundError("user {} not exist or password is not "
                                    "correct!".format(input_username))


def user_logout(request):
    logout(request)


def __validate_email(email):
    return ('@' in email) and len(email) >= 3
