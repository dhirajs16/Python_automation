# Automation with Python

- **Lesson 1**: Basic selenium setup.
- **Lesson 2**: Login automation.
- **Lesson 3**: API accessing with request lib, Difference in `json()`, `json.dumps()` and `json.loads()`, requests lib post operation.
- **Lesson 4**: automate sending gamils with `yagmail`

<hr>

## **Lesson 3**

### **API Accessing : Brief on json module methods**

`json()` method and the json module's `.dumps()` and `.loads()` functions serve different purposes. Let’s break it down:

`requests.Response.json()`

Purpose: Used to parse JSON content from an HTTP response.

Usage: When you make an HTTP request using the requests library in Python, and the response contains JSON data, you use .json() to convert the JSON response to a Python dictionary.

Example:

```python
import requests

response = requests.get('https://api.example.com/data')
data = response.json()  # Converts the JSON response to a dictionary
print(data)

```

`json.loads()`

Purpose: Used to convert a JSON string to a Python dictionary.

Usage: When you have a JSON formatted string and need to work with it as a Python dictionary.

Example:

```python
import json

json_str = '{"name": "John", "age": 30}'
data = json.loads(json_str)  # Converts the JSON string to a dictionary
print(data)

```

`json.dumps()`

Purpose: Used to convert a Python dictionary to a JSON string.

Usage: When you have a Python dictionary and need to convert it to a JSON formatted string, perhaps to save to a file or send as a part of an HTTP request.

Example:

python

```
import json

data = {"name": "John", "age": 30}
json_str = json.dumps(data)  # Converts the dictionary to a JSON string
print(json_str)

```

#### **Summary**
`.json()`: Parses JSON data from an HTTP response into a Python dictionary.

`json.loads()`: Converts a JSON string to a Python dictionary.

`json.dumps()`: Converts a Python dictionary to a JSON string.

<hr>

## **Lesson 4**

- To hide sender and receiver emails use `config()` method of `python-decouple` package with a `.env` file.

```python

pip install python-decouple

```

- `yagmail` is a GMAIL/SMTP client that aims to make it as simple as possible to send emails.

```python

pip install yagmail

```