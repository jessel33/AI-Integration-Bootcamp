from django import forms

from .models import Customer, ServiceRepresentative, SupportTicket


class SupportTicket(forms.ModelForm):
    class Meta:
        model = SupportTicket
        fields = [
            "model_name",
            "model_number",
            "scope_of_work",
            "customer",
            "service_rep",
            "service_rep_notes",
            "repair_status",
            "ticket_completed_at",
        ]


class Customer(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            "customer_name",
            "street",
            "city",
            "state",
            "country",
            "phone",
            "email",
        ]


class ServiceRepresentative(forms.ModelForm):
    class Meta:
        model = ServiceRepresentative
        fields = [
            "service_rep_id",
            "service_rep_name",
            "phone",
            "email",
            "start_date",
            "specialization",
        ]
