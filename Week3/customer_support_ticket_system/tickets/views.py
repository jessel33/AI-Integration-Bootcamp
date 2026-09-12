from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from .forms import SupportTicket


def supporttickets(request):
    if request.method == "POST":
        form = SupportTicket(request.POST)
        if form.is_valid():
            model_name = form.cleaned_data["model_name"]
            model_number = form.cleaned_data["model_number"]
            scope_of_work = form.cleaned_data["scope_of_work"]
            customer = form.cleaned_data["customer"]
            service_rep = form.cleaned_data["service_rep"]
            service_rep_notes = form.cleaned_data["service_rep_notes"]
            repair_status = form.cleaned_data["repair_status"]
            ticket_completed_at = form.cleaned_data["ticket_complete_at"]

            form.save()

            return redirect("success")

        else:
            pass
    else:
        form = SupportTicket()
    return render(request, "ticket.html", {"form": form})


def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())


def success(request):
    template = loader.get_template("success.html")
    return HttpResponse(template.render())
