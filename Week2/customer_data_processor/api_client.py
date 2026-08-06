# api_client.py
# This module should:
# Build the API request.
# Send the HTTP request.
# Check whether the request succeeded.
# Convert the JSON response into Python data.
# Handle connection, timeout, and invalid-response errors.
# Return useful data to the rest of the program.
#
# functions inputs: desired request and data required for request
# functions return value: python dictionary of requested data

import requests

GEOCODING_ENDPOINT = "https://geocoding-api.open-meteo.com/v1/search"
STATE_CODES_TO_NAMES = {
    "AZ": "Arizona",
    "PA": "Pennsylvania"
}

def find_location(city, state, country):
   
    geocoding_parameters = {
        "name": city,
        "count": 5,
        "language": "en",
        "format": "json",
        "countryCode": country
    }

    state_name = STATE_CODES_TO_NAMES.get(state.upper())

    if state_name is None:
        return {}

    try:
        geocoding_response = requests.get(GEOCODING_ENDPOINT, params=geocoding_parameters, timeout=10.0)
        geocoding_response.raise_for_status()
        geocoding_data = geocoding_response.json()
        
        # return geocoding_data.get("results", [])

    except requests.exceptions.RequestException:
        return {}

    geocoding_returned_results = geocoding_data.get("results", [])
    for location in geocoding_returned_results:
        if location.get("admin1") == state_name:
            return location

    return {}
    

geocoding_find_location = find_location("Phoenix", "AZ", "US")
print(geocoding_find_location)

