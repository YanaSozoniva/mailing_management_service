from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from mailing.models import Newsletter
from mailing.forms import NewsletterForm
from django.core.cache import cache


class NewsletterList(ListView):
    """Контроллер вывода списка рассылок"""

    model = Newsletter
    template_name = "mailing/newsletter/newsletter_list.html"
    context_object_name = "newsletters"


class NewsletterDetail(DetailView):
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
            cache.set(cache_key, recipients, timeout=60 * 15)  # Кэшируем на 15 минут

        return context


class NewsletterCreate(CreateView):
    """Контроллер создания новой рассылки"""

    model = Newsletter
    form_class = NewsletterForm
    template_name = "mailing/newsletter/newsletter_form.html"
    success_url = reverse_lazy("mailing:newsletter_list")


class NewsletterUpdate(UpdateView):
    """Контроллер изменения рассылки"""

    model = Newsletter
    form_class = NewsletterForm
    template_name = "mailing/newsletter/newsletter_form.html"
    success_url = reverse_lazy("mailing:newsletter_list")


class NewsletterDelete(DeleteView):
    """Контроллер удаления получателя рассылок"""

    model = Newsletter
    template_name = "mailing/newsletter/newsletter_confirm_delete.html"
    success_url = reverse_lazy("mailing:newsletter_list")
