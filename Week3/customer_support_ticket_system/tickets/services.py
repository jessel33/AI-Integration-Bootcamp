# services.py
#
# Service receives the incoming ticket information
# asks the repository for the customer
# stops if the customer does not exist
# builds the approved ticket_data
# asks the repository to create the ticket
# returns the created SupportTicket.

from .repositories import (
    create_support_ticket,
    get_customer_by_id,
    get_support_ticket_by_id,
)


def create_new_support_ticket(model_name, model_number, scope_of_work, customer_id):
    """Function accepts 4 arguments, call repositories for customer object, then creates support ticket data, send it to repositories then waits for returned created support ticket which it then returns back to views."""
    customer_object = get_customer_by_id(customer_id)

    if customer_object is None:
        return None
    else:
        ticket_data = {
            "model_name": model_name,
            "model_number": model_number,
            "scope_of_work": scope_of_work,
            "customer": customer_object,
            "repair_status": "Pending",
        }

        ticket = create_support_ticket(ticket_data)
        return ticket


def get_support_ticket(ticket_id):
    """Function accepts ticket_id(int) argument, call repositories for support ticket object, then return support ticket object or None."""
    support_ticket_object = get_support_ticket_by_id(ticket_id)

    if support_ticket_object is None:
        return None
    else:
        return support_ticket_object
