# csv_reader.py
# File that will read incoming csv files
# and converts it into python dictionaries.
# with built-in csv module


import csv

def read_customer_csv(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", newline="") as rfile:
            csv_dictionary_reader = csv.DictReader(rfile)
            dictionary_rows = []
            for row in csv_dictionary_reader:
                row["customer_id"] = int(row["customer_id"])
                dictionary_rows.append(row)

            return dictionary_rows
    except FileNotFoundError:
        print(f"The customer.csv file was not found here: {file_path}")
        return []
    
    except ValueError:
        print("A customer_id cannot be converted to an integer.")
        return []
    
if __name__ == "__main__":

    testing1 = read_customer_csv("data/customers.csv")
    print(testing1)

