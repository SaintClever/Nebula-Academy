
---

# Introduction to APIs with Python

## Objective
By the end of this lesson, students will understand what APIs are, how to make HTTP requests in Python using the `requests` library, how to process JSON responses, and how to perform basic data manipulation.

## Prerequisites
- Basic knowledge of Python (variables, data types, loops, functions)
- Python installed on your computer
- `requests` library installed (you can install it using `pip install requests` in your terminal or command prompt)

## Materials
- IDE or text editor
- Terminal or Command Prompt
- Internet connection

---

### 1. Introduction to APIs 
**What is an API?**  
An API (Application Programming Interface) is a set of rules that allows different software applications to communicate with each other. It defines the methods and data formats for requests and responses.

**Real-world Analogy:**  
Think of an API like a menu in a restaurant. The menu provides a list of dishes you can order, along with a description of each dish. When you specify which dish you want, the kitchen (the system) prepares the meal and serves it. In this analogy, the menu is the API, the order is the request, and the dish served to you is the response.

**Types of APIs:**  
- Web APIs: Interfaces for interactions between the internet-connected devices.
- Library APIs: Interfaces within software libraries or frameworks.

---

### 2. Understanding HTTP Requests 
**What is HTTP?**  
HTTP (Hypertext Transfer Protocol) is the foundation of data communication on the World Wide Web. It's a protocol used for transmitting hypermedia documents, such as HTML.

**HTTP Methods:**  
- GET: Retrieve data from a specified resource.
- POST: Submit data to be processed to a specified resource.
- PUT: Update a specified resource.
- DELETE: Delete a specified resource.

**Structure of an HTTP Request:**  
- **URL (Uniform Resource Locator):** Specifies the location of the resource on the web.
- **Headers:** Provide information to both the client and server. It can include authentication tokens, specifying the type of response, etc.
- **Body (optional):** Contains data sent with a POST or PUT request.

**Status Codes:**  
- 200 OK: The request has succeeded.
- 404 Not Found: The server can't find the requested resource.
- 500 Internal Server Error: The server encountered an unexpected condition.

---

### 3. Using the `requests` Library in Python 
Python’s `requests` library simplifies making HTTP requests. It abstracts the complexities of making requests behind a beautiful, simple API.

**Making a GET Request:**
```python
import requests

response = requests.get('https://api.example.com/data')
```

**Handling Response:**
```python
if response.status_code == 200:
    print('Success!')
else:
    print('An error has occurred.')
```

**JSON Response:**
JSON (JavaScript Object Notation) is a lightweight format for storing and transporting data. The `requests` library can easily convert a JSON response into a Python dictionary using `.json()` method.

```python
data = response.json()
print(data)
```

---

### 4. Hands-on Example: Fetching Data from JSONPlaceholder API 
**Objective:** Fetch posts from JSONPlaceholder, a free fake online REST API.

**Example Code:**
```python
import requests

# Fetching data from the API
response = requests.get('https://jsonplaceholder.typicode.com/posts')
if response.status_code == 200:
    posts = response.json()
    # Printing the first post
    print(posts[0])
else:
    print("Failed to retrieve data")
```

**Data Manipulation:**
Iterating over data and accessing specific elements.
```python
for post in posts[:5]:  # Limiting to first 5 posts for brevity
    print(f"Title: {post['title']}\nBody: {post['body']}\n")
```

---

### 5. Q&A and Recap 
Take this time to recap the key points covered in today's lesson and address any questions the students may have.

---

### 6. Exercise 
**Tasks:**
1. Print the name and email of each user from the `/users` endpoint.
2. Find users who work for the company with the catchphrase "Harness real-time e-markets".
3. Create and print a list of usernames in alphabetical order.

**Endpoint:** `https://jsonplaceholder.typicode.com/users`

---

### Wrap-up
This lesson provided a foundational understanding of APIs, including how to make requests, handle responses, and manipulate

 data in Python. Students are encouraged to explore other public APIs and consider how APIs can be utilized in their projects.

---

## Extended Exercise: Deep Dive into Data Manipulation with JSONPlaceholder API

These exercises aim to deepen your understanding of APIs by interacting with the JSONPlaceholder API, focusing on data retrieval, analysis, and manipulation. They will require you to apply logic, work with different data structures, and utilize Python's capabilities more extensively.

### Pre-requisites:
- Complete the lesson and understand the basics of making API requests, parsing JSON responses, and basic Python data manipulation.

### Exercise Tasks:

#### Task 1: Detailed User Profiles
- **Objective:** Fetch data from the `/users` endpoint (`https://jsonplaceholder.typicode.com/users`). For each user, print a detailed profile that includes their name, email, company name, and address in a nicely formatted output.
- **Challenge:** Additionally, format the address to include street, suite, city, and zipcode in a single string.

#### Task 2: Posts and Comments Analysis
1. **Fetch Posts:** Retrieve all posts for a specific user by their ID from the `/posts` endpoint. Choose any user ID between 1 to 10.
2. **Fetch Comments for Posts:** For each post retrieved, fetch comments from the `/comments` endpoint filtering by the post's ID.
3. **Analysis:** For each post, print the title, the number of comments it has received, and the email addresses of the commenters.
4. **Insight:** Identify the post with the most comments and print its title and the total number of comments.

#### Task 3: To-Do Analysis for Users
- **Objective:** Fetch to-do items for each user from the `/todos` endpoint and perform an analysis of completed versus pending tasks.
- **Tasks:**
  1. For each user, calculate the total number of to-do items and the number of completed tasks.
  2. Determine the user with the highest number of completed tasks and print their name and the number of completed tasks.
  3. **Bonus:** For the user identified in step 2, fetch and print their company name and catchphrase.

### Guidelines for the Exercises:
- Use functions to organize your code. Consider creating a function for each major task, such as fetching data, parsing, and printing.
- Pay attention to error handling. Ensure your script gracefully handles any network errors or unexpected responses.
- Be mindful of API rate limits. Cache responses or use loops judiciously to avoid excessive requests.
- Experiment with Python's string formatting features to create readable and well-formatted output.

### Expected Learning Outcomes:
- Gain proficiency in making HTTP requests and handling responses.
- Develop a deeper understanding of working with JSON data and Python dictionaries.
- Improve data manipulation and analysis skills in Python.
- Learn to extract insights from data and present information in a clear, structured format.

---