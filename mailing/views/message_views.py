from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from mailing.models import Message
from mailing.forms import MessageForm
from mailing.services import get_list_by_owner


class MessageList(LoginRequiredMixin, ListView):
    """Контроллер вывода списка сообщений"""

    model = Message
    template_name = "mailing/message/message_list.html"
    context_object_name = "messages"

    def get_queryset(self):
        if not self.request.user.has_perm("mailing.view_message"):
            return get_list_by_owner(self.request.user.id, Message)
        return Message.objects.all()


class MessageDetail(LoginRequiredMixin, DetailView):
    """Контроллер детализации сообщения"""

    model = Message
    template_name = "mailing/message/message_detail.html"


class MessageCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Контроллер создания нового сообщения"""

    model = Message
    form_class = MessageForm
    template_name = "mailing/message/message_form.html"
    success_url = reverse_lazy("mailing:message_list")
    permission_required = 'mailing.add_message'

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class MessageUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Контроллер изменения сообщения"""

    model = Message
    form_class = MessageForm
    template_name = "mailing/message/message_form.html"
    success_url = reverse_lazy("mailing:message_list")
    permission_required = 'mailing.change_message'

    def get_success_url(self):
        return reverse('mailing:message_detail', args=[self.kwargs.get('pk')])


class MessageDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Контроллер удаления получателя рассылок"""

    model = Message
    template_name = "mailing/message/message_confirm_delete.html"
    success_url = reverse_lazy("mailing:message_list")
    permission_required = 'mailing.delete_message'
