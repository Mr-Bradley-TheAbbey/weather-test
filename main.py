import requests
import json
import os

url = "http://api.weatherapi.com/v1/current.json"
params = {
    "key": "cee822c542374998b6e140536240805",
    "q": "Reading",
    "aqi": "no"
}

response = requests.get(url, params=params)

json_data = response.json()

last_updated = json_data["current"]["last_updated"]
last_updated = last_updated[-5::]
temp_c = json_data["current"]["temp_c"]
wind_mph = json_data["current"]["wind_mph"]
wind_degree = json_data["current"]["wind_degree"]
pressure_mb = json_data["current"]["pressure_mb"]

os.system('clear')
print("Reading Weather App")
print("___________________")
print()
print(f"Last updated at: {last_updated}")
print()
print(f"Temperature: {temp_c} C")
print(f"Wind Speed: {wind_mph} mph")
print(f"Wind direction: {wind_degree} degrees ")
print(f"Pressure: {pressure_mb} mb ")
print()
print("___________________")

