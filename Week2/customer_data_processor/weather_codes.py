# weather_codes.py
#
# Open-Meteo uses numeric World Meteorological Organization (WMO)
# weather interpretation codes (weather_code) in its API responses
# to describe current or forecasted weather conditions.

weather_codes = {
    0: "Clear sky",
    1: "Mainly clear, partly cloudy, and overcast",
    2: "Mainly clear, partly cloudy, and overcast",
    3: "Mainly clear, partly cloudy, and overcast",
    45, 48: "Fog and depositing rime fog"
    51-55: "Drizzle (light to dense)"
    56, 57: "Freezing Drizzle (light and dense)"
    61-65: "Rain (slight to heavy)"
    66, 67: "Freezing Rain (light and heavy)"
    71-75: "Snow fall (slight to heavy)"
    77, 85-86: "Snow, including grains and showers"
    80-82: "Rain showers (slight to violent)"
    95-99: "Thunderstorms (slight to heavy), potentially with hail"
}

