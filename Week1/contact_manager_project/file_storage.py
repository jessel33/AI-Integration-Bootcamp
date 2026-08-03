# data_storage.py
# For Project: 
# Contact Management System
# This file will:
# * Save/load data
# Focus of Project:
# Code organization
# Classes
# Error handling
# design 2 methods as follows:
# def save_contacts() - receives a list of Contact objects
# def load_contacts() - returns a list of Contact objects

import json
from address import Address
from contact import Contact
from contact_book import ContactBook

class FileStorage:
    def __init__(self, contact_book, data_file_path):
        self.contact_book = contact_book
        self.data_file_path = data_file_path # path and filename

    def __str__(self):
        if not self.contact_book:
            return "No current contact book"
        else:
            return f"Contact Book: {self.contact_book}\nData file-path: {self.data_file_path}\n"

    def save_contacts(self):
        with open(self.data_file_path, "w") as wfile:
            json.dump(self.contact_book.list_of_contact_dict(), wfile)


    def load_contacts(self):
        contact_book = ContactBook()
        try:
            with open(self.data_file_path, "r") as rfile:
                raw_data = json.load(rfile)

            for data in raw_data:
                address = Address(**data["address"])
                data["address"] = address
                contact = Contact(**data)
                contact_book.add_contact_to_contact_book(contact)

            return contact_book
        
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
        
