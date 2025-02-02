from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("users/", include("users.urls", namespace="users")),
    path("admin/", admin.site.urls),
    path("", include("mailing.urls", namespace="mailing")),
]
