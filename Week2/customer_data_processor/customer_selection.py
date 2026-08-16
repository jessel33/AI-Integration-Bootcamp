# customer_selection.py
# Customer selection/input structure,
# test for valid input type and value.
# Return one customer dictionary to report generator.
#


def select_customer(customers):
    """
    Customer-selection/input loop, 
    validates input for type and range,
    Returns selected customer dictionary.
    """


    y = True
    while y:
        x = input("Pick a customer by their ID number, please enter a number: ")
        try:
            x = int(x)
            
        except ValueError:
            print("Wrong input, please try again.")
            continue

        if 1 <= x <= len(customers):
            customer_dictionary = customers[x - 1]
            y = False

        else:
            print("Your input was outside of the stored customer ID numbers.")
            
    print("Thank you!")
    return customer_dictionary

