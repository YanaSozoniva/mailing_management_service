from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from mailing.models import MailingRecipient
from mailing.forms import MailingRecipientForm
from django.contrib.auth.mixins import LoginRequiredMixin


class MailingRecipientList(LoginRequiredMixin, ListView):
    """Контроллер вывода списка получателей рассылок"""

    model = MailingRecipient
    template_name = "mailing/recipient/recipient_list.html"
    context_object_name = "recipients"


class MailingRecipientDetail(LoginRequiredMixin, DetailView):
    """Контроллер детализации получателя рассылок"""

    model = MailingRecipient
    template_name = "mailing/recipient/recipient_detail.html"
    context_object_name = "recipient"


class MailingRecipientCreate(LoginRequiredMixin, CreateView):
    """Контроллер создания получателя рассылок"""

    model = MailingRecipient
    form_class = MailingRecipientForm
    template_name = "mailing/recipient/recipient_form.html"
    success_url = reverse_lazy("mailing:recipient_list")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class MailingRecipientUpdate(LoginRequiredMixin, UpdateView):
    """Контроллер изменения получателя рассылок"""

    model = MailingRecipient
    form_class = MailingRecipientForm
    template_name = "mailing/recipient/recipient_form.html"
    success_url = reverse_lazy("mailing:recipient_list")


class MailingRecipientDelete(LoginRequiredMixin, DeleteView):
    """Контроллер удаления получателя рассылок"""

    model = MailingRecipient
    template_name = "mailing/recipient/recipient_confirm_delete.html"
    success_url = reverse_lazy("mailing:recipient_list")
