from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from mailing.models import MailingRecipient
from mailing.forms import MailingRecipientForm


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