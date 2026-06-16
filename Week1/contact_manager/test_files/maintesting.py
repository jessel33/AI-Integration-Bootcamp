import os
from contact import Contact
from contact_book import ContactBook
from file_storage import FileStorage

def test_file_storage_pipeline():
    print("\n--- 💾 TESTING FILE STORAGE PIPELINE 💾 ---")
    
    # 1. Setup sample data environment
    test_filename = "contacts_test_output.json"
    storage = FileStorage(file_path=test_filename)
    
    original_book = ContactBook()
    
    # Create test contacts using your custom dataclass fields
    c1 = Contact("Diana Prince", "diana@justice.org", 5551111, address={"city": "Oil City"}, notes="Amazonian")
    c2 = Contact("Bruce Wayne", "bruce@gotham.com", 5552222, address={"street": "Wayne Manor"})
    
    original_book.add_contact(c1)
    original_book.add_contact(c2)

    # 2. Test Saving Data
    print("\n[Storage Step 1] Saving contacts book to JSON file...")
    storage.save_contacts(original_book)
    print("✅ File successfully written.")
    
    # 3. Print the written file to visually verify allowable keys
    print("\n[Storage Step 2] Reading raw file text from disk (Verifying Filtered Keys):")
    if os.path.exists(test_filename):
        with open(test_filename, "r") as f:
            print(f.read())
    else:
        print("❌ Error: JSON file was never created!")

    # 4. Test Loading Data back into a separate object
    print("\n[Storage Step 3] Loading JSON data back into a fresh ContactsBook instance...")
    loaded_book = storage.load_contacts()
    print("✅ Load method completed.")
    
    # 5. Verify the data inside the re-hydrated dataclass object
    print("\n[Storage Step 4] Verifying the contents of the reloaded object:")
    print(f"Total contacts found: {len(loaded_book._contacts)}")
    
    for saved_contact in loaded_book._contacts:
        print(f"• Found Contact Dataclass Instance: {saved_contact}")
        print(f"  ↳ Internal Verification -> Name: {saved_contact.name} | Phone: {saved_contact.phone}")
        
    # Clean up the test file afterwards (optional)
    if os.path.exists(test_filename):
        os.remove(test_filename)
        print("\n🗑️ Temporary test file cleaned up from directory.")

    print("\n--- 🎉 FILE STORAGE TESTING COMPLETE 🎉 ---")

if __name__ == "__main__":
    # Run the storage verification test
    test_file_storage_pipeline()
