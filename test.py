# a simple script for locally testing your app & sendgrid configuration

import requests

url = "http://127.0.0.1:5000/"
data = {"email": "test@example.com"}
response = requests.post(url, data=data)
print(response.text)