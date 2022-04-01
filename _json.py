# https://httpbin.org/
# What is JSON?
"""
* JSON stands for **Java Script Object Notation**
* A standardised format commonly used for data transfer.
* Readable both of Humans and Machine.
* Used in Databases and API's.
* XML is one more format used for data transfer.
"""

info = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}

"""
* Python has builtin module called `json` to help work with JSON data
# Serilisation and de-serilisation
* Encoding data into JSON format is called **serialisation**. e.x. Converting a python list to a JSON 
* Decoding JSON data is called **de-serilisation** e.x. Reading JSON data into Python Dictionary/List
"""

# Serialising data into JSON file.
# Let's consider a python dictionary
data = {
          "user": {
                     "name": "John Doe",
                     "age": 26
                  }
       }
"""
* The json module exposes two methods for serializing Python objects into JSON format
* **dump()** will write Python data to a file-like object. We use this when we want to serialize our Python data to an external JSON file.
* **dumps()** will write Python data to a string in JSON format. This is useful if we want to use the JSON elsewhere in our program, or if we just want to print it to the console to check that it’s correct.
"""
import json

with open('data.json', 'w') as f:
   json.dump(data, f, indent=4)

# Running above code creates a file named data.json, with python Dictionary converted into JSON format.

# Extracting COVID information from free api to csv file
import requests
import json
import csv

url = "https://api.apify.com/v2/key-value-stores/toDWvRj1JpTXiM8FF/records/LATEST?disableRedirect=true"
response = requests.request("GET", url)
data = json.loads(response.text)
region_data = data['regionData']

with open('data.csv', 'w') as f:
    csv_writer = csv.DictWriter(f, ["region", "activeCases", "recovered", "newInfected", "deceased", "newDeceased", "totalInfected"])
    csv_writer.writeheader()
    for item in region_data:
        csv_writer.writerow(item)

# Email validator - https://api.eva.pingutil.com/email?email=fname.lname@company.com
emails = [
    {"email": "hello.world", "expected_result": "failure"},
    {"email": "hello.world@company.com", "expected_result": "success"},
    {"email": "hello.world@", "expected_result": "failure"},
    {"email": "hello.world@.com", "expected_result": "failure"},
    {"email": "hello.world@company.gov.in", "expected_result": "success"},
    {"email": "hello.world@company.edu", "expected_result": "success"},
]

for item in emails:
    url = f"https://api.eva.pingutil.com/email?email={item['email']}"

    print(f"Hitting URL {url}")

    # Hit the webservice
    response = requests.request("GET", url)

    # Convert the JSON object to text
    data = json.loads(response.text)

    # Assert the response
    try:
        assert (item['expected_result'] == data['status'])
    except AssertionError:
        print(f"Incorrect Response from server {item['email']} {data['status']}")

# Webservice to get Bank Information using IFSC code
codes = [
    {"code": "HDFC0001755", "expected_branch": "100 FEET ROAD-INDIRA NAGAR"},
    {"code": "SBIN0040014", "expected_branch": "BASAVANAGUDI"},
    {"code": "ICIC0000002", "expected_branch": "BANGALORE - M G ROAD"}
    ]

for item in codes:
    url = f"https://ifsc.razorpay.com/{item}"

    print(f"Hitting url {url}")

    # Hit the webservice
    response = requests.request("GET", url)

    # Convert the JSON object to text
    data = json.loads(response.text)

    # Assert the response
    try:
        assert (item['expected_branch'] == data['BRANCH'])
    except AssertionError:
        print(f"Incorrect Response from Server {item['code']} {data['BRANCH']}")
