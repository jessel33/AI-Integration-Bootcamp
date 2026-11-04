# views.py
# this views file handles both GET and POST requests
# coming from the forms.py
#
from django.shortcuts import render

from .ai_client import analyze_ticket
from .forms import TicketComplaintForm


def analyze_ticket_view(request):
    result = None
    error_message = None
    if request.method == "POST":
        form = TicketComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.cleaned_data["complaint"]
            result = analyze_ticket(complaint)
            if result is None:
                error_message = "Unable to analyze your complaint. Please try again."

    else:
        form = TicketComplaintForm()

    context = {"form": form, "result": result, "error_message": error_message}
    return render(request, "ai_analyzer/analyze_ticket.html", context)
