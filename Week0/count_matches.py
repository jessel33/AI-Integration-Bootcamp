customer_names = [
    "Alice",
    "Bob",
    "Amanda",
    "Christopher",
    "Eve",
]

def count_names_starting_with_a(names): 
    count1 = 0 
    for name in names: 
        if name.startswith("A"): 
            count1 += 1 
            
    return count1


def count_names_longer_than_five_characters(names):
    count2 = 0
    for name in names:
        if len(name) > 5:
            count2 += 1
            
    return count2

longer_than_five_characters = count_names_longer_than_five_characters(customer_names)
print(longer_than_five_characters)


def count_long_names_start_with_A(names):
    count3 = 0

    for name in names:
        if len(name) > 5 and name.startswith("A"):
            count3 += 1

    return count3

long_a_names = count_long_names_start_with_A(customer_names)
print(long_a_names)
