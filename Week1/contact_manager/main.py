# main.py file for Contact Management System
# Will work as the interface for the contact management system

from contact import Contact
from address import Address

jlaAddress = Address("400 River Ave. Apt# 2F", "PO BOX 112", "Emlenton", "PA", "16373", "USA")
jla33 = Contact(1, "Jesse", "jesse@amcsoftware.dev", "7244213733", "Phone")

print(f"Address is: {jlaAddress.get_info()}\n")
print(jla33.get_info())

