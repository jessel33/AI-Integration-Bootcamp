# repositories.py
# Handle sending data to ORM for support ticket creation and persistance.
# Gets customer infomation from requests by the customer's id.
# Gets support ticket information from requests.
#

from tickets.models import Customer, SupportTicket


def get_customer_by_id(customer_id):
    """This function takes an integer representing the customer desired from the database and it returns the customer model object if one exists or it will return None"""
    try:
        customer = Customer.objects.get(pk=customer_id)
        return customer
    except Customer.DoesNotExist:
        return None


def create_support_ticket(ticket_data):
    """This function takes a dictionary from the service layer, places it into the proper commands for ORM object model creation, sends this onto the ORM for model object creation, once the object model is created it then will return a supportticket model object"""
    support_ticket = SupportTicket.objects.create(**ticket_data)
    return support_ticket
