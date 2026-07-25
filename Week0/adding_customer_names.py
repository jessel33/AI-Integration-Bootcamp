customer_names = [
    "Alice",
    "Bob",
    "Amanda",
]

def add_customer_name(names, new_names):
    for x in names:
        if x.strip().lower() == new_names.strip().lower():
            return False

    names.append(new_names)
    return True


result1 = add_customer_name(customer_names, "Christopher")
print(f"{result1} {customer_names}")
result2 = add_customer_name(customer_names, "  amanda  ")
print(f"{result2} {customer_names}")