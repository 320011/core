from django.urls import path

from . import views

app_name = "analytics"

urlpatterns = [
    path("", views.view_landing, name='default'),
]
