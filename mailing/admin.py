from django.contrib import admin
from mailing.models import MailingRecipient


@admin.register(MailingRecipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "surname", "email", "comment")
    list_filter = ("email",)
    search_fields = ("email", "last_name", "first_name")
