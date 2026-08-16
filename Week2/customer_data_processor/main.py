# main.py
# Coordinator of everything
#

import sys
from customer_processor import process_customers
from customer_selection import select_customer
from report_generator import generate_customer_report

def main():
    """Executes the core application logic"""


    print("Application started successfully")

    list_of_customers = process_customers("data/customers.csv")
    chosen_customer = select_customer(list_of_customers)
    final_customer_report = generate_customer_report(chosen_customer)

    print(final_customer_report)

if __name__ == "__main__":
    sys.exit(main())

