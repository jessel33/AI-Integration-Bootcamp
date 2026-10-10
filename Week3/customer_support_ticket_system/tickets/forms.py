from django import forms

from .models import Customer, ServiceRepresentative, SupportTicket


class SupportTicketForm(forms.ModelForm):
    class Meta:
        model = SupportTicket
        fields = (
            "model_name",
            "model_number",
            "scope_of_work",
            "customer",
        )


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            "customer_name",
            "street",
            "city",
            "state",
            "country",
            "phone",
            "email",
        )


class ServiceRepresentativeForm(forms.ModelForm):
    class Meta:
        model = ServiceRepresentative
        fields = (
            "service_rep_id",
            "service_rep_name",
            "phone",
            "email",
            "start_date",
            "specialization",
        )


class ChangeSupportTicketStatus(forms.ModelForm):
    class Meta:
        model = SupportTicket
        fields = ("repair_status",)


class SelectSupportTicket(forms.Form):
    ticket_id = forms.IntegerField()
