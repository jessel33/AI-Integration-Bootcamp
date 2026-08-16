# report_generator.py
# This file will create a business report for the user
# with the following information:
# customer name
# city/state
# current temperature
# feels-like temperature
# humidity
# weather description
# Note:  Comment on weather conditions that might 
# influence user traveling to the customer’s location.
#


def generate_customer_report(customer):
    """
    Receives one processed customer dictionary.
    Builds and returns a readable business report as a string.
    """

    first_name = customer["first_name"]
    last_name = customer["last_name"]
    full_name = f"{first_name} {last_name}".strip()

    city = customer["city"]
    state = customer["state"]

    weather_dict = customer.get("weather", {})
    temperature = weather_dict.get("temperature_2m", "N/A")
    feels_like_temperature = weather_dict.get("apparent_temperature", "N/A")
    humidity = weather_dict.get("relative_humidity_2m", "N/A")
    description = weather_dict.get("weather_description", "N/A")
    if isinstance(temperature, float):
        if temperature >= 85:
            weather_note = "The temperature in " + city + ", " + state + " is greater than 85°F. Drink lots of water."

        elif temperature < 85 and temperature > 55:
            weather_note = "The temperature in " + city + ", " + state + " is above 55°F but below 85°F. Enjoy your travels."

        else:
            weather_note = "The temperature in " + city + ", " + state + " is less than 56°F, take a jacket."

    else:
        weather_note = "The system is unavailable, no weather information was obtained."

    filtered_metrics = [
        f"Customer: {full_name}",
        f"City: {city}",
        f"State: {state}",
        f"Current Temperature: {temperature}°F",
        f"Feel Like Temperature: {feels_like_temperature}°F",
        f"Relative Humidity: {humidity}%",
        f"Condition: {description}",
        f"Note: {weather_note}"
    ]
    

    return " BUSINESS REPORT // " + " | ".join(filtered_metrics)

