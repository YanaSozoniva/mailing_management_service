from users.models import User
from django.contrib.auth.forms import UserCreationForm
from mailing.forms import StyleFormMixin
from django import forms


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    username = None
    usable_password = None

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "password1", "password2")
