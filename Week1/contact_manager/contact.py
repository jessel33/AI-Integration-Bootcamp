# Contact Class for Contact Management System
from address import Address

class Contact(Address):
    def __init__(self, internal_ID, contact_name, email, phone, preferred_contact_method):
        self.internal_ID = internal_ID
        self.contact_name = contact_name
        self.email = email
        self.phone = phone
        self.preferred_contact_method = preferred_contact_method

    def __str__(self):
        return f"Internal ID: {self.internal_ID}\nName: {self.contact_name}\nEmail: {self.email}\nPhone: {self.phone}\nPreferred Contact Method: {self.preferred_contact_method}"

    def get_info(self):
            return f"Internal ID: {self.internal_ID}\nName: {self.contact_name}\nEmail: {self.email}\nPhone: {self.phone}\nPreferred Contact Method: {self.preferred_contact_method}"


    def update_fields(self, **kwargs):
            allowed_fields = ["contact_name", "email", "phone", "address", "preferred_contact_method"]
            for key, value in kwargs.items():
                if key in allowed_fields:
                    setattr(self, key, value)

                else:
                    raise AttributeError(f"'{type(self).__name__}' object either has no attribute '{key}' or that attribute in not modifiable")
                
            return True
    