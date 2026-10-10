from django.shortcuts import redirect, render

from .forms import SupportTicket
from .services import get_support_ticket


def updatesupporttickets(request):
    if request.method == "POST":
        form = SupportTicket(request.POST)
        if form.is_valid():
            repair_status = form.cleaned_data["repair_status"]
            retrieved_support_ticket = get_support_ticket(ticket_id)
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
