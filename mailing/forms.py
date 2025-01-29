from django.forms import ModelForm, BooleanField
from mailing.models import MailingRecipient, Message, Newsletter


class StyleFormMixin:
    """Стилизация форм"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-control"


class MailingRecipientForm(StyleFormMixin, ModelForm):
    class Meta:
        model = MailingRecipient
        fields = "__all__"


class MessageForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Message
        fields = ('subject_letter', 'body_letter')


class NewsletterForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Newsletter
        fields = "__all__"
