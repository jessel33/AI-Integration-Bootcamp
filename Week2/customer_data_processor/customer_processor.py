# customer_processor.py
# This file's responsibility is to coordinate
# the customer information workflow.
#

import pprint
from csv_reader import read_customer_csv
from api_client import find_location, get_current_weather
import weather_codes


def process_customers(file_path):
    """
    Processes customer csv data to retreive the current weather for customer's location.
    Call read_customer_csv to get city, state and country strings
    for find_location which returns latitude and longitude floats.
    These are passed to get_current_weather which returns a dictionary of the weather or an empty dictionary if location is not found.
    """

    processed_customers = []
    customers = read_customer_csv(file_path)
    for customer in customers:
        location = find_location(customer["city"], customer["state"], customer["country"])
        processed_customer = customer.copy()
        if location:
            weather = get_current_weather(location["latitude"], location["longitude"])
            weather_code = weather["weather_code"]
            if weather_code:
                weather_description = weather_codes.WMO_WEATHER_CODES[weather_code]
                weather.update({"weather_code": weather_description})
            
        else:
            weather = {}

        processed_customer["weather"] = weather
        processed_customers.append(processed_customer)

    return processed_customers


if __name__ == "__main__":
    customer_data = process_customers("data/customers.csv")
    pprint.pprint(customer_data)
