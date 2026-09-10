# repositories.py
# Handle sending data to ORM for support ticket creation and persistance.
# Gets customer infomation from requests by the customer's id.
# Gets support ticket information from requests.
#
from tickets.models import Customer


def get_customer_by_id(customer_id):
    """This function take an integer representing the customer desired from the database and it returns the customer model object if one exists or it will print out a 'does not exist' statement plus return None"""
    customer = {}
    customer = Customer.objects.filter(pk=customer_id).all()

    if not customer.exists():
        print(f"The requested customer ID {customer_id} does not exist.")
        return None
    else:
        return customer


def create_support_ticket(ticket_data):
    """This function will return a supportticket model object"""
