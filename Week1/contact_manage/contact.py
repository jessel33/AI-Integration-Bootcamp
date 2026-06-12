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
        return vars(self)       

    def get_info(self):
        return f"Name: {self.name} Email: {self.email} Phone: {self.phone} Address: {self.address} Notes: {self.notes}"
    
    def update_fields(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise AttributeError(f"'{type(self).__name__}' object has no attribute '{key}'")


contacts_address = {
    "Street": "123 Main St.",
    "City": "City X",
    "State": "Paranoia",
    "Zip Code": "336699",
    "Country": "USA",
}
Billy_Bob = Contact("Billy Bob", "billyBob@gmail.com", 8149991234, contacts_address, "This is a note. Do you like this note? I created this note. It is MY note!")

print(Billy_Bob.get_info())
print(Billy_Bob.to_dict())
Billy_Bob.update_fields(name = "Billy Jo Bob")
print(Billy_Bob.get_info())

