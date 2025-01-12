from django.forms import ModelForm
from mailing.models import MailingRecipient, Message, Newsletter


class MailingRecipientForm(ModelForm):
    class Meta:
        model = MailingRecipient
        fields = "__all__"
