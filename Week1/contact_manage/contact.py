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

    def get_info(self):
        return f"Name: {self.name} Email: {self.email} Phone: {self.phone} Address: {self.address} Notes: {self.notes}"
    
