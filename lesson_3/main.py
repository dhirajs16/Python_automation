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



import requests
URL = ''
req = requests.get(url=URL)
content = req.json()
print(content['message'])

