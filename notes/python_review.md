# Python Review
## Date:  June 22, 2026
## Return Statements and Loops

1. What does return do inside a function?
   - My Answer: The return statement exits a function immediately, sending a specific value back and returns control to the code that called it.
     
   - ChatGPT: Correct - Tighter Version:  return immediately ends the function and sends a value back to the caller.

2. What happens when return is inside a for loop?
    - My Answer: It will stop the for loop once the return statement is reached and any iteration of the for loop that should have executed, will not occur.
  
    - ChatGPT: Correct - Also: A return inside a loop does not just stop the loop.  It stops the entire function.

3. What happens when return is after a for loop?
    - My Answer: It will execute the return statements code(see #1) after the for loop has executed the number of iteration it was intended to execute.
  
    - ChatGPT: Correct - Refinement: If return is after the loop, Python lets the loop finish first.  Then the function returns a value after all iterations are complete.

4. What is the difference between printing a value and returning a value?
    - My Answer: Printing a value, is for humans, it displays a text representation of data to the screen.  Returning a value, is intended for the computer, it returns data to the calling function that the computer or programs logic uses.
  
    - ChatGPT: Excellent - Also: print shows information.  Return gives information back to the program.

5. Why does returning too early cause bugs?
    - My Answer: Because not all of the code that the program requires for proper operation has been performed and therefore this early return will cause the program not to operate as desired.
  
    - ChatGPT: Correct - Returning too early causes bugs because the function exits before it has completed the full decision-making process.

ChatGPT Grades:
   - Conceptual understanding: Approved
   - Wording clarity: Good
   - Ready for practice exercises: Yes

## Return Placement Practice
- You have a list of email addresses.
- You want to check whether "bob@example.com" exists.
- Where should return True go?
  The 'return True' statement should go within the for loop and be executed when the if statement has returned true for a match of an email in the list with "bob@example.com".
  
  Why?
  Because once a match has been found by the if statement, there is no need to iterate through the rest of the list, this would just add to the program's runtime.

- Where should return False go?
    The 'return False' statement should go after the for loop structure, where it has iterated through all the item in the list since the nested if statement has never returned true for a match of an email in the list with "bob@example.com".

    Why?
        Because the for statement/structure needs to iterate through the entire list of items, if no match is being found by the if statement. Otherwise the search process is not complete and it can not be determined if the email already exists in the list of emails.


### Exercise 1: Search a list
Goal: Find whether a value exists in a list.

### Exercise 2: Count matches
Goal: Count how many values match a condition.

### Exercise 3: Validate all items
Goal: Check whether every item passes a rule.


### My current understanding
See Answers to question above.

### Examples that confuse me
None at this moment.

### Rules I need to remember

When searching a list:
- Return success inside the loop when the item is found.
- Return failure after the loop, once every item has been checked.
Do not return failure inside the loop unless one failed item is enough to end the whole function. 


## Current Progress 2026-06-29

You've already completed and demonstrated a solid understanding of:

* ✅ What `return` does
* ✅ `return` inside a loop
* ✅ `return` after a loop
* ✅ Difference between `print` and `return`
* ✅ Why returning too early causes bugs
* ✅ Correct placement of `return True` and `return False` in a search loop

This gives us a solid base to continue from.

---

## Next Lesson

When you resume, we'll begin with the next conceptual exercise:

**Count Matches**

> You have a list of customer names.
>
> You want to count how many names start with `"A"`.

We'll determine where the `return` statement belongs and why, then reinforce the concept with a few beginner-friendly examples before moving on to the next Python topic.


## Date: 2026-07-14
## Counting Matches

```Python
customer_names = [
    "Alice",
    "Bob",
    "Amanda",
    "Aaron",
    "Charlie",
]
```
Suppose return count were placed inside the for loop, like this:
```Python
def count_names_starting_with_a(names):
    count = 0

    for name in names:
        if name starts with "A":
            count increases

        return count
```
Using the original list, answer these two questions in your own words:
1. How many customer names would the loop examine before the function returned?
    It would only examine the 1st name in the list.

2. Why would placing return count inside the loop produce an incorrect result?
    Since the return is inside the for loop and will be executed at the end of the 1st iteration, this would not return the desired result.

Next Step: Build the Count Pattern
Fill in the blanks:
```Python
def count_names_starting_with_a(names):
    count = ___

    for name in names:
        if name.startswith(___):
            count ___

    return ___
```
Explain each answer:
What should count initially equal, and why?
  It should be initialized to zero as the count of matches starts with zero matches.

What argument should be passed to startswith()?
 The string letter A, as in 'A'.

How should the counter be increased?
  It should be increased by 1 each time a match is found.

What value should the function return?
    The function should return the final value of count, as that will be the total number of names starting with the letter 'A'.


## ChatGPT's responses for 
## Aug.1 - 2, 2026

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

You are **very close**. For tonight, note only these four fixes:

1. **Update bug:**
   This passes the literal field name `"info_name_to_update"`:

```python
info_name_to_update=info_value_to_update
```

Build a dictionary using the user’s input as the key, then unpack it with `**`.

2. **Delete option:** still needs to ask for a contact name and call `delete_contact()`.

3. **Invalid message:** change “1 through 6” to **“1 through 7.”**

4. **Loading:** the program currently creates an empty book every time. Eventually, load the saved contact book when the program starts.

Your add, search, save, print-all, ID assignment, and overall menu loop are structured correctly. Excellent progress today—get some rest.


