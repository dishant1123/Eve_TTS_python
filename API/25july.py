"""
API  :  application  program interface 

pip install import requests

GET → Retrieve data.
POST → Send new data.
PUT/PATCH → Update data.
DELETE → Remove data.


Code	Meaning	Example Use
200 OK	Request succeeded	Data fetched successfully
201 Created	Resource created	New user added via API
400 Bad Request	Client error	Wrong parameters sent
401 Unauthorized	Authentication required	Missing/invalid API key
403 Forbidden	Access denied	No permission to view resource
404 Not Found	Resource not found	Wrong URL or missing data
500 Internal Server Error	Server-side problem	API server crashed
502 Bad Gateway	Invalid response from upstream server	Proxy error
503 Service Unavailable	Server temporarily down	Maintenance mode
"""

# ex :1 GET
import requests

"""city ="New Delhi"
url =f'https://wttr.in/{city}?format=j1'

response = requests.get(url) 

print("status code : ",response.status_code)
data = response.json()
print("city :",city)
print("weather : ",data['current_condition'][0]['weatherDesc'][0])
print("temperature : ",data['current_condition'][0]['temp_C'])
print("humidity : ",data['current_condition'][0]['humidity'])

"""
# ex:2 GET

"""url ="https://fakestoreapi.com/products"

response = requests.get(url)

print("status code : ",response.status_code)
products = response.json()

# for i in products[0:5]:  # 0 1 2 3 4 
    # print(i['title'])

# print(products[0]['title'])
# print(products[1]['description'])
for i in products:  # 0 1 2 3 4 
    print(i['title'])
    print(i['price'])
    print("-"*40)
"""

# ex :3 GET  
"""
url ="https://randomuser.me/api/"

response = requests.get(url)

data =response.json()

print("status code : ",response.status_code)

for  i in data['results']:
    print(i['name']['first'])
    print(i['location']['city'])
    print("-"*40)
"""

# ex :4 Query parameters  :  instead of writing parameters in the URL pass them using parameters. 

url ="https://jsonplaceholder.typicode.com/comments"

"""
params = {
    "postId": 1
}
"""
params = {
    "id": 1
}
response = requests.get(url,params=params)

print(response.url)
print(response.status_code)

comments = response.json()

for i in comments:
    print(i['email'])

# name , email  for post_id 1,2,3,4,5