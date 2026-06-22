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

    @property
    def contacts(self):
        return self._contacts
 
    def __str__(self):
        if not self._contacts:
            return "Contact book is empty."
        output = "Contact Book:\n"
        for contact in self._contacts:
            output += f" - {contact}\n"
        return output.strip()

    def store_list_of_contacts(self, existing_contact_list):
        for contact in existing_contact_list:
            for existing_contact in self._contacts:
                if existing_contact.email == contact.email:
                    return False
            if not isinstance(contact, dict):
                raise TypeError(f"Expected a dictionary, but got {type(contact).__name__}")
                return False
            self._contacts.append(contact)
            return True
                     
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
    
    def search_contacts(self, query: str):
        query_lower = query.lower()

        for contact in self._contacts:
            if query_lower in contact.name.lower() or query_lower in contact.email.lower():
                return contact.to_dict()
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
    