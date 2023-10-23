import requests
import json

# url = 'https://www.google.com/search?q=pytest'
#
# r = requests.get(url)
# #print(r.text)

# url = 'https://regres.in/api/users'
# r = requests.get(url)
# print(r.status_code)
# # Show user-agent
# print(r.headers)
# print(r.request.headers)
# print(r.text)
#
# print(r.json())

"""This is GET demo"""
URL = "https://httpbin.org/get"
myparams = {'key1': 'value1', 'key2':'value2'}
r = requests.get(url=URL, params=myparams)
print(r.url)

for key, value in r.json().items():
    print(key, ":", value)

print(r.json()["headers"]["Host"])

"""This is POST demo"""

URL = "https://httpbin.org/post"
payload = {'key1': 'value1', 'key2':'value2'}

r = requests.post(url=URL,json=payload)
print(r.url)
print(r.status_code)
print(r.text)