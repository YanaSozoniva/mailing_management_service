from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from mailing.models import Newsletter, MailingRecipient, Message
from mailing.forms import MailingRecipientForm


class MailingRecipientList(ListView):
    model = MailingRecipient
    context_object_name = 'recipient'


class MailingRecipientDetail(DetailView):
    model = MailingRecipient


class MailingRecipientCreate(CreateView):
    model = MailingRecipient
    form_class = MailingRecipientForm
    success_url = reverse_lazy("mailing:recipient_list")


class MailingRecipientUpdate(UpdateView):
    model = MailingRecipient
    form_class = MailingRecipientForm
    success_url = reverse_lazy("mailing:recipient_list")


class MailingRecipientDelete(DeleteView):
    model = MailingRecipient
    success_url = reverse_lazy("mailing:recipient_list")