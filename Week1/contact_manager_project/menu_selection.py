# menu_selection.py
#
# For Project: 
# Contact Management System
# This file will:
# Take input from user
# and preform the operation requested
# by user from their input.
# Focus of this Project:
# Code organization
# Classes
# Error handling

"""Best flow
Create one ContactBook when the program starts.
Show a menu such as:
Add contact
Search contacts
Update contact
Delete contact
Exit

When the user chooses Add contact:
Gather the information
Create the Address
Create the Contact
Pass the completed contact to ContactBook.add_contact()"""

from address import Address
from contact import Contact
from contact_book import ContactBook
from file_storage import FileStorage

contact_book = ContactBook()
contact_storage = FileStorage(contact_book, "Week1/contact_manager_project/contact_data.json")
contact_book = contact_storage.load_contacts()
if not contact_book:    
    contact_book = ContactBook()
    print("New contact book was created.")

else:
    print("Loaded the existing contact book")
      
while True:
    print("\n*Contact Management System Menu*")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Save Contacts")
    print("6. Print all contacts in current contact book")
    print("7. Exit")

    operation_number = input("\nPlease enter the number for the operation you wish to perform: ")

    if operation_number == "1":
        print("-Please enter the following information-")
        contact_name = input("Contact's name(required): ")
        address_line_1 = input("Address line 1(required): ")
        address_line_2 = input("Address line 2: ")
        locality = input("Locality(required): ")
        administrative_area = input("Administrative Area: ")
        postal_code = input("Postal Code: ")
        country = input("Country(required): ")
        email = input("Contact's Email(email or phone required, both preferred): ")
        phone = input("Contact's Phone(email or phone required, both preferred): ")
        preferred_contact_method = input("Contact's Preferred Contact Method(phone or email): ")

        print("Adding Contact")
        new_contact_address = Address(address_line_1, address_line_2, locality, administrative_area, postal_code, country)
        new_contact = Contact(contact_book.get_next_id(), contact_name, new_contact_address, email, phone, preferred_contact_method)
        contact_added = contact_book.add_contact_to_contact_book(new_contact)
        if contact_added:
            print(new_contact)
            add_contact_store = FileStorage(contact_book, "Week1/contact_manager_project/contact_data.json")
            add_contact_store.save_contacts()
            print("\nContact created, add to contact book, and updated contact book saved.\n")

        else:
            print("Contact Book found a Duplicate Contact of the same name.")

    elif operation_number == "2":
        search_contact = input("Enter the name of the contact to search for: ")
        print("\nSearching for Contact\n")
        print(contact_book.search_contacts(search_contact))
        
    elif operation_number == "3":
        contact_to_update = input("Enter the name of the contact you want to Update: ")
        info_name_to_update = input("Enter the name of the information you want to Update: ")
        info_value_to_update = input("Enter the new value of the information you want to Update: ")

        update_dictionary = {info_name_to_update.strip().lower(): info_value_to_update}
        print("\nUpdating Contact")

        contact_updated = contact_book.update_contact(contact_to_update, **update_dictionary)

        if contact_updated:
            print(f"Contact Updated\n")

            if info_name_to_update == "contact_name":
                print(contact_book.search_contacts(info_value_to_update))
            else:
                print(contact_book.search_contacts(contact_to_update))

            upd_contact_store = FileStorage(contact_book, "Week1/contact_manager_project/contact_data.json")
            upd_contact_store.save_contacts()
            print("Updated contact book saved.\n")

        elif contact_updated is None:
            print(f"The contact book does not contain a contact by that name: {contact_to_update}.\nPlease confirm your information and retry.")

        else:
            print("You entered an invalid field name.\nPlease confirm your information and retry")

    elif operation_number == "4":
        target_name = input("Enter the name of the contact you want to delete: ")
        confirm_delete = input(f"You want to delete contact {target_name}, (y) or (n): ")
        if confirm_delete.strip().lower() == 'y':
            print("\nDeleting Contact")
            contact_deleted = contact_book.delete_contact(target_name)
            if contact_deleted:
                print(f"Contact {target_name} was deleted.")
                del_contact_store = FileStorage(contact_book, "Week1/contact_manager_project/contact_data.json")
                del_contact_store.save_contacts()
                print("Updated contact book saved.\n")

            else:
                print(f"The contact you specified {target_name} was not found.")

        elif confirm_delete.strip().lower() == 'n':
            print("\nContact deletion was aborted.")

        else:
            print(f"\nYour entry {confirm_delete} was not valid, please retry.")

    elif operation_number == "5":
        contact_storage = FileStorage(contact_book, "Week1/contact_manager_project/contact_data.json")
        print("\nSaving Contacts")
        contact_storage.save_contacts()
        print("Save Complete")

    elif operation_number == "6":
        print(contact_book.get_info())

    elif operation_number == "7":
        break

    else:
        print("\nInvalid selection. Please enter a number from 1 through 7.")            
