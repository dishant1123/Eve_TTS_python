import requests

API_KEY = "23258c3bbd9eb3a964c6a17be4270035"      # Paste your API key here
city = input("Enter city: ")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(url, params=params)
data = response.json()

if response.status_code == 200:
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Weather:", data["weather"][0]["description"])
else:
    print("Error:", data.get("message", "Something went wrong"))
    
# https://openweathermap.org/?utm_source=chatgpt.com