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
        exclude = ('owner',)


class MessageForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Message
        fields = ("subject_letter", "body_letter")


class NewsletterForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Newsletter
        exclude = ('owner',)

    def clean(self):
        """Валидация проверки ввода даты начало и конца рассылки (начало<конца)"""
        cleaned_data = super().clean()
        first_sending = cleaned_data.get("first_sending")
        last_sending = cleaned_data.get("last_sending")

        if last_sending < first_sending:
            self.add_error("last_sending", "Дата конца рассылки не может быть раньше начало самой рассылки")
