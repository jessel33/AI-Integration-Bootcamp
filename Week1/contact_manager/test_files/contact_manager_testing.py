

billy_bob = Contact(name="Billy Bob", email="billyBob@gmail.com", phone=8149991234, address=contacts_address, notes="This is a note. Do you like this note? I created this note. It is MY note!")
c1 = Contact(name="Alice", email="alice@example.com", phone=9998887777, address=contacts_address, notes="I am really tired of not knowing enough information.")
c2 = Contact(name="Jimmy", email="jimmy@gmail.com", phone=8149991234, address=contacts_address, notes="Hello from #c2")

raw_json_string = """{billy_bob, c1, c2}"""
contact_object = (billy_bob, c1, c2)
jesses_contacts = ContactBook(owner="Jesse Armstrong", contacts=contact_object)
'''raw_json_string = """
{
    "_contacts": 
    "name": "Jimmy C Jumper",
    "email": "jimmycjumper@icloud.com",
    "phone": "8885551212"
    "address": {
        "street": "335 State St.",
        "city": "Blairville",
        "state": "WV",
        "zip_code": "100001",
        "country": "USA",
    }
    "notes": "Test note, test notes!"
}
"""'''







save_contacts = ContactBook.model_validate_json(raw_json_string) 

print(jesses_contacts)

load_contacts = save_contacts.model_dump_json(indent=4)

with open("contact_data.json", "w") as file:
    file.write(load_contacts)