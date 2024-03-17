import requests, pprint

# response = requests.get("https://jsonplaceholder.typicode.com/users")
# posts = response.json() if response.status_code == 200 else print("Failed to retrieve data")
# # 1. Print the name and email of each user from the /users endpoint.
# for post in posts[:5]:
#     print(f"Name: {post.get("name")}\nEmail: {post.get("email")}\n")
#
#
# # 2. Find users who work for the company with the catchphrase "Harness real-time e-markets".
# print("=" * 30)
# for post in posts:
#     if post.get("company").get("bs").capitalize() == "Harness real-time e-markets":
#         print(post.get("company").get("bs").capitalize())
#         print(f"Name: {post.get("name")}\n")
#
#
# # 3. Create and print a list of usernames in alphabetical order.
# print("=" * 30)
# print(sorted([post.get("username") for post in posts]))
# print()
#
#
# # Task 1: Detailed User Profiles
# # Objective: Fetch data from the /users endpoint (https://jsonplaceholder.typicode.com/users). For each user, print a detailed profile that includes their name, email, company name, and address in a nicely formatted output.
# # Challenge: Additionally, format the address to include street, suite, city, and zipcode in a single string.
# print("=" * 30)
# for post in posts:
#     print(f"Name: {post.get("name")}\nEmail: {post.get("email")}\nCompany: {post.get("company").get("name")}")
#     # print(f"Street: {post.get("address").get("street")}")
#     # print(f"Suite: {post.get("address").get("suite")}")
#     # print(f"City: {post.get("address").get("city")}")
#     # print(f"Zipcode: {post.get("address").get("zipcode")}\n")
#
#     # or
#
#     for key, value in post.get("address").items():
#         print(f"{key}: {value}")
#     print()




# '''
# Task 2: Posts and Comments Analysis
# Fetch Posts: Retrieve all posts for a specific user by their ID from the /posts endpoint. Choose any user ID between 1 to 10.
# Fetch Comments for Posts: For each post retrieved, fetch comments from the /comments endpoint filtering by the post's ID.
# Analysis: For each post, print the title, the number of comments it has received, and the email addresses of the commenters.
# Insight: Identify the post with the most comments and print its title and the total number of comments.
# '''
# user_id = 1
#
# # Fetch posts for the specified user
# posts_response = requests.get(f'https://jsonplaceholder.typicode.com/posts?userId={user_id}')
# posts = posts_response.json()
# #print(posts,'posts')
# post_comment_counts = {}
# post_commenter_emails = {}
#
# # For each post, fetch comments and perform analysis
# for post in posts:
#     comments_response = requests.get(f'https://jsonplaceholder.typicode.com/comments?postId={post["id"]}')
#     comments = comments_response.json()
#
#     post_comment_counts[post["id"]] = len(comments)
#     post_commenter_emails[post["id"]] = [comment["email"] for comment in comments]
#
#     print(f"Post Title: {post['title']}")
#     print(f"Number of Comments: {len(comments)}")
#     print(f"Commenter Emails: {', '.join(post_commenter_emails[post['id']])}\n")
#
# # Insight: Post with the most comments
# post_id_max_comments = max(post_comment_counts, key=post_comment_counts.get)
#
# max_comments = post_comment_counts[post_id_max_comments]
#
# print(f"Post with the Most Comments:")
# print(f"Post ID: {post_id_max_comments}, Number of Comments: {max_comments}")


def to_do(id: int| None = None):
    # ?userId={id}}
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos/")
    to_dos =  response.json() if response.status_code == 200 else print("Failed to retrieve data")

    to_do_items = {}

    for to_do in to_dos:
        print(to_do.get('userId'), to_do.get('completed'))
        # response = requests.get(f"https://jsonplaceholder.typicode.com/todos/?userId={id}")
        # to_dos =  response.json() if response.status_code == 200 else print("Failed to retrieve data")

    # return to_dos
pprint.pprint(to_do(1))