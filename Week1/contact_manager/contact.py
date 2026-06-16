# contact.py file
# Create a Contact class that can:
# - store name, email, phone, address, and notes
# - update its own fields
# - return a readable string version
# - convert itself to a dictionary

from dataclasses import dataclass, field

@dataclass
class Contact:
    name: str
    email: str
    phone: int
    address: dict
    notes: str = ""

    def to_dict(self) -> dict:
        keys_to_include = ["name", "email", "phone", "address", "notes"]
        return {key: getattr(self, key) for key in keys_to_include if hasattr(self, key)}

    def get_info(self) -> str:
        return f"Name: {self.name}\nEmail: {self.email}\nPhone: {self.phone}\nAddress: {str(self.address)}\nNotes: {self.notes}"
    
    def update_fields(self, **kwargs) -> bool | None:
        allowed_fields = ["name", "email", "phone", "address", "notes"]
        for key, value in kwargs.items():
            if key in allowed_fields:
                setattr(self, key, value)
                return True
            else:
                raise AttributeError(f"'{type(self).__name__}' object either has no attribute '{key}' or that attribute in not modifiable")
                return False
            