from users.models import User
from django.contrib.auth.forms import UserCreationForm
from mailing.forms import StyleFormMixin
from django import forms


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    username = forms.CharField(max_length=50, required=True)
    usable_password = None

    class Meta:
        model = User
        fields = ("email", 'username', 'first_name', 'last_name', "password1", "password2")
