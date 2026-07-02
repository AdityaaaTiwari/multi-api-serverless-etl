import requests
import json

url = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=28.6139"
    "&longitude=77.2090"
    "&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m"
)

response = requests.get(url)

if response.status_code == 200:
    with open("weather.json", "w") as f:
        json.dump(response.json(), f, indent=4)

    print("Weather data saved successfully!")
else:
    print("Failed to fetch weather data")