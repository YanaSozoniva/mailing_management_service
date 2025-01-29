from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from mailing.models import Newsletter, MailingRecipient, Message
from mailing.forms import MailingRecipientForm, MessageForm, NewsletterForm


class MailingRecipientList(ListView):
    """Контроллер вывода списка получателей рассылок"""

    model = MailingRecipient
    template_name = "mailing/recipient_list.html"
    context_object_name = "recipients"


class MailingRecipientDetail(DetailView):
    """Контроллер детализации получателя рассылок"""

    model = MailingRecipient
    template_name = "mailing/recipient_detail.html"
    context_object_name = "recipient"


class MailingRecipientCreate(CreateView):
    """Контроллер создания получателя рассылок"""

    model = MailingRecipient
    form_class = MailingRecipientForm
    template_name = "mailing/recipient_form.html"
    success_url = reverse_lazy("mailing:recipient_list")


class MailingRecipientUpdate(UpdateView):
    """Контроллер изменения получателя рассылок"""

    model = MailingRecipient
    form_class = MailingRecipientForm
    template_name = "mailing/recipient_form.html"
    success_url = reverse_lazy("mailing:recipient_list")


class MailingRecipientDelete(DeleteView):
    """Контроллер удаления получателя рассылок"""

    model = MailingRecipient
    success_url = reverse_lazy("mailing:recipient_list")


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


class NewsletterList(ListView):
    """Контроллер вывода списка рассылок"""

    model = Newsletter
    context_object_name = "newsletters"


class NewsletterDetail(DetailView):
    """Контроллер детализации рассылки"""

    model = Newsletter


class NewsletterCreate(CreateView):
    """Контроллер создания новой рассылки"""

    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy("mailing:newsletter_list")


class NewsletterUpdate(UpdateView):
    """Контроллер изменения рассылки"""

    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy("mailing:newsletter_list")


class NewsletterDelete(DeleteView):
    """Контроллер удаления получателя рассылок"""

    model = Newsletter
    success_url = reverse_lazy("mailing:newsletter_list")
