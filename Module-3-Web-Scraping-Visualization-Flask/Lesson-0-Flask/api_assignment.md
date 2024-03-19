# Building Simple Web Applications Assignment

## Overview

In this assignment, you will enhance your Flask application to handle more complex interactions. Specifically, you will develop a POST route capable of accepting JSON data, performing validation on this data, and responding appropriately. This will deepen your understanding of RESTful API development with Flask, focusing on server-client interactions that involve JSON data transmission.

## Objectives

- Create a POST route in a Flask application that accepts JSON data.
- Validate incoming JSON data for specific criteria.
- Return a modified version of the valid data or an error message in JSON format.

## Assignment Details

### Step 1: Set Up Your Flask Environment

Ensure your Flask development environment is set up correctly. If you're continuing from a previous assignment, you can build upon your existing Flask application. Otherwise, set up a new Flask application as your starting point.

### Step 2: Implement a POST Route

Create a new route in your Flask application that only accepts POST requests. This route should be designed to process JSON data sent in the request body. Use the route `/api/process-data` for this purpose.

Example route definition:

```python
@app.route('/api/process-data', methods=['POST'])
def process_data():
    # Your code here
    pass
```

### Step 3: Accepting and Validating JSON Data

Inside the `process_data` function, write code to:

1. Check if the incoming request contains JSON data.
2. Validate the JSON data. For this assignment, assume the JSON data must contain at least the following keys with corresponding value types:
   - `name`: A string representing a user's name.
   - `age`: An integer representing the user's age.
3. If the JSON data is missing any of these keys or the value types do not match the expected types, return an error response in JSON format. The error response should include an appropriate error message and a 400 status code.

Example validation and error response:

```python
from flask import request, jsonify

# Inside your route function
if not request.is_json:
    return jsonify({"error": "Request must be JSON"}), 400

data = request.get_json()

if 'name' not in data or not isinstance(data['name'], str):
    return jsonify({"error": "Invalid or missing name"}), 400

if 'age' not in data or not isinstance(data['age'], int):
    return jsonify({"error": "Invalid or missing age"}), 400
```

### Step 4: Modifying and Returning the Data

If the JSON data is valid, write logic to modify the data in some way. For example, you could add a new key-value pair to the data, such as `status: "processed"`, or modify existing values.

Then, return the modified data in JSON format, along with a 200 status code to indicate success.

Example modification and successful response:

```python
# Assuming data validation passed
data['status'] = "processed"
return jsonify(data), 200
```

## Submission Guidelines

- Submit your Flask application files containing the implemented POST route, validation logic, and response handling.
- Ensure your code is well-commented to explain the logic behind your implementation.
- If you've hosted your Flask application online (e.g., on Heroku), include the URL to your hosted application.

## Evaluation Criteria

- **Functionality**: The POST route correctly accepts, validates, and responds to JSON data as specified.
- **Error Handling**: The application appropriately returns error messages and status codes when receiving invalid data.
- **Code Quality**: The code is well-organized, commented, and follows Python best practices.

Remember, this assignment is an opportunity to apply the concepts learned in the lecture. Take your time to test your application thoroughly and ensure it behaves as expected. Good luck!