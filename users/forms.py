from users.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from mailing.forms import StyleFormMixin


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    username = None

    class Meta:
        model = User
        fields = ("email", "phone", "avatar", "country", "password1", "password2")


class UserUpdateForm(StyleFormMixin, UserChangeForm):
    username = None

    class Meta:
        model = User
        fields = ("email", "phone", "avatar", "country")
