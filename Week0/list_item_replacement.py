customer_names = [
    "Alice",
    "Bob",
    "Amanda",
    "Bob",
]

def update_customer_name(names, target_name, new_name):
    found_match = False
    for index, name in enumerate(names):
        if name.strip().lower() == target_name.strip().lower():
            names[index] = new_name
            found_match = True
        
    return found_match


result = update_customer_name(customer_names, "Bob", "Bobby")
print(f"{result} {customer_names}")

result2 = update_customer_name(customer_names, "Christopher", "Chris")
print(f"{result2} {customer_names}")
