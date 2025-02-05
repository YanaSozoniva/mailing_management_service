from django.core.management.base import BaseCommand
from mailing.models import Newsletter
from mailing.services import send_email, update_status


class Command(BaseCommand):
    help = "Отправляет письма для активных рассылок"

    def handle(self, *args, **kwargs):
        # Получаем все активные и созданные рассылки
        newsletters = Newsletter.objects.filter(status="Запущена" or "Создана")

        for newsletter in newsletters:
            self.stdout.write(f"Обработка рассылки: {newsletter.name}")
            update_status(newsletter)

            if newsletter.status != "COMPLETED":
                recipients = [recipient.email for recipient in newsletter.recipients.all()]

                for recipient in recipients:
                    send_email(newsletter, recipient)
                    self.stdout.write(f"Письмо отправлено на {recipient}")
            else:
                self.stdout.write(f"Рассылка {newsletter.name} завершена и не может быть отправлена.")

        self.stdout.write(self.style.SUCCESS("Все рассылки обработаны!"))
