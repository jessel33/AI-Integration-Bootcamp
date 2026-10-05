# repositories.py
# Handle sending data to ORM for support ticket creation and persistance.
# Gets customer infomation from requests by the customer's id.
# Gets support ticket information from requests.
#

from tickets.models import Customer, SupportTicket, TicketStatusHistory


def get_customer_by_id(customer_id):
    """This function takes an integer representing the customer desired from the database and it returns the customer model object if one exists or it will return None"""
    try:
        customer = Customer.objects.get(pk=customer_id)
        return customer
    except Customer.DoesNotExist:
        return None


def get_support_ticket_by_id(ticket_id):
    """This function takes an integer representing the support ticket desired from the database and it returns the support ticket model object if one exists or it will return None"""
    try:
        support_ticket = SupportTicket.objects.get(pk=ticket_id)
        return support_ticket
    except SupportTicket.DoesNotExist:
        return None


def create_support_ticket(ticket_data):
    """This function takes a dictionary from the service layer, places it into the proper commands for ORM object model creation, sends this onto the ORM for model object creation, once the object model is created it then will return a supportticket model object"""
    support_ticket = SupportTicket.objects.create(**ticket_data)
    return support_ticket


def update_support_ticket_status(support_ticket, new_status):
    """This function takes a Support Ticket object with an updated repair status. Then it changes the repair status and saves that change through the ORM."""
    support_ticket.repair_status = new_status
    support_ticket.save(update_fields=["repair_status"])
    return support_ticket


def create_ticket_status_history(history_data):
    """This function takes the support ticket number, the updated repair status, and the user who is changing it, then sends this onto the ORM for model object creation, once the object model is created it then will return a ticket_status_history model object"""
    ticket_status_history = TicketStatusHistory.objects.create(**history_data)
    return ticket_status_history
