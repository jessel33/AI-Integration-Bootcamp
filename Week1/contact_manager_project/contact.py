# contact.py
# Contact Class
# For Project: 
# Contact Management System
# This file will:
# * Create contact
# * Update contact fields
# Focus of this Project:
# Code organization
# Classes
# Error handling

class Contact:
    def __init__(self, internal_id, contact_name, address, email, phone, preferred_contact_method):
        self.internal_id = internal_id
        self.contact_name = contact_name
        self.address = address
        self.email = email
        self.phone = phone
        self.preferred_contact_method = preferred_contact_method

    def __str__(self):
        return f"Internal ID: {self.internal_id}\nName: {self.contact_name}\n{self.address}\nEmail: {self.email}\nPhone: {self.phone}\nPreferred Contact Method: {self.preferred_contact_method}"

    def get_info(self):
            return str(self)
    
    def update_fields(self, **kwargs):
        allowed_contact_fields = ["contact_name", "email", "phone", "preferred_contact_method"]
        allowed_address_fields = ["address_line_1", "address_line_2", "locality", "administrative_area", "postal_code", "country"]
        for key, value in kwargs.items():
            if key in allowed_contact_fields:
                setattr(self, key, value)

            elif key in allowed_address_fields:
                setattr(self.address, key, value)

            else:
                return False
              
        return True

    # convert contact object into a dictionary
    def to_dict(self):
        return {
            'internal_id': self.internal_id,
            'contact_name': self.contact_name,
            'address': self.address.to_dict(),
            'email': self.email,
            'phone': self.phone,
            'preferred_contact_method': self.preferred_contact_method
        }

    