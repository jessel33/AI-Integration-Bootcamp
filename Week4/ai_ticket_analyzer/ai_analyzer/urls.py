from django.urls import path

from . import views

urlpatterns = [
    path("ticket/", views.analyze_ticket_view, name="analyze_ticket"),
    path("main/", views.main, name="main"),
]
