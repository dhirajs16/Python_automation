'''
The .json() method and the json module's .dumps() and .loads() functions serve different purposes. 
Let's break it down:

requests.Response.json()
Purpose: Used to parse JSON content from an HTTP response.
Usage: When you make an HTTP request using the requests library in Python, and the response 
contains JSON data, you use .json() to convert the JSON response to a Python dictionary.

json.loads()
Purpose: Used to convert a JSON string to a Python dictionary.
Usage: When you have a JSON formatted string and need to work with it as a Python dictionary.

json.dumps()
Purpose: Used to convert a Python dictionary to a JSON string.
Usage: When you have a Python dictionary and need to convert it to a JSON formatted string, 
perhaps to save to a file or send as a part of an HTTP request.


File Handling with Python
json.dump()
Purpose: Writes JSON data to a file.
Usage: When you need to serialize a Python object and write it to a file as JSON.

json.load()
Purpose: Reads JSON data from a file and converts it to a Python object.
Usage: When you need to deserialize JSON data from a file to a Python object.
'''


'''Accesing Data get request'''
# import requests
# URL = ''
# req = requests.get(url=URL)
# content = req.json()
# print(content['message'])



'''How to use json methods (dumps & loads)'''
# from json import dumps, loads

# json_string = '{"name":"Shyam", "course":"B.Tech"}'
# print("json_str:", json_string)
# print("json_str type:", type(json_string))

# print('===============================')
# jstd = loads(json_string)
# print("jstd type",type(jstd))
# print("jstd=",jstd)

# print('===============================')
# dtjs = dumps(jstd)
# print("dtjs type", type(dtjs))


'''request.post() method'''
import requests

URL = 'https://api.languagetoolplus.com/v2/check'

data = {
    'text': 'Ths iz eazy!',
    'language': 'en-US'
}

response = requests.post(url=URL, data=data)
content = response.json()


print('response type:', type(response))
print('content type:', type(content))
print(content)