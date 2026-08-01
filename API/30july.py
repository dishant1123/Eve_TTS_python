"""import requests

API_KEY = "YOUR_API_KEY"      # Paste your API key here

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
    
"""

# ex :1 session  :

"""import requests

session = requests.Session()

response = session.get("https://jsonplaceholder.typicode.com/posts/1")

print(response.status_code)
print(response.json())
"""
# ex :2 reusing headers : 

"""import requests

session = requests.Session()
session.headers.update({
    "User-Agent": "Dishant-App"
})

url = "https://jsonplaceholder.typicode.com/posts"
response = session.get(url)
print(response.status_code)

"""
# ex :3 pip install aiohttp

import asyncio
import aiohttp

async def get_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            print(data["title"])

async def main():
    await asyncio.gather(
        get_post(1),
        get_post(2),
        get_post(3)
    )

asyncio.run(main())
