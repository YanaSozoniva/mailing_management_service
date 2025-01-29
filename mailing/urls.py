from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import (
    MailingRecipientList,
    MailingRecipientDetail,
    MailingRecipientCreate,
    MailingRecipientDelete,
    MailingRecipientUpdate,
    MessageList, MessageDelete, MessageDetail, MessageUpdate, MessageCreate,
)

app_name = MailingConfig.name

urlpatterns = [
    path("", MailingRecipientList.as_view(), name="recipient_list"),
    path("recipient/<int:pk>/", MailingRecipientDetail.as_view(), name="recipient_detail"),
    path("recipient/create/", MailingRecipientCreate.as_view(), name="recipient_create"),
    path("recipient/<int:pk>/delete/", MailingRecipientDelete.as_view(), name="recipient_delete"),
    path("recipient/<int:pk>/update/", MailingRecipientUpdate.as_view(), name="recipient_update"),

    path("message/", MessageList.as_view(), name="message_list"),
    path("message/<int:pk>/", MessageDetail.as_view(), name="message_detail"),
    path("message/create/", MessageCreate.as_view(), name="message_create"),
    path("message/<int:pk>/delete/", MessageDelete.as_view(), name="message_delete"),
    path("message/<int:pk>/update/", MessageUpdate.as_view(), name="message_update"),
]
