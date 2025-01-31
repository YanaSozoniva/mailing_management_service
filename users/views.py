from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserRegisterForm


class UserCreateViews(CreateView):
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")
