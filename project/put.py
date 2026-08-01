import requests

data = {
    "name": "Dishant Shah",
    "course": "Generative AI"
}

response = requests.put(
    "http://localhost:8000/students/1",
    json=data
)

print(response.status_code)
print(response.json())
