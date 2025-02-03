from django.core.cache import cache

from mailing.models import MailingRecipient, Message, Newsletter
from config.settings import CACHE_ENABLED


def get_list_by_owner(owner_id, model):
    """Функция получения списка указанной модели по владельцу из кеша, если кэш пустой - из бд"""

    if not CACHE_ENABLED:
        return model.objects.filter(owner=owner_id)
    key = f'{model}_list'
    list_model = cache.get(key)

    if list_model is not None:
        return list_model
    list_model = model.objects.filter(owner=owner_id)
    cache.set(key, list_model)
    return list_model
