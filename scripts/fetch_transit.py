import requests
import json

url = "https://api-v3.mbta.com/stops"

response = requests.get(url)

if response.status_code == 200:
    with open("transit.json", "w") as f:
        json.dump(response.json(), f, indent=4)

    print("Transit data saved successfully!")
else:
    print("Failed to fetch transit data")