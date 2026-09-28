from django.urls import path

from . import views

urlpatterns = [
    path("success/<int:ticket_id>/", views.success, name="success"),
    path("supporttickets/", views.supporttickets, name="supportticket"),
]
