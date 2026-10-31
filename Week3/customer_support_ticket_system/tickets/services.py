# services.py
#
# Service receives the incoming ticket information
# asks the repository for the customer
# stops if the customer does not exist
# builds the approved ticket_data
# asks the repository to create the ticket
# returns the created SupportTicket.
from django.db import transaction

from .ai_client import summarize_scope_of_work
from .repositories import (
    create_customer,
    create_support_ticket,
    create_ticket_status_history,
    get_customer_by_id,
    get_support_ticket_by_id,
    update_support_ticket_status,
    update_support_ticket_summary,
)


def register_customer(customer_name, street, city, state, country, phone, email):
    """Function accepts 7 arguments, creates customer data, send it to repositories then waits for returned created customer object which it then returns back to views."""
    customer_data = {
        "customer_name": customer_name,
        "street": street,
        "city": city,
        "state": state,
        "country": country,
        "phone": phone,
        "email": email,
    }

    customer = create_customer(customer_data)
    return customer


def create_new_support_ticket(
    model_name, model_number, scope_of_work, customer_id, priority
):
    """Function accepts 5 arguments, call repositories for customer object, then creates support ticket data, send it to repositories then waits for returned created support ticket which it then returns back to views."""
    customer_object = get_customer_by_id(customer_id)

    if customer_object is None:
        return None
    else:
        ticket_data = {
            "model_name": model_name,
            "model_number": model_number,
            "scope_of_work": scope_of_work,
            "customer": customer_object,
            "priority": priority,
            "repair_status": "Pending",
        }

        ticket = create_support_ticket(ticket_data)
        return ticket


def get_support_ticket(ticket_id):
    """Function accepts ticket_id(int) argument, calls repositories for support ticket object, then returns support ticket object or None."""
    support_ticket_object = get_support_ticket_by_id(ticket_id)

    if support_ticket_object is None:
        return None
    else:
        return support_ticket_object


def change_support_ticket_status(ticket_id, new_status, changed_by):
    support_ticket_object = get_support_ticket_by_id(ticket_id)

    if support_ticket_object is None:
        return None

    elif support_ticket_object.repair_status == new_status:
        return (support_ticket_object, False)

    else:
        history_data = {
            "ticket": support_ticket_object,
            "status": new_status,
            "changed_by": changed_by,
        }

        with transaction.atomic():
            changed_support_ticket = update_support_ticket_status(
                support_ticket_object, new_status
            )

            create_ticket_status_history(history_data)

        return (changed_support_ticket, True)


def generate_support_ticket_summary(ticket_id):
    support_ticket_object = get_support_ticket_by_id(ticket_id)

    if support_ticket_object is None:
        return None

    support_ticket_summary = summarize_scope_of_work(
        support_ticket_object.scope_of_work
    )
    if support_ticket_summary is None:
        return None

    updated_support_ticket_ai_summary = update_support_ticket_summary(
        support_ticket_object, support_ticket_summary
    )

    return updated_support_ticket_ai_summary
