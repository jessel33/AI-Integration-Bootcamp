# post_request.py
# Build a dictionary payload.
# Send it with requests.post().
# Print/check response.status_code.
# Convert the response with .json().
# Inspect what the API sends back.
#

import requests

def send_post_request():

    url = "https://jsonplaceholder.typicode.com/posts"

    data = {
        "model_year": 2006,
        "make": "Porsche",
        "model": "Cayman S",
        "engine_size": "3.4H",
        "transmission_type": "PDK 5 Speed",
        "planned_upgrades": True
    }

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        print(response.status_code)
        incoming_code = response.json()
        print(incoming_code)
        return True
    except requests.exceptions.RequestException as err:
        print(err)
        return False


if __name__ == "__main__":
    send_post_request()

