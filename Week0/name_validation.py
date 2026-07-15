customer_names1 = [
    "Alice",
    "   ",
    "Amanda",
]

customer_names2 = [
    "Alice",
    " B ",
    "Amanda"
]

def all_names_are_valid(names):
    for name in names:
        if name.strip() == "":
            return False

    return True

cust_names_valid = all_names_are_valid(customer_names1)
print(cust_names_valid)


def all_names_are_valid_2x(names):
    for name in names:
        cleaned_name = name.strip()
        if(cleaned_name == "" or len(cleaned_name) < 2):
            return False

    return True

cust_names_valid2x = all_names_are_valid_2x(customer_names2)
print(cust_names_valid2x)