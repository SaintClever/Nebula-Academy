from collections import Counter
from pprint import pprint
from bs4 import BeautifulSoup
import requests
import pandas as pd


def get_quotes(page_numbers: int = 1):
    response = requests.get(f"https://quotes.toscrape.com/page/{page_numbers}/")
    html_content = response.text

    # Parse the HTML
    soup = BeautifulSoup(html_content, "html.parser")

    # Print the prettified HTML
    # print(soup.prettify())

    # Find the title tag
    # title_tag = soup.find("title")
    # print(title_tag)

    quotes = soup.find_all("div", class_="quote")

    data = []

    for quote in quotes:
        quotes_ = quote.find("span", class_="text").text.casefold()
        authors_ = quote.find("small", class_="author").text.casefold()
        tags_ = ", ".join(
            quote.find("div", class_="tags")
            .text.replace("\n", " ")
            .replace("Tags:", "")
            .strip()
            .split()
        )

        data.append({"quotes": quotes_, "authors": authors_, "tags": tags_})

    # print(quotes_)
    # print(authors_)
    # print(tags_)

    df = pd.DataFrame(data)
    # print(df)
    # print()

    most_common_word = Counter(" ".join(df.get("quotes")).split())
    print(
        f"The most commonly used word from page(s) {page_numbers} in a qoute is: {most_common_word.most_common(1)[0][0]!r}"
    )

    most_frequently_quoted = df.get("authors")
    print(
        f"The most frequently quoted author from page(s) {page_numbers} is: {Counter(most_frequently_quoted).most_common(1)[0][0]!r}"
    )

    print()

    return {"common_word": most_common_word, "common_author": most_frequently_quoted}


common_words = [
    Counter(get_quotes(i).get("common_word")).most_common(1)[0][0] for i in range(1, 11)
]
common_authors = [
    Counter(get_quotes(i).get("common_author")).most_common(1)[0][0]
    for i in range(1, 11)
]

print("==== Most Common Word and Author in general ====")
pprint(
    {
        "most_common_word": Counter(common_words).most_common(1)[0],
        "most_common_author": Counter(common_authors).most_common(1)[0],
    }
)
print()

print("==== Most common Words and Authors by page ====")
pprint(
    {
        "most_common_words_by_page": common_words,
        "most_common_authors_by_page": common_authors,
    }
)
print()
