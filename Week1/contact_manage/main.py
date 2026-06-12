# This is just a placeholder awaiting the start of Bootcamp.
import contact

contacts_address = {
    "street": "123 Main St.",
    "city": "City X",
    "state": "Paranoia",
    "zip_code": "336699",
    "country": "USA",
}

billy_bob = contact.Contact("Billy Bob", "billyBob@gmail.com", 8149991234, contacts_address, "This is a note. Do you like this note? I created this note. It is MY note!")

print(billy_bob.get_info())
print(billy_bob.to_dict())
billy_bob.update_fields(name = "Billy Jo Bob")
print(billy_bob.get_info())
