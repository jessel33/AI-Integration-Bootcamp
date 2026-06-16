# File Storage Program Notes

## How to make Python class objects interact with JSON files.

- Requires translating Python objects into dictionary primitives (serialization) and converting them back into class instances (deserialization).

## Serializing a Class Object to a JSON File.
- To save a class instance to a JSON file, you can access the object's local attributes using its built-in __dict__ dictionary wrapper and save it using json.dump().
  
``` python
import json

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

# Instantiate the custom class
user_obj = User("Alice", "Admin")

# Open file and write the object's dictionary format
with open("user_data.json", "w") as json_file:
    json.dump(user_obj.__dict__, json_file, indent=4)
```

## Deserializing a JSON File into a Class Object.
- To reconstruct your class object from a saved JSON file, read the data into a native dictionary using json.load() and pass it to your constructor using the ** dictionary unpacking operator.

``` python
import json

# Read the file and unpack the keys directly into the class constructor
with open("user_data.json", "r") as json_file:
    raw_data = json.load(json_file)
    
new_user = User(**raw_data)

print(new_user.name)  # Output: Alice
print(new_user.role)  # Output: Admin
```

## Handling Complex or Nested Custom Objects
- If your class contains nested custom objects or data types that JSON cannot read directly (like datetime), the standard __dict__ approach will fail. You can handle this natively by adding dedicated serialization methods or by implementing a custom encoder class.

``` python
import json

class Department:
    def __init__(self, dept_name, manager_obj):
        self.dept_name = dept_name
        self.manager = manager_obj  # This is a nested User class object

    def to_json_dict(self):
        # Recursively converts nested class properties into valid JSON types
        return {
            "dept_name": self.dept_name,
            "manager": self.manager.__dict__ 
        }

# Setup and execution
manager = User("Bob", "Manager")
dept = Department("Engineering", manager)

with open("dept_data.json", "w") as json_file:
    json.dump(dept.to_json_dict(), json_file, indent=4)
```

## Modern Alternative: Using Pydantic
- For robust real-world production projects, using the standard Python JSON documentation strategies can become verbose. Most developers rely on Pydantic because it performs automatic data type validation, smoothly handles nested structures, and provides built-in .model_dump_json() and .model_validate_json() utilities.

- Using Pydantic makes handling nested dictionaries and custom class structures straightforward because it enforces data validation and handles serialization out of the box.
## Why Pydantic Excels at Nested Data
- In standard Python, extracting nested dictionaries requires manual loops or factory methods. With Pydantic, you define your schema using Type Hints. Pydantic automatically parses the nested dictionaries into distinct, fully validated Python sub-objects.

## Complete Pydantic Implementation
- Here is how you define, parse, and save a class instance that contains a nested dictionary structure using Pydantic v2:
  
``` python
import json
from pydantic import BaseModel, Field

# 1. Define the child structure (the nested object)
class TechnicalSpecs(BaseModel):
    storage_gb: int
    ram_gb: int
    processor: str

# 2. Define the parent structure (the main class)
class Product(BaseModel):
    product_id: int
    name: str
    # Type hinting this as TechnicalSpecs tells Pydantic to parse the dictionary automatically
    specs: TechnicalSpecs 

# --- USE CASE 1: Deserializing (Loading JSON data into our objects) ---

# Mock data simulating what you read from a .json file
raw_json_string = """
{
    "product_id": 101,
    "name": "Developer Laptop",
    "specs": {
        "storage_gb": 512,
        "ram_gb": 16,
        "processor": "M3 Pro"
    }
}
"""

# Load directly from the raw JSON string
laptop_item = Product.model_validate_json(raw_json_string)

# You can now access nested fields with clean dot-notation instead of bracket strings
print(laptop_item.name)           # Output: Developer Laptop
print(laptop_item.specs.ram_gb)   # Output: 16


# --- USE CASE 2: Serializing (Exporting back to a JSON File) ---

# Modify an attribute to show it changes
laptop_item.specs.ram_gb = 32

# Export the object straight to a formatted JSON string
updated_json_data = laptop_item.model_dump_json(indent=4)

with open("product_data.json", "w") as file:
    file.write(updated_json_data)
```

## Core Features You Gain
- Type Safety: If a user passes "sixteen" instead of 16 for ram_gb, Pydantic will throw a clear validation error immediately instead of letting bad data corrupt your file.
  
- Auto-Conversion: If a JSON field is a string like "512" but your model defines it as an int, Pydantic safely converts it automatically.
  
- Dot Notation: You no longer need to write messy dictionary lookups like data["specs"]["ram_gb"]. Instead, you use data.specs.ram_gb


