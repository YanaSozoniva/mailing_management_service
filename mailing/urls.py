from django.urls import path
from django.views.decorators.cache import cache_page

from mailing.apps import MailingConfig
from mailing.views import (
    MailingRecipientList,
    MailingRecipientDetail,
    MailingRecipientCreate,
    MailingRecipientDelete,
    MailingRecipientUpdate,
    MessageList,
    MessageDelete,
    MessageDetail,
    MessageUpdate,
    MessageCreate,
    NewsletterList,
    NewsletterCreate,
    NewsletterDelete,
    NewsletterDetail,
    NewsletterUpdate,
    HomeViews,
    MailingAttemptView,
    NewsletterSendMail,
)

app_name = MailingConfig.name

urlpatterns = [
    path("", HomeViews.as_view(), name="home"),
    path("attempt/", MailingAttemptView.as_view(), name="attempt"),
    path("recipient/", cache_page(60)(MailingRecipientList.as_view()), name="recipient_list"),
    path("recipient/<int:pk>/", MailingRecipientDetail.as_view(), name="recipient_detail"),
    path("recipient/create/", MailingRecipientCreate.as_view(), name="recipient_create"),
    path("recipient/<int:pk>/delete/", MailingRecipientDelete.as_view(), name="recipient_delete"),
    path("recipient/<int:pk>/update/", MailingRecipientUpdate.as_view(), name="recipient_update"),
    path("message/", cache_page(60)(MessageList.as_view()), name="message_list"),
    path("message/<int:pk>/", MessageDetail.as_view(), name="message_detail"),
    path("message/create/", MessageCreate.as_view(), name="message_create"),
    path("message/<int:pk>/delete/", MessageDelete.as_view(), name="message_delete"),
    path("message/<int:pk>/update/", MessageUpdate.as_view(), name="message_update"),
    path("newsletter/", cache_page(60)(NewsletterList.as_view()), name="newsletter_list"),
    path("newsletter/<int:pk>/", NewsletterDetail.as_view(), name="newsletter_detail"),
    path("newsletter/create/", NewsletterCreate.as_view(), name="newsletter_create"),
    path("newsletter/<int:pk>/delete/", NewsletterDelete.as_view(), name="newsletter_delete"),
    path("newsletter/<int:pk>/update/", NewsletterUpdate.as_view(), name="newsletter_update"),
    path("newsletter/<int:pk>/sendmail", NewsletterSendMail.as_view(), name="newsletter_sendmail"),
]
