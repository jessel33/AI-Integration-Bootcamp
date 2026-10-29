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
    path(
        "ticket_selection/",
        views.select_support_ticket,
        {"purpose": "change_status"},
        name="ticket_selection",
    ),
    path(
        "ticket_selection/view/",
        views.select_support_ticket,
        {"purpose": "view"},
        name="ticket_selection_view",
    ),
    path(
        "view_support_ticket/<int:ticket_id>/",
        views.view_support_ticket,
        name="view_support_ticket",
    ),
    path("main/", views.main, name="main"),
    path("customer/", views.customer, name="customer"),
    path("registered/", views.customer, name="customer"),
]
