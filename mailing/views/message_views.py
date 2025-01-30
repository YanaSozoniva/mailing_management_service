from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from mailing.models import Message
from mailing.forms import MessageForm


class MessageList(ListView):
    """Контроллер вывода списка сообщений"""

    model = Message
    template_name = "mailing/message/message_list.html"
    context_object_name = "messages"


class MessageDetail(DetailView):
    """Контроллер детализации сообщения"""

    model = Message
    template_name = "mailing/message/message_detail.html"


class MessageCreate(CreateView):
    """Контроллер создания нового сообщения"""

    model = Message
    form_class = MessageForm
    template_name = "mailing/message/message_form.html"
    success_url = reverse_lazy("mailing:message_list")


class MessageUpdate(UpdateView):
    """Контроллер изменения сообщения"""

    model = Message
    form_class = MessageForm
    template_name = "mailing/message/message_form.html"
    success_url = reverse_lazy("mailing:message_list")


class MessageDelete(DeleteView):
    """Контроллер удаления получателя рассылок"""

    model = Message
    template_name = "mailing/message/message_confirm_delete.html"
    success_url = reverse_lazy("mailing:message_list")
