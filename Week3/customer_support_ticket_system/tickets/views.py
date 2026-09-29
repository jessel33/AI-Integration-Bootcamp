from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from .forms import SupportTicket
from .services import create_new_support_ticket, get_support_ticket


def supporttickets(request):
    if request.method == "POST":
        form = SupportTicket(request.POST)
        if form.is_valid():
            model_name = form.cleaned_data["model_name"]
            model_number = form.cleaned_data["model_number"]
            scope_of_work = form.cleaned_data["scope_of_work"]
            customer_object = form.cleaned_data["customer"]
            customer_id = customer_object.customer_id
            captured_support_ticket = create_new_support_ticket(
                model_name, model_number, scope_of_work, customer_id
            )
            if captured_support_ticket is not None:
                ticket_id = captured_support_ticket.ticket_id
                return redirect("success", ticket_id)

            else:
                return render(
                    request,
                    "ticket.html",
                    {"form": form, "message": "Customer was not found in database."},
                )
        else:
            return render(request, "ticket.html", {"form": form})
    else:
        form = SupportTicket()
        return render(request, "ticket.html", {"form": form})


def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())


def success(request, ticket_id):
    support_ticket = get_support_ticket(ticket_id)
    if support_ticket is None:
        raise Http404
    template = loader.get_template("success.html")
    context = {"support_ticket": support_ticket}
    return HttpResponse(template.render(context, request))
