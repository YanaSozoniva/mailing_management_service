from django.db import models


class MailingRecipient(models.Model):
    """Модель Получатель рассылок"""

    email = models.EmailField(unique=True, verbose_name="Email", help_text="Укажите вашу электронную почту")
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    surname = models.CharField(max_length=100, verbose_name="Отчество", null=True, blank=True)
    comment = models.TextField(verbose_name="Комментарий", null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} email: {self.email}"

    class Meta:
        verbose_name = "получатель"
        verbose_name_plural = "получатели"
        ordering = ["last_name", "first_name"]


class Message(models.Model):
    """Модель Сообщение"""

    subject_letter = models.CharField(max_length=200, verbose_name="Тема письма")
    body_letter = models.TextField(verbose_name="Тело письма", null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.subject_letter}"

    class Meta:
        verbose_name = "сообщение"
        verbose_name_plural = "сообщения"
        ordering = ["subject_letter"]


class Newsletter(models.Model):
    """Модель Рассылка"""

    CREATED = "create"
    LAUNCHED = "launch"
    COMPLETED = "complete"

    STATUS_CHOICES = [
        (CREATED, "Создана"),
        (LAUNCHED, "Запущена"),
        (COMPLETED, "Завершена"),
    ]
    name = models.CharField(max_length=50, verbose_name="Название рассылки")
    first_sending = models.DateTimeField(verbose_name="Дата и время создания первой рассылки", null=True, blank=True)
    last_sending = models.DateField(verbose_name="Дата и время последней рассылки", null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=CREATED, verbose_name="статус рассылки")
    message = models.ForeignKey(
        to=Message,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="newsletters",
        verbose_name="Сообщение",
    )
    recipients = models.ManyToManyField(
        to=MailingRecipient, related_name="newsletters", verbose_name="Получатели рассылки"
    )

    def __str__(self):
        return f"{self.name}: Дата первой рассылки: {self.first_sending}, дата последней рассылки: {self.last_sending}"

    class Meta:
        verbose_name = "рассылка"
        verbose_name_plural = "рассылки"
        ordering = ["name", "first_sending", "last_sending"]
