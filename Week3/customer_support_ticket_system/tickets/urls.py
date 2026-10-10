from django.urls import path

from . import views

urlpatterns = [
    path("success/<int:ticket_id>/<str:operation>/", views.success, name="success"),
    path("supporttickets/", views.supporttickets, name="supportticket"),
    path(
        "change_ticket_status/<int:ticket_id>/",
        views.change_ticket_status,
        name="change_ticket_status",
    ),
    path("ticket_selection/", views.select_support_ticket, name="ticket_selection"),
    path("main/", views.main, name="main"),
]
