# contact_book.py
# ContactBook class should be responsible for:
# - storing a list of Contact objects
# - adding a contact
# - removing a contact
# - searching contacts
# - listing all contacts
# - updating an existing contact
# Before coding, decide how will this class uniquely identify a contact,
# for update/remove/search?

class ContactBook:
    def __init__(self):
        self._contacts = []
                     
    def load_contacts(self, existing_contacts_list):
        self._contacts = existing_contacts_list

    def add_contact(self, contact):
        for existing_contact in self._contacts:
            if existing_contact.email == contact.email:
                return False
        self._contacts.append(contact)
        return True
        
    def remove_contact(self, email):
        for contact in self._contacts:
            if contact.email == email:
                self._contacts.remove(contact)
                return True
        return False
    
    def find_by_email(self, email):
        for contact in self._contacts:
            if contact.email == email:
                return contact
        return None
    
    def list_all_contacts(self):
        return self._contacts.copy()
    
    def update_existing_contact(self, id_email, **kwargs):
        if "email" in kwargs:
            return False
        for contact in self._contacts:
            if contact.email == id_email:
                contact.update_fields(**kwargs)
                return True
        return False
