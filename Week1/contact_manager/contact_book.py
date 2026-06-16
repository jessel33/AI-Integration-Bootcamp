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

from dataclasses import dataclass, field
from contact import Contact

@dataclass
class ContactBook:
    _contacts: list[Contact] = field(default_factory=list)
                     
    def add_contact(self, contact: Contact) -> bool:
        for existing_contact in self._contacts:
            if existing_contact.email == contact.email:
                return False
        self._contacts.append(contact)
        return True
        
    def remove_contact(self, email) -> bool:
        for contact in self._contacts:
            if contact.email == email:
                self._contacts.remove(contact)
                return True
        return False
    
    def search_contacts(self, query: str) -> dict | None:
        query_lower = query.lower()

        for contact in self._contacts:
            if query_lower in contact.name.lower() or query_lower in contact.email.lower():
                print(f"🎯 Match found for '{query}'!")
                return contact.to_dict()
        print(f"❌ No contact found matching '{query}'.")
        return None
    
    def list_all_contacts(self) -> list:
        return self._contacts.copy()
    
    def update_existing_contact(self, id_email, **kwargs) -> bool:
        if "email" in kwargs:
            return False
        for contact in self._contacts:
            if contact.email == id_email:
                contact.update_fields(**kwargs)
                return True
        return False
