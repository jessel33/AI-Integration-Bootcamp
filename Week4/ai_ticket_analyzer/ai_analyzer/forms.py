# forms.py
# form to create the complaint ticket form.
#
from django import forms


class TicketComplaintForm(forms.Form):
    complaint = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))
