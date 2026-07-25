# file_storage.py
# FileStorage program should do all of the following:
# - Save contact data to a JSON file
# - Load contact data from a JSON file
# - Handle missing file errors
# - Handle invalid JSON errors
# - Convert loaded dictionaries back into Contact objects
# design 2 methods as follows:
# def save_contacts() - receives a list of Contact objects
# def load_contacts() - returns a list of Contact objects

import json
from Week1.contact_manager.oldfirstiterationfiles.contact_book import ContactBook
from Week1.contact_manager.oldfirstiterationfiles.contact import Contact

class FileStorage:
    def __init__(self):
        self._contacts = []
        self.file_path = "Week1/contact_manager/contacts.json"

    def save_contacts(self, book_object):
        serialized_contacts = [contact.to_dict() for contact in book_object.contacts]

        with open("Week1/contact_manager/contacts.json", "w") as f:
            json.dump(serialized_contacts, f, indent=4)
        return True

    def load_contacts(self, file_path):
        contact_book = ContactBook()

        try:
            with open(file_path, "r") as f:
                raw_data = json.load(f)
                       
            for data in raw_data:
                contact = Contact(**data)
                contact_book.add_contact(contact)

            return contact_book.list_all_contacts()
        
        except FileNotFoundError as e:
            print(f"The specified file could not be found: {e.strerror}")
            
            return False
        
        except json.JSONDecodeError as e:
            print(f"JSON parsing failed: {e.msg}")
            print(f"Error occurred at line {e.lineno}, column {e.colno}.")
            
            return False
        
        except TypeError as e:
            print(f"Type Error: The input provided was not a valid string or bytes object. Details: {e}")
            
            return False
