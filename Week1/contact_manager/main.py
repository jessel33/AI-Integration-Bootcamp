# This is just a placeholder awaiting the start of Bootcamp.

from contact import Contact
from contact_book import ContactBook
from file_storage import FileStorage

contacts_address = {
    "street": "123 Main St.",
    "city": "City X",
    "state": "Paranoia",
    "zip_code": "336699",
    "country": "USA",
}

book1 = ContactBook()

billy_bob = Contact("Billy Bob", "billyBob@gmail.com", 8149991234, contacts_address, "This is a note. Do you like this note? I created this note. It is MY note!")
book1.add_contact(billy_bob)

c1 = Contact("Alice", "alice@example.com", 9998887777, contacts_address, "I am really tired of not knowing enough information.")
book1.add_contact(c1)

c2 = Contact("Bob", "bob@example.com", 1234567890, contacts_address, "Hello from #c2")
book1.add_contact(c2)

def test_search_and_filter():
# 2. Test the filtering directly on a single contact object
    print("\n[Test 1] Testing single contact filtered dictionary output:")
    print(c1.to_dict())

    # 3. Test successful search execution 
    print("\n[Test 2] Testing successful book search (by name):")
    search_result = book1.search_contacts("Alice")
    print(f"Returned Data: {search_result}")

    # 4. Test searching by a different field (email)
    print("\n[Test 3] Testing book search (by email sub-string):")
    search_result_email = book1.search_contacts("example.com")
    print(f"Returned Data: {search_result_email}")

    # 5. Test search with no matches
    print("\n[Test 4] Testing failed book search:")
    failed_result = book1.search_contacts("Zelda")
    print(f"Returned Data: {failed_result}")

if __name__ == "__main__":
    test_search_and_filter()

def run_verification():
    print("--- 🔍 STARTING DATACLASS INTEGRATION TEST 🔍 ---")

    # ==========================================
    # STEP 1: Verify Dataclass Print & Creation
    # ==========================================

    contact_found = book1.search_contacts("alice@example.com")
    print(f"33 Found: {contact_found}")

    book1.update_existing_contact("alice@example.com", name="Alice May")
    print(book1)

    all_contacts = book1.list_all_contacts()
    print(f"List of all Contacts: {all_contacts}")

    # This will print the whole book object and the nested array of contacts
    print(f"Current Book State:\n{book1}")

    # ==========================================
    # STEP 3: Verify Storage Serialization (Save)
    # ==========================================
    print("\n[Step 3] Saving to disk via FileStorage...")

    storage = FileStorage("my_data.json")
    storage.save_contacts(book1)


    json_contacts = storage.save_contacts(book1)
    print(json_contacts)

    # ==========================================
    # STEP 4: Verify Storage Deserialization (Load)
    # ==========================================
    print("\n[Step 4] Reading back into a brand new object instance...")
    fresh_book = storage.load_contacts()

    print(f"Reconstructed Book State:\n{fresh_book}")
        
    # Final check: Make sure they are real objects, not raw strings or dicts
    if fresh_book._contacts:
        test_obj = fresh_book._contacts[0]
        print(f"\n✅ Success! Verification object type: {type(test_obj)}")
        print(f"✅ Extracted property test: {test_obj.name} -> {test_obj.email}")

    print("\n--- 🎉 ALL DATACLASSES SOURCED AND VERIFIED SUCCESSFULLY 🎉 ---")

if __name__ == "__main__":
    run_verification()
