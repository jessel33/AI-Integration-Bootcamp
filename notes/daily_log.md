# June 22, 2026
## Current status:

- Repository organization: complete
- notes/ folder: confirmed on GitHub
- .venv: not committed
- __pycache__: not committed
- temporary files: not committed
- Contact Manager project: paused
- Bootcamp mode: Python review week

### What I studied
Organized the bootcamp repository and notes folder.

### What confused me
How to structure notes and how to pause the current project cleanly.

### What I practiced
Created markdown note files and prepared the repo for a reset.

### Questions for ChatGPT
How should I prepare before restarting the bootcamp?

### One thing I understand better now
The notes folder should live at the project root and track the whole learning journey.


## ChatGPT's responses for Aug.1 - 2, 2026

Small naming improvement:

```python
for contact in self.__contacts:
    contact_dict_list.append(contact.to_dict())
```

**Reason:** `contact` is clearer than `x`.

**Next action:** create `file_storage.py` and start the save function using:
```python
json.dump(contact_book.list_of_contact_dict(), file)
```


**Your `save_contacts()` is correct.**
```python
def save_contacts(self): with open(self.data_file_path, "w") as wfile:
    json.dump(self.contact_book.list_of_contact_dict(), wfile)
```

Excellent — that output confirms the full round trip is working:

**`Address` object → dictionary → JSON → dictionary → `Address` object**

Your loaded contacts are now real `Contact` objects containing real `Address` objects, not nested dictionaries.

**Next action:** test these two failure cases:

1. The JSON file does not exist.
2. The JSON file exists but contains invalid JSON.

After those pass, your save/load foundation is complete.


```python
def load_contacts(self):
    contact_book = ContactBook()
    try:
        with open(self.data_file_path, "r") as rfile:
            raw_data = json.load(rfile)

        for data in raw_data:
            address = Address(**data["address"])
            data["address"] = address
            contact = Contact(**data)
            contact_book.add_contact_to_contact_book(contact)

        return contact_book
    
    except FileNotFoundError as e:
        print(f"The specified file could not be found: {e.strerror}")
        
        return False
    
    except json.JSONDecodeError as e:
        print(f"JSON parsing failed: {e.msg}")
        print(f"Error occurred at line {e.lineno}, column {e.colno}.")
        
        return False
    
    except TypeError as e:
        print(f"Type Error: The input provided was not a valid string or bytes object. Details: {e}")
        
        return False
```

## Output from code testing of retrieving json file and converting data to Python objects.

Contact Book: 
- Internal ID: 1 
- Name: AMC Software LLC 
- Address line 1: 400 River Ave. Apt# 2F 
- Address line 2: PO BOX 112 
- Locality: Emlenton 
- Administrative Area: PA 
- Postal Code: 16373 
- Country: USA 
- Email: jesse.amcsoftware@icloud.com 
- Phone: 7244213733 
- Preferred Contact Method: Phone

- Internal ID: 2 
- Name: Billy Bob Boy 
- Address line 1: 400 River Ave. Apt# 2F 
- Address line 2: PO BOX 112 
- Locality: Emlenton 
- Administrative Area: PA 
- Postal Code: 16373 
- Country: USA 
- Email: jesse@armstrongsgarage.com 
- Phone: 7244213733 
- Preferred Contact Method: Phone

