from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from .forms import (
    ChangeSupportTicketStatus,
    CustomerForm,
    SelectSupportTicket,
    SupportTicketForm,
)
from .services import (
    change_support_ticket_status,
    create_new_support_ticket,
    get_support_ticket,
    register_customer,
)


def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())


def customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer_name = form.cleaned_data["customer_name"]
            street = form.cleaned_data["street"]
            city = form.cleaned_data["city"]
            state = form.cleaned_data["state"]
            country = form.cleaned_data["country"]
            phone = form.cleaned_data["phone"]
            email = form.cleaned_data["email"]
            captured_customer = register_customer(
                customer_name, street, city, state, country, phone, email
            )
            if captured_customer is not None:
                customer_id = captured_customer.customer_id
                return redirect("registered", customer_id)
            else:
                return render(
                    request,
                    "customer.html",
                    {"form": form, "message": "Customer already in database."},
                )
        else:
            return render(request, "customer.html", {"form": form})
    else:
        form = CustomerForm()
        return render(request, "customer.html", {"form": form})


def supporttickets(request):
    if request.method == "POST":
        form = SupportTicketForm(request.POST)
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
                return redirect("success", ticket_id, "ticket_created")

            else:
                return render(
                    request,
                    "ticket.html",
                    {"form": form, "message": "Customer was not found in database."},
                )
        else:
            return render(request, "ticket.html", {"form": form})
    else:
        form = SupportTicketForm()
        return render(request, "ticket.html", {"form": form})


def select_support_ticket(request, purpose):
    if request.method == "POST":
        form = SelectSupportTicket(request.POST)
        if form.is_valid():
            ticket_id = form.cleaned_data["ticket_id"]
            captured_ticket = get_support_ticket(ticket_id)
            if captured_ticket is not None:
                ticket_id = captured_ticket.ticket_id
                if purpose == "view":
                    return redirect("view_support_ticket", ticket_id)

                return redirect("change_ticket_status", ticket_id)
            else:
                return render(
                    request,
                    "ticket_selection.html",
                    {
                        "form": form,
                        "message": "Support ticket not found. Please enter another ticket number.",
                    },
                )
        else:
            return render(
                request,
                "ticket_selection.html",
                {"form": form},
            )
    else:
        form = SelectSupportTicket()
        return render(request, "ticket_selection.html", {"form": form})


@login_required
def change_ticket_status(request, ticket_id):
    captured_ticket = get_support_ticket(ticket_id)
    if captured_ticket is None:
        raise Http404
    elif request.method == "POST":
        form = ChangeSupportTicketStatus(request.POST)
        if form.is_valid():
            new_status = form.cleaned_data["repair_status"]
            changed_by = request.user
            changed_support_ticket = change_support_ticket_status(
                ticket_id, new_status, changed_by
            )
            if changed_support_ticket is None:
                return render(
                    request,
                    "change_ticket_status.html",
                    {"form": form, "captured_ticket": captured_ticket},
                )
            else:
                _ticket, status_change = changed_support_ticket

                if status_change:
                    return redirect("success", ticket_id, "status_changed")
                else:
                    return redirect("success", ticket_id, "status_unchanged")
        else:
            return render(
                request,
                "change_ticket_status.html",
                {"form": form, "captured_ticket": captured_ticket},
            )
    else:
        form = ChangeSupportTicketStatus(instance=captured_ticket)
        return render(
            request,
            "change_ticket_status.html",
            {"form": form, "captured_ticket": captured_ticket},
        )


@login_required
def view_support_ticket(request, ticket_id):
    captured_ticket = get_support_ticket(ticket_id)
    if captured_ticket is None:
        raise Http404

    template = loader.get_template("view_support_ticket.html")
    context = {
        "support_ticket": captured_ticket,
    }
    return HttpResponse(template.render(context, request))


def success(request, ticket_id, operation):
    support_ticket = get_support_ticket(ticket_id)
    if support_ticket is None:
        raise Http404

    if operation == "status_changed":
        message = "Status successfully changed."
        declaration_message = "Success!"

    elif operation == "status_unchanged":
        message = f"No changes made.  Repair status is already {support_ticket.repair_status}."
        declaration_message = "No Changes Made"

    elif operation == "ticket_created":
        message = "Your request has been processed."
        declaration_message = "Success!"

    else:
        raise Http404

    template = loader.get_template("success.html")
    context = {
        "support_ticket": support_ticket,
        "title": "Customer Information",
        "declaration_message": declaration_message,
        "message": message,
    }
    return HttpResponse(template.render(context, request))
