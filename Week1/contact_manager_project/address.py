# address.py
# Address Class
# For Project: 
# Contact Management System
# This file will:
# Save a Contact's Address
# Focus of this project:
# Code organization
# Classes
# Error handling

class Address:
    def __init__(self, address_line_1, address_line_2, locality, administrative_area, postal_code, country):
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.locality = locality
        self.administrative_area = administrative_area
        self.postal_code = postal_code
        self.country = country

    def __str__(self):
        return f"Address line 1: {self.address_line_1}\nAddress line 2: {self.address_line_2}\nLocality: {self.locality}\nAdministrative Area: {self.administrative_area}\nPostal Code: {self.postal_code}\nCountry: {self.country}"

    def get_info(self):
        return str(self)

    def to_dict(self):
        address_dict = {}
        address_dict.update(self.__dict__)
        return address_dict

