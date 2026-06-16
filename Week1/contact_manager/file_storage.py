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
from contact_book import ContactBook
from contact import Contact
from dataclasses import dataclass, field

contacts_address = {
        "street": "335 State St.",
        "city": "Blairville",
        "state": "WV",
        "zip_code": "100001",
        "country": "USA",
}

@dataclass
class FileStorage:
    file_path: str

    def save_contacts(self, book: ContactBook) -> None:

        serialized_contacts = [c.to_dict() for c in book._contacts]

        with open(self.file_path, "w") as f:
            json.dump(serialized_contacts, f, indent=4)

    def load_contacts(self) -> ContactBook:
        try:
            with open(self.file_path, "r") as f:
                raw_data = json.load(f)
        
            contacts_object = [Contact(**data) for data in raw_data]
            return ContactBook(_contacts=contacts_object)
        
        except (FileNotFoundError, json.JSONDecodeError):
            return ContactBook()

