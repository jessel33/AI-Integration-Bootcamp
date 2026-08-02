# Projects

## Week 1 Project:
Contact Management System
Build:
* Create contact
* Update contact
* Delete contact
* Search contact
* Save/load data
Focus:
Code organization
Classes
Error handling

## Important information...

What do I have wrong here, hint please:
from contact_book.py ContactBook class:

The error means **`contact_name` is actually a `Contact` object**, not a string.

You likely have something similar to:

```python
for contact_name in self.contacts:
```

Inside that loop, access the object’s name attribute before using string methods:

```python
contact.contact_name.strip().lower()
```

So rename the loop variable from `contact_name` to `contact`, then compare:

```python
contact.contact_name
```

**Reason:** `.strip()` belongs to strings. Your `Contact` object contains the string in its `contact_name` attribute.


```Python
def update_contact_name(self, target_name, new_name):
        found_match = False
        for index, target_name in enumerate(self.contacts):
            if new_name.contact_name.strip().lower() == target_name.strip().lower():
                self.contacts[index] = new_name
                found_match = True
        
        return found_match
```

You have **three variable-role mixups**:

    1. `for index, target_name in enumerate(self.contacts)`
    Here, `target_name` becomes a **Contact object**, replacing the original search-name parameter.

    2. `new_name.contact_name`
    `new_name` is probably a **string**, so it should not have `.contact_name`.

    3. `self.contacts[index] = new_name`
    This replaces the entire `Contact` object with a string.

### Hint

Use a loop variable named `contact`, then think:

```python
contact.contact_name   # existing name
target_name            # name to search for
new_name               # replacement string
```

When matched, update the attribute on the existing object rather than replacing the whole object:

```python
contact.contact_name = new_name
```


Fixed the last two errors we talked about:

```Python
class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact_to_contact_book(self, new_names):
        for x in self.contacts:
            if x.strip().lower() == new_names.strip().lower():
                return False

        self.contacts.append(new_names)
        return True

    def update_contact_name(self, target_name, new_name):
        found_match = False
        for contact in self.contacts:
            if contact.contact_name.strip().lower() == target_name.strip().lower():
                contact.contact_name = new_name
                found_match = True
        
        return found_match

    def search_contacts(self, target_name):
        for contact in self.contacts:
            if contact.contact_name.strip().lower() == target_name.strip().lower():
                return contact
            
        return None
```

Nice work — your **update** and **search** methods now use the `Contact` object correctly.

One small heads-up before you move on: in `add_contact_to_contact_book()`, `x` will also be a `Contact` object, so `x.strip()` will cause the same error later. You’ll need to compare one of its string attributes, such as `x.contact_name` or `x.email`.

For delete, use the same pattern you just learned:

**loop through contacts → find the match → remove that Contact object → return success/failure**.


