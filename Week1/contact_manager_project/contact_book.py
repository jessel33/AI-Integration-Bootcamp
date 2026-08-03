# contact_book.py
# ContactBook class
# For Project: 
# Contact Management System
# This file will:
# - Add Contact to Contact Book
# - Update Contact
# - Search Contacts
# - Delete Contact
# Focus of this Project:
# Code organization
# Classes
# Error handling

"""Best flow
Create one ContactBook when the program starts.
Show a menu such as:
Add contact
Search contacts
Update contact
Delete contact
Exit

When the user chooses Add contact:
Gather the information
Create the Address
Create the Contact
Pass the completed contact to ContactBook.add_contact()"""


class ContactBook:
    def __init__(self):
        self.__contacts = []

    def __str__(self):
        if not self.__contacts:
            return "Contact book is empty."
        output = "Contact Book:\n"
        for contact in self.__contacts:
            output += f" - {contact}\n"
        return output.strip()
    

    def get_info(self):
        return str(self)
    

    def get_next_id(self):
        if not self.__contacts:
            return 1
        
        return self.__contacts[-1].internal_id + 1
    
        
    def add_contact_to_contact_book(self, new_contact):
        for contact in self.__contacts:
            if contact.contact_name.strip().lower() == new_contact.contact_name.strip().lower():
                return False

        self.__contacts.append(new_contact)
        return True
    

    def update_contact(self, target_contact, **kwargs):
        contact = self.search_contacts(target_contact)
        if contact is None:
            return None
        
        return contact.update_fields(**kwargs)
    

    def search_contacts(self, target_contact):
        for contact in self.__contacts:
            if contact.contact_name.strip().lower() == target_contact.strip().lower():
                return contact
            
        return None
    

    def delete_contact(self, target_contact):
        contact = self.search_contacts(target_contact)
        if contact is None:
            return False

        self.__contacts.remove(contact)
        return True
    

    def list_of_contact_dict(self):
        contact_dict_list = []
        for contact in self.__contacts:
            contact_dict_list.append(contact.to_dict())

        return contact_dict_list

