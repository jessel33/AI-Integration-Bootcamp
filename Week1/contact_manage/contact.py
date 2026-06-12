# Contact.py file
# Create a Contact class that can:
# - store name, email, phone, address, and notes
# - update its own fields
# - return a readable string version
# - convert itself to a dictionary

class Contact:
    def __init__(self, name, email, phone, address, notes):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.notes = notes

    def to_dict(self):
        keys_to_include = ["name", "email", "phone", "address", "notes"]
        return {key: getattr(self, key) for key in keys_to_include}

    def get_info(self):
        return f"Name: {self.name}\nEmail: {self.email}\nPhone: {self.phone}\nAddress: {str(self.address)}\nNotes: {self.notes}"
    
    def update_fields(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise AttributeError(f"'{type(self).__name__}' object has no attribute '{key}'")

