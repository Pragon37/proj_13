from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #    path('lettings/', views.lettings_index, name='lettings_index'),
    #    path('lettings/<int:letting_id>/', views.letting, name='letting'),
    #    path('profiles/', views.profiles_index, name='profiles_index'),
    #    path('profiles/<str:username>/', views.profile, name='profile'),
    path("", include("lettings.urls")),
    path("", include("profiles.urls")),
    path("admin/", admin.site.urls),
]
