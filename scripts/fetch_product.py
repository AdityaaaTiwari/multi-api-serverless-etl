import requests
import json

url = "https://dummyjson.com/products"

response = requests.get(url)

with open("product.json", "w") as f:
    json.dump(response.json(), f, indent=4)

print("Product data saved successfully!")