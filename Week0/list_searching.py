customer_names = [
    "Alice",
    "Bob",
    "Amanda",
    "Robert",
]

def find_customer(names, target_name):
    for name in names:
        if name.strip().lower() == target_name.strip().lower():
            return name
        
    return None


result = find_customer(customer_names, "  amanda  ")
print(result)
