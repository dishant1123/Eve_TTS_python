import requests

response = requests.delete(
    "http://localhost:8000/students/1"
)

print(response.status_code)
print(response.json())
