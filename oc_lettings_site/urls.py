from django.contrib import admin
from django.urls import include, path

from . import views


def trigger_error(request):
    division_by_zero = 1 / 0   # noqa F841


urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls", namespace="lettings")),
    path("profiles/", include("profiles.urls", namespace="profiles")),
    path("admin/", admin.site.urls),
    path('sentry-debug/', trigger_error),
]
