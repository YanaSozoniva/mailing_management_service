from users.models import User
from django.contrib.auth.forms import UserCreationForm
from mailing.forms import StyleFormMixin
from django import forms


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    username = None

    class Meta:
        model = User
        fields = ("email", "phone", "avatar", "country", "password1", "password2")
