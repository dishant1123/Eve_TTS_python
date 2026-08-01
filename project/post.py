import requests

data = {
    "id": 3,
    "name": "Amit",
    "course": "AI"
}

response = requests.post(
    "http://localhost:8000/students",
    json=data
)

print(response.status_code)
print(response.json())
