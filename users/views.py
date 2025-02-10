import secrets

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import cache_page
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserUpdateForm
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


class UserUpdateViews(LoginRequiredMixin, UpdateView):
    template_name = "users/register.html"
    form_class = UserUpdateForm
    success_url = reverse_lazy("users:login")

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def get_success_url(self):
        return reverse("users:user_detail", args=[self.kwargs.get("pk")])


class UserList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Контроллер вывода списка сообщений"""

    model = User
    template_name = "users/users_list.html"
    context_object_name = "users"
    permission_required = "users.view_user"

    def get_queryset(self):
        """Исключение из списка суперпользователя и всех менеджеров"""
        queryset = super().get_queryset()
        queryset = queryset.filter(is_superuser=False)
        # Исключаем пользователей с правами can_block_users
        queryset = queryset.exclude(groups__permissions__codename='can_block_users')
        return queryset


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

        return redirect("users:users_list")


@method_decorator(cache_page(60 * 5), name="dispatch")
class UserDetail(LoginRequiredMixin, DetailView):
    """Контроллер вывода списка сообщений"""

    model = User
    template_name = "users/user_detail.html"
    context_object_name = "user"
