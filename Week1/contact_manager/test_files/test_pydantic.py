from file_storage import Contact, ContactBook

# --- STEP 1: Create a ContactBook and add nested data ---
my_book = ContactBook(owner="Alice")

# Add contact 1
my_book.contacts.append(Contact(
    name="Bob Smith",
    phone=5550199,
    email="bob@example.com",
    address = {
        "street": "335 State St.",
        "city": "Blairville",
        "state": "WV",
        "zip_code": "100001",
        "country": "USA",
        },
    notes="Note 1!"
))

# Add contact 2
my_book.contacts.append(Contact(
    name="Charlie Brown",
    phone=5550234,
    email="charlie@example.com",
    address = {
        "street": "335 State St.",
        "city": "Blairville",
        "state": "WV",
        "zip_code": "100001",
        "country": "USA",
        },
    notes="Note 2?"
))

# --- STEP 2: Execute Use Case 'save_contacts' ---

FILE_NAME = "my_contacts.json"
my_book.save_contacts(FILE_NAME)


# --- STEP 3: Execute Use Case 'load_contacts' ---
# Reconstruct a completely brand new object instance from the physical file

loaded_book = ContactBook.load_contacts(FILE_NAME)


# --- STEP 4: Interact with the loaded objects via dot-notation ---

print(f"\n--- Contact Book Owner: {loaded_book.owner} ---")
for person in loaded_book.contacts:
    print(f"Name: {person.name}")
    print(f"Email: {person.email}")

    # Access the nested dictionary safely

    print(f"City: {person.address.get('city')}")
    print("-" * 20)