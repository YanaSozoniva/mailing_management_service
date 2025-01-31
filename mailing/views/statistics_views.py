from django.views.generic import ListView
from mailing.models import MailingAttempt


class MailingAttemptView(ListView):
    """Контроллер вывода информации по попыткам отправки рассылок фильтруя в контроллере по конкретному пользователю"""

    model = MailingAttempt
    template_name = "mailing/attempt.html"
    context_object_name = "attempts"
