"""
Weather Service

This module handles interactions with external weather services to fetch
real-time weather data for specific locations.

Dependencies:
    - requests

Functions:
    get_weather(city): Fetches current temperature and condition for a city.

AUTHOR: Deepak Rakhit
GITHUB: https://github.com/deepakrakshit
"""

import requests

def get_weather(city: str) -> str:
    """
    Fetch current weather for a city using the public wttr.in service.
    
    This function connects to the wttr.in JSON API to retrieve the current
    temperature (Celsius) and weather description.

    Args:
        city (str): The name of the city to fetch weather for.

    Returns:
        str: A formatted string containing the city name, temperature, and description.
             Returns an error message string if the request fails.
    """
    try:
        # Requesting format=j1 gives a JSON response
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url, timeout=5)
        data = response.json()

        current = data["current_condition"][0]
        temp = current["temp_C"]
        desc = current["weatherDesc"][0]["value"]

        return f"{city.title()}: {temp}°C, {desc}"

    except Exception:
        return (
            "⚠️ Unable to fetch weather at the moment.\n"
            "This feature uses a public weather service and may be temporarily unavailable."
        )