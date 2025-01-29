from django.contrib import admin
from mailing.models import MailingRecipient, Message, Newsletter


@admin.register(MailingRecipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "surname", "email", "comment")
    list_filter = ("email",)
    search_fields = ("email", "last_name", "first_name")


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("subject_letter", "body_letter")
    list_filter = ("subject_letter",)
    search_fields = ("subject_letter", "body_letter")


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ("name", "first_sending", "last_sending", "status", "message")
    list_filter = ("name", "first_sending", "last_sending", "status",)
    search_fields = ("name", "message", "recipients")
