# Pydantic Contact Book Implementation

- To manage a collection of items like a contact book, you define a parent ContactBook model that contains a list of your child Contact models.
  
``` python
from pathlib import Path
from pydantic import BaseModel, Field


# 1. Define the child object structure

class Contact(BaseModel):
    name: str
    phone: str
    email: str

    # A nested dictionary for flexible custom data (e.g., {"tags": ["work"], "notes": "boss"})

    meta_data: dict[str, str | list[str]] = Field(default_factory=dict)


# 2. Define the parent manager object structure

class ContactBook(BaseModel):
    owner: str

    # Typing this as a list of Contact objects tells Pydantic to auto-convert nested JSON arrays

    contacts: list[Contact] = Field(default_factory=list)

    # --- USE CASE 1: Save Contact Book to JSON ---

    def save_contacts(self, file_path: str | Path) -> None:

        """Serializes the entire object structure and saves it to a JSON file."""

        # model_dump_json() handles the nested dictionaries and lists natively
        
        json_data = self.model_dump_json(indent=4)
        Path(file_path).write_text(json_data, encoding="utf-8")
        print(f" Successfully saved contact book to {file_path}")


    # --- USE CASE 2: Load Contact Book from JSON ---

    @classmethod
    def load_contacts(cls, file_path: str | Path) -> "ContactBook":
        """Reads a JSON file and deserializes it back into a validated ContactBook instance."""
        path = Path(file_path)
        if not path.exists():

            # Return an empty contact book if the file doesn't exist yet

            print(f" File {file_path} not found. Creating a blank contact book.")
            return cls(owner="Unknown")
            
        json_string = path.read_text(encoding="utf-8")


        # model_validate_json automatically converts raw strings into structured Python objects

        return cls.model_validate_json(json_string)
```

## How to Use the Code (Execution Walkthrough)

- Here is how you initialize the data, execute your two required use cases, and interact with the resulting Python objects.
  
``` python
# --- STEP 1: Create a ContactBook and add nested data ---
my_book = ContactBook(owner="Alice")

# Add contact 1
my_book.contacts.append(Contact(
    name="Bob Smith",
    phone="555-0199",
    email="bob@example.com",
    meta_data={"relationship": "manager", "tags": ["work", "urgent"]}
))

# Add contact 2
my_book.contacts.append(Contact(
    name="Charlie Brown",
    phone="555-0234",
    email="charlie@example.com",
    meta_data={"relationship": "friend"}
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

    print(f"Role: {person.meta_data.get('relationship')}")
    print("-" * 20)
```

## The Resulting my_contacts.json File

- Pydantic outputs a standard, clean JSON string behind the scenes that accurately maintains your array structures and nested dictionaries:
  
``` json
{
    "owner": "Alice",
    "contacts": [
        {
            "name": "Bob Smith",
            "phone": "555-0199",
            "email": "bob@example.com",
            "meta_data": {
                "relationship": "manager",
                "tags": [
                    "work",
                    "urgent"
                ]
            }
        },
        {
            "name": "Charlie Brown",
            "phone": "555-0234",
            "email": "charlie@example.com",
            "meta_data": {
                "relationship": "friend"
            }
        }
    ]
}
```

