from django.views.generic import TemplateView
from mailing.models import Newsletter, MailingRecipient


class HomeViews(TemplateView):
    """Контроллер для отображения статистических данных на главной страницы проекта: количество всех рассылок,
    количество активных рассылок (со статусом 'Запущена') и количество уникальных получателей."""
    template_name = "mailing/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["newsletter_count"] = Newsletter.objects.all().count()
        context["activ_newsletter_count"] = Newsletter.objects.filter(status='launch').count()
        context["recipient_count"] = MailingRecipient.objects.all().count()
        return context
