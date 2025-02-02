from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from mailing.models import Message
from mailing.forms import MessageForm


class MessageList(LoginRequiredMixin, ListView):
    """Контроллер вывода списка сообщений"""

    model = Message
    template_name = "mailing/message/message_list.html"
    context_object_name = "messages"


class MessageDetail(LoginRequiredMixin, DetailView):
    """Контроллер детализации сообщения"""

    model = Message
    template_name = "mailing/message/message_detail.html"


class MessageCreate(LoginRequiredMixin, CreateView):
    """Контроллер создания нового сообщения"""

    model = Message
    form_class = MessageForm
    template_name = "mailing/message/message_form.html"
    success_url = reverse_lazy("mailing:message_list")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class MessageUpdate(LoginRequiredMixin, UpdateView):
    """Контроллер изменения сообщения"""

    model = Message
    form_class = MessageForm
    template_name = "mailing/message/message_form.html"
    success_url = reverse_lazy("mailing:message_list")


class MessageDelete(LoginRequiredMixin, DeleteView):
    """Контроллер удаления получателя рассылок"""

    model = Message
    template_name = "mailing/message/message_confirm_delete.html"
    success_url = reverse_lazy("mailing:message_list")
