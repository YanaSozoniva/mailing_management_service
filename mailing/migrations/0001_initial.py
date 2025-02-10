# Generated by Django 5.1.4 on 2025-01-08 09:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MailingRecipient",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "email",
                    models.EmailField(
                        help_text="Укажите вашу электронную почту", max_length=254, verbose_name="Email"
                    ),
                ),
                ("first_name", models.CharField(max_length=100, verbose_name="Имя")),
                ("last_name", models.CharField(max_length=100, verbose_name="Фамилия")),
                ("surname", models.CharField(blank=True, max_length=100, null=True, verbose_name="Отчество")),
                ("comment", models.TextField(blank=True, null=True, verbose_name="Комментарий")),
            ],
            options={
                "verbose_name": "получатель",
                "verbose_name_plural": "получатели",
                "ordering": ["last_name", "first_name"],
            },
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("subject_letter", models.CharField(max_length=200, verbose_name="Тема письма")),
                ("body_letter", models.TextField(verbose_name="Тело письма")),
            ],
            options={
                "verbose_name": "сообщение",
                "verbose_name_plural": "сообщения",
                "ordering": ["subject_letter"],
            },
        ),
        migrations.CreateModel(
            name="Newsletter",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=50, verbose_name="Название рассылки")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания первой рассылки"),
                ),
                ("updated_at", models.DateField(auto_now=True, verbose_name="Дата и время последней рассылки")),
                (
                    "status",
                    models.CharField(
                        choices=[("create", "Создана"), ("launch", "Запущена"), ("complete", "Завершена")],
                        default="create",
                        max_length=15,
                        verbose_name="статус рассылки",
                    ),
                ),
                (
                    "message",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="newsletters",
                        to="mailing.message",
                        verbose_name="Сообщение",
                    ),
                ),
                (
                    "recipients",
                    models.ManyToManyField(
                        related_name="newsletters", to="mailing.mailingrecipient", verbose_name="Получатели рассылки"
                    ),
                ),
            ],
            options={
                "verbose_name": "рассылка",
                "verbose_name_plural": "рассылки",
                "ordering": ["name", "created_at", "updated_at"],
            },
        ),
    ]
