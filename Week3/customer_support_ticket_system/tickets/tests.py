from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Customer, SupportTicket


class TicketSummaryViewTests(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            customer_name="Harry L. Clark",
            street="West Home Rd",
            city="Union City",
            state="PA",
            country="USA",
            phone="(814) 775-0940",
            email="hlclark@unionstrong.com",
        )

        self.ticket = SupportTicket.objects.create(
            model_name="SpeedRoute 5G",
            model_number="SR-500",
            scope_of_work="I cannot reassign - change my local LAN URL.",
            customer=self.customer,
            ai_summary="Customer cannot make changes to their local LAN URL.",
        )

        self.user = get_user_model().objects.create_user(username="sreinhard")
        self.client.force_login(self.user)

    def test_summary_failure_preserves_existing_summary(self):
        url = reverse("view_support_ticket", args=[self.ticket.ticket_id])
        original_summary = self.ticket.ai_summary

        with patch("tickets.views.generate_support_ticket_summary", return_value=None):
            response = self.client.post(url)

        self.assertContains(
            response, "Could not generate an AI summary. Please try again."
        )
        self.assertContains(response, self.ticket.ai_summary)
        self.ticket.refresh_from_db()

        self.assertEqual(self.ticket.ai_summary, original_summary)
