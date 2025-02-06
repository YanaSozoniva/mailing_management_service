from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from mailing.models import Newsletter


class DisableNewsletterView(LoginRequiredMixin, View):

    def post(self, request, pk):
        newsletter = get_object_or_404(Newsletter, id=pk)

        if not request.user.has_perm("mailing.can_disable_newsletter"):
            raise PermissionDenied("У вас нет права на отключение/включение рассылки")

        if newsletter.status == "complete":
            newsletter.status = "launch"
        else:
            newsletter.status = "complete"

        newsletter.save()

        return redirect("mailing:newsletter_detail", pk=pk)
