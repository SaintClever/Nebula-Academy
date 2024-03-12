import requests, pprint

response = requests.get("https://jsonplaceholder.typicode.com/users")
posts = response.json() if response.status_code == 200 else print("Failed to retrieve data")


# 1. Print the name and email of each user from the /users endpoint.
for post in posts[:5]:
    print(f"Name: {post.get("name")}\nEmail: {post.get("email")}\n")


# 2. Find users who work for the company with the catchphrase "Harness real-time e-markets".
# print()
print("=" * 30)
for post in posts:
    if post.get("company").get("bs").capitalize() == "Harness real-time e-markets":
        print(post.get("company").get("bs").capitalize())
        print(f"Name: {post.get("name")}\n")


# 3. Create and print a list of usernames in alphabetical order.
print("=" * 30)
print(sorted([post.get("username") for post in posts]))
print()


# Task 1: Detailed User Profiles
# Objective: Fetch data from the /users endpoint (https://jsonplaceholder.typicode.com/users). For each user, print a detailed profile that includes their name, email, company name, and address in a nicely formatted output.
# Challenge: Additionally, format the address to include street, suite, city, and zipcode in a single string.
print("=" * 30)
for post in posts:
    print(f"Name: {post.get("name")}\nEmail: {post.get("email")}\nCompany: {post.get("company").get("name")}")

    for key, value in post.get("address").items():
        print(f"{key}: {value}")
    print()


# Task 2: Posts and Comments Analysis
# Fetch Posts: Retrieve all posts for a specific user by their ID from the /posts endpoint. Choose any user ID between 1 to 10.
print("=" * 30)
def fetch_posts(id: int):
    # for post in posts:
    #     if id == post.get("id"):
    #         return post
    #     else:
    #         return "Choose any user ID from 1 to 10"
    
    return next(post if id == post.get("id") else "Choose any user ID from 1 to 10" for post in posts)

print(fetch_posts(1))
print()


# Fetch Comments for Posts: For each post retrieved, fetch comments from the /comments endpoint filtering by the post's ID.

# Analysis: For each post, print the title, the number of comments it has received, and the email addresses of the commenters.

# Insight: Identify the post with the most comments and print its title and the total number of comments.
def request_response(id: int | None = '', endpoint: str | None = 'posts'):
    response = requests.get(f"https://jsonplaceholder.typicode.com/{endpoint}")
    users = response.json() if response.status_code == 200 else print("Failed to retrieve data")

    print(''.join(user.get('body') + '\n\n' for user in users))
    print(''.join(f'title: {user.get('title').title()}\n' for user in users))

request_response()