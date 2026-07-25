# Notes from July 24, 2026
## Restarted the 6 Week learning path today!

1.  What real-world thing should a Contact object represent?  

An entity that we want to store its contact information, for later retrieval and use.

2.  What information belongs to one individual contact?

Name, address, phone, email, preferred contact method.

3.  Which contact field should uniquely identify a person in this application?
Email

4.  What responsibilities should belong to an individual Contact?


Provide methods to access stored information.

5.  What responsibilities should not belong to Contact, because they involve managing several contacts?  

Adding contacts, editing contacts, removing contacts, etc.


## 2nd Set of Questions:

1.  Should every contact be required to have an address, or should it be optional?

I personally don't like address being optional.  If you won't provide your address I won't do business with you!

2.  Which address fields should be required?

| Field               | Requirement |
| ------------------- | ----------- |
| Address line 1      | Required    |
| Address line 2      | Optional    |
| Locality            | Required    |
| Administrative area | Optional    |
| Postal code         | Optional    |
| Country             | Required    |

3.  Should an address represent only United States addresses, or should the design allow other countries?

Always allow for Common Foreign Addresses.

4.  Which validation responsibilities should belong to Address rather than Contact?

Address Validates, all are validated.


## 3rd Set of Questions:

### Before writing either class, decide:
1.  Should name be one flexible display-name field, or separated into first name, middle name, last name, and business name?

I like one flexible display-name field, but I worry about validity and removing spam, etc.

2.  Should one contact be allowed to represent either a person or a business?

One contact can be either a person, a business, or the business contact enitity, might be Ai?

1.  Should phone and email both be required, or is one valid communication method enough?

One will be acceptable if both are not provided, if they are in valid format.

1.  What values should be allowed for preferred contact method?

Email or Phone, either is fine.


## 4th Set of Questions:

### Now return to the class-invariant exercise and decide what should happen when:
1.  both email and phone are missing


2.  preferred method is email, but email is missing


3.  the address supplied is not an Address object


4.  the display name contains only spaces


5.  the contact type is unsupported


### For each, state whether the object should be rejected, normalized, or accepted and why.
