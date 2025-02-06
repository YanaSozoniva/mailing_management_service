import secrets

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import cache_page
from django.views.generic import CreateView, ListView, DetailView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import User
from django.contrib import messages


class UserCreateViews(CreateView):
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}/"
        send_mail(
            subject="Подтверждение почты",
            message=f"Здравствуйте, для регистрации почты {url} перейдите по ссылке",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )

        messages.success(self.request, "Письмо с подтверждением отправлено на ваш email.")
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.token = None
    user.is_active = True
    user.save()
    messages.success(request, "Ваш email успешно подтверждён!")
    return redirect(reverse("users:login"))


class UserList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Контроллер вывода списка сообщений"""

    model = User
    template_name = "users/users_list.html"
    context_object_name = "users"
    permission_required = "users.view_user"


class BlockUsersView(LoginRequiredMixin, View):

    def post(self, request, pk):
        user = get_object_or_404(User, id=pk)

        if not request.user.has_perm("users.can_block_users"):
            raise PermissionDenied("У вас нет права на блокировку/разблокировку пользователя")

        if user.is_active:
            user.is_active = False
        else:
            user.is_active = True

        user.save()

        return redirect("users:user_detail", pk=pk)


@method_decorator(cache_page(60 * 5), name="dispatch")
class UserDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Контроллер вывода списка сообщений"""

    model = User
    template_name = "users/user_detail.html"
    context_object_name = "user"
    permission_required = "users.can_block_users"
