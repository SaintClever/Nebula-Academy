import requests

# Making a GET request to a hypothetical API
response = requests.get("https://cat-fact.herokuapp.com/facts")

# Assuming the response contains JSON data
data = response.json()

# Example of accessing data
for entry in data:
    print(entry['text'])
    print('=========================')