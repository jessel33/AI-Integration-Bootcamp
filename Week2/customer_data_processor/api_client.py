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
import state_codes

GEOCODING_ENDPOINT = "https://geocoding-api.open-meteo.com/v1/search"
OPEN_METEO_FORECAST_ENDPOINT = "https://api.open-meteo.com/v1/forecast"


def find_location(city, state, country):
    """
    Finds a geographic location using a city, state, and country.
    Receives those three values as strings.
    Returns the matching location as a dictionary,
    or an empty dictionary if no location is found.
    """

    geocoding_parameters = {
        "name": city,
        "count": 5,
        "language": "en",
        "format": "json",
        "countryCode": country
    }

    state_name = state_codes.STATE_CODES_TO_NAMES.get(state.upper())

    if state_name is None:
        return {}

    try:
        geocoding_response = requests.get(GEOCODING_ENDPOINT, params=geocoding_parameters, timeout=10.0)
        geocoding_response.raise_for_status()
        geocoding_data = geocoding_response.json()

    except requests.exceptions.RequestException:
        return {}

    locations = geocoding_data.get("results", [])
    for location in locations:
        if location.get("admin1") == state_name:
            return location

    return {}


def get_current_weather(latitude, longitude):
    """
    Gets the current weather for a latitude and longitude.
    Receives those two values as floats.
    Returns the current weather for said location as a dictionary,
    or an empty dictionary if weather data cannot be retrieved.
    """

    weather_parameters = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,weather_code",
        "temperature_unit": "fahrenheit",
        "timezone": "auto"
    }

    try:
        weather_response = requests.get(OPEN_METEO_FORECAST_ENDPOINT, params=weather_parameters, timeout=10.0)
        weather_response.raise_for_status()
        weather_data = weather_response.json()
        
        return weather_data.get("current", {})

    except requests.exceptions.RequestException:
        return {}


if __name__ == "__main__":
    geocoding_find_location = find_location("Pittsburgh", "PA", "US")
    print(geocoding_find_location)
    if geocoding_find_location:
        weather_information = get_current_weather(geocoding_find_location["latitude"], geocoding_find_location["longitude"])
        print(weather_information)

