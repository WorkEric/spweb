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
            form.save()
            user_obj = form.cleaned_data
            url = user_obj['url']
            email = user_obj['username']
            password = user_obj['password1']
            sp_user = SpUser(email=email, company_url=url, activated=True)
            user = authenticate(username=email, password=password)
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
        username = user_obj['username']
        password = user_obj['password']
        if '@' not in username:
            sp_user = SpUser.objects.get(username=username)
            if not sp_user:
                raise UserNotFoundError("user {} not exist or password is not "
                                        "correct!".format(username))
            username = sp_user.email
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(return_page)
        else:
            raise UserNotFoundError("user {} not exist or password is not "
                                    "correct!".format(username))


def user_logout(request):
    logout(request)





