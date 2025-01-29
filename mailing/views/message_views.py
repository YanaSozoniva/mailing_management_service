from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from mailing.models import Message
from mailing.forms import MessageForm


class MessageList(ListView):
    """Контроллер вывода списка сообщений"""

    model = Message
    context_object_name = "messages"


class MessageDetail(DetailView):
    """Контроллер детализации сообщения"""

    model = Message


class MessageCreate(CreateView):
    """Контроллер создания нового сообщения"""

    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailing:message_list")


class MessageUpdate(UpdateView):
    """Контроллер изменения сообщения"""

    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailing:message_list")


class MessageDelete(DeleteView):
    """Контроллер удаления получателя рассылок"""

    model = Message
    success_url = reverse_lazy("mailing:message_list")
