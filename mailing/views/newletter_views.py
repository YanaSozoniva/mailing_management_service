from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, View
from mailing.models import Newsletter
from mailing.forms import NewsletterForm
from django.core.cache import cache
from django.contrib import messages

from mailing.services import get_list_by_owner, send_email, update_status


class NewsletterList(LoginRequiredMixin, ListView):
    """Контроллер вывода списка рассылок"""

    model = Newsletter
    template_name = "mailing/newsletter/newsletter_list.html"
    context_object_name = "newsletters"

    def get_queryset(self):
        if not self.request.user.has_perm("mailing.view_newsletter"):
            return get_list_by_owner(self.request.user.id, Newsletter)
        return Newsletter.objects.all()


class NewsletterSendMail(LoginRequiredMixin, View):
    """Класс для отправки писем пользователям"""

    model = Newsletter
    template_name = "mailing/newsletter/newsletter_detail.html"
    context_object_name = "newsletters"

    def post(self, request, pk):
        newsletter = get_object_or_404(Newsletter, id=pk)
        if newsletter.status == "COMPLETED":
            messages.error(request, f"Рассылка не может быть инициирована, т.к. была завершена")
        else:
            self.send_emails(newsletter, request)
            messages.success(request, "Письма отправлены!")

        return redirect("mailing:newsletter_detail", pk=pk)

    @staticmethod
    def send_emails(newsletter, request):
        recipients = [recipient.email for recipient in newsletter.recipients.all()]
        update_status(newsletter)
        if newsletter.status != "COMPLETED":
            for recipient in recipients:
                send_email(newsletter, recipient)
        else:
            messages.error(
                request, f"Рассылка не может быть инициирована, т.к. дата окончания рассылки {newsletter.last_sending}"
            )


class NewsletterDetail(LoginRequiredMixin, DetailView):
    """Контроллер детализации рассылки"""

    model = Newsletter
    template_name = "mailing/newsletter/newsletter_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        newsletter = self.get_object()
        context["recipients"] = ", ".join([recipient.email for recipient in newsletter.recipients.all()])
        return context


class NewsletterCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Контроллер создания новой рассылки"""

    model = Newsletter
    form_class = NewsletterForm
    template_name = "mailing/newsletter/newsletter_form.html"
    success_url = reverse_lazy("mailing:newsletter_list")
    permission_required = "mailing.add_newsletter"

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class NewsletterUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Контроллер изменения рассылки"""

    model = Newsletter
    form_class = NewsletterForm
    template_name = "mailing/newsletter/newsletter_form.html"
    success_url = reverse_lazy("mailing:newsletter_list")
    permission_required = "mailing.change_newsletter"

    def get_success_url(self):
        return reverse("mailing:newsletter_detail", args=[self.kwargs.get("pk")])


class NewsletterDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Контроллер удаления получателя рассылок"""

    model = Newsletter
    template_name = "mailing/newsletter/newsletter_confirm_delete.html"
    success_url = reverse_lazy("mailing:newsletter_list")
    permission_required = "mailing.delete_newsletter"
