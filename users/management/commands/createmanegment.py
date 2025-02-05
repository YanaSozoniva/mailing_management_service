from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    """Кастомная команда для создания группы Менеджер"""

    def handle(self, *args, **options):
        manager_group = Group.objects.create(name="Менеджер")
        view_recipients_permission = Permission.objects.get(codename="view_mailingrecipient")
        view_message_permission = Permission.objects.get(codename="view_message")
        view_newsletter_permission = Permission.objects.get(codename="view_newsletter")
        view_user_permission = Permission.objects.get(codename="view_user")
        block_user_permission = Permission.objects.get(codename="can_block_users")
        disable_newsletter_permission = Permission.objects.get(codename="can_disable_newsletter")

        # Назначаем разрешения группе
        manager_group.permissions.add(
            view_user_permission,
            view_newsletter_permission,
            view_recipients_permission,
            view_message_permission,
            block_user_permission,
            disable_newsletter_permission,
        )
        self.stdout.write(self.style.SUCCESS(f"Successfully created group {manager_group.name}"))
