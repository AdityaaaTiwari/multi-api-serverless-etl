import requests
import json

url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"

response = requests.get(url)

with open("earthquake.json", "w") as f:
    json.dump(response.json(), f, indent=4)

print("Earthquake data saved successfully!")