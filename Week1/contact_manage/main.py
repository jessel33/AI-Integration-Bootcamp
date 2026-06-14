# This is just a placeholder awaiting the start of Bootcamp.
from contact import Contact
from contact_book import ContactBook

contacts_address = {
    "street": "123 Main St.",
    "city": "City X",
    "state": "Paranoia",
    "zip_code": "336699",
    "country": "USA",
}

billy_bob = Contact("Billy Bob", "billyBob@gmail.com", 8149991234, contacts_address, "This is a note. Do you like this note? I created this note. It is MY note!")
c1 = Contact("Alice", "alice@example.com", 9998887777, contacts_address, "I am really tired of not knowing enough information.")
c2 = Contact("Bob", "bob@example.com", 1234567890, contacts_address, "Hello from #c2")

manager = ContactBook()
existing_contacts_list = [billy_bob, c1]

manager.load_contacts(existing_contacts_list)
manager.add_contact(c2)

contact_found = manager.find_by_email("alice@example.com")
print(contact_found)
#manager.list_all_contacts()
manager.update_existing_contact("alice@example.com", email="billyBob@gmail.com")
print(f"{c1.get_info()}")

all_contacts = manager.list_all_contacts()
print(all_contacts)
