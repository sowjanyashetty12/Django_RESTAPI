import requests

endpoint="http://localhost:8000/api"  #equivalent to http://127.0.0.1:8000/

# THIS IS ALL ABOUT CONNECTING TO THE API AND PRINTING THE RESPONSE OF THE API


# response=requests.get(endpoint)
# print(response.text)  #will give the raw form of whtever you see on chrome

# print(response.status_code) 

# print(response.json())
# print(response.json()['message'])



# response=requests.get(endpoint)
# print(response.text)

response=requests.post(endpoint,json={"title":"Hello world!","description":"random","price":"15"})
print(response.text)