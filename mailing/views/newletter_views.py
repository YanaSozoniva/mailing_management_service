from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from mailing.models import Newsletter
from mailing.forms import NewsletterForm
from django.core.cache import cache

from mailing.services import get_list_by_owner


class NewsletterList(LoginRequiredMixin, ListView):
    """Контроллер вывода списка рассылок"""

    model = Newsletter
    template_name = "mailing/newsletter/newsletter_list.html"
    context_object_name = "newsletters"

    def get_queryset(self):
        if not self.request.user.has_perm("mailing.view_newsletter"):
            return get_list_by_owner(self.request.user.id, Newsletter)
        return Newsletter.objects.all()


class NewsletterDetail(LoginRequiredMixin, DetailView):
    """Контроллер детализации рассылки"""

    model = Newsletter
    template_name = "mailing/newsletter/newsletter_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        newsletter = self.get_object()
        # Кэширование списка получателей
        cache_key = f"newsletter_{newsletter.id}_recipients"
        recipients = cache.get(cache_key)

        if not recipients:
            recipients = ", ".join([recipient.email for recipient in newsletter.recipients.all()])
            cache.set(cache_key, recipients, timeout=60)  # Кэшируем на 15 минут

        return context


class NewsletterCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Контроллер создания новой рассылки"""

    model = Newsletter
    form_class = NewsletterForm
    template_name = "mailing/newsletter/newsletter_form.html"
    success_url = reverse_lazy("mailing:newsletter_list")
    permission_required = 'mailing.add_newsletter'

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
    permission_required = 'mailing.change_newsletter'

    def get_success_url(self):
        return reverse('mailing:newsletter_detail', args=[self.kwargs.get('pk')])


class NewsletterDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Контроллер удаления получателя рассылок"""

    model = Newsletter
    template_name = "mailing/newsletter/newsletter_confirm_delete.html"
    success_url = reverse_lazy("mailing:newsletter_list")
    permission_required = 'mailing.delete_newsletter'
