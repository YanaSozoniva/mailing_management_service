from django.urls import path
from mailing.apps import MailingConfig
from  mailing.views import MailingRecipientList, MailingRecipientDetail, MailingRecipientCreate, MailingRecipientDelete, MailingRecipientUpdate

app_name = MailingConfig.name

urlpatterns = [
    path("", MailingRecipientList.as_view(), name="recipient_list"),
    path("recipient/<int:pk>/", MailingRecipientDetail.as_view(), name="recipient_detail"),
    path("recipient/create/", MailingRecipientCreate.as_view(), name="recipient_create"),
    path("recipient/<int:pk>/delete/", MailingRecipientDelete.as_view(), name="recipient_delete"),
    path("recipient/<int:pk>/update/", MailingRecipientUpdate.as_view(), name="recipient_update"),
]
