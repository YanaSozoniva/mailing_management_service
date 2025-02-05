from django.utils import timezone
from django.contrib import messages
from django.core.cache import cache
from config.settings import CACHE_ENABLED, EMAIL_HOST_USER
from django.core.mail import send_mail
from mailing.models import MailingAttempt


def get_list_by_owner(owner_id, model):
    """Функция получения списка указанной модели по владельцу из кеша, если кэш пустой - из бд"""

    if not CACHE_ENABLED:
        return model.objects.filter(owner=owner_id)
    key = f"{model}_list"
    list_model = cache.get(key)

    if list_model is not None:
        return list_model
    list_model = model.objects.filter(owner=owner_id)
    cache.set(key, list_model)
    return list_model


def send_email(newsletter, email):
    """Функция отправки сообщений пользователям и занесение данных по результатам рассылки"""
    try:
        mail_response = send_mail(
            subject=newsletter.message.subject_letter,
            message=newsletter.message.body_letter,
            from_email=EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
        )
    except Exception as e:
        mail_response = e

    MailingAttempt.objects.create(
        status=MailingAttempt.SUCCESS if mail_response == 1 else MailingAttempt.FAILURE,
        mail_response=mail_response if mail_response != 1 else "",
        newsletter=newsletter,
        email_recipient=email,
    )


def update_status(newsletter):
    """Функция изменения статуса рассылки с учетом текущей даты"""
    now = timezone.now()
    if newsletter.last_sending < now:
        newsletter.status = "COMPLETED"
    elif newsletter.status != "COMPLETED":
        newsletter.status = "Запущена"
    newsletter.save()
