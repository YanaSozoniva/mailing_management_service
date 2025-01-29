from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from mailing.models import Newsletter
from mailing.forms import NewsletterForm

class NewsletterList(ListView):
    """Контроллер вывода списка рассылок"""

    model = Newsletter
    context_object_name = "newsletters"


class NewsletterDetail(DetailView):
    """Контроллер детализации рассылки"""

    model = Newsletter


class NewsletterCreate(CreateView):
    """Контроллер создания новой рассылки"""

    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy("mailing:newsletter_list")


class NewsletterUpdate(UpdateView):
    """Контроллер изменения рассылки"""

    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy("mailing:newsletter_list")


class NewsletterDelete(DeleteView):
    """Контроллер удаления получателя рассылок"""

    model = Newsletter
    success_url = reverse_lazy("mailing:newsletter_list")
