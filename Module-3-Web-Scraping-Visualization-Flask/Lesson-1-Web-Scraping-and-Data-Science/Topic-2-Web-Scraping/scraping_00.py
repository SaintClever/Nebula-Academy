from bs4 import BeautifulSoup
import requests

# Fetch the webpage
response = requests.get("https://www.codewars.com/")
html_content = response.text

# Parse the HTML
soup = BeautifulSoup(html_content, "html.parser")
print(soup.prettify())

# paragraphs = soup.find_all("p")
# for i, paragraphs in enumerate(paragraphs):
#     print(i + 1, paragraphs)

# print(soup.find("title").string)

links = soup.find_all("a")
for link in links:
    print(link.get("href"))

"""
Try It Yourself
1. Parse the HTML of a webpage of your choice.
2. Extract and print the text of the title tag.
3. Find and print all links (a tags) on the page
"""
