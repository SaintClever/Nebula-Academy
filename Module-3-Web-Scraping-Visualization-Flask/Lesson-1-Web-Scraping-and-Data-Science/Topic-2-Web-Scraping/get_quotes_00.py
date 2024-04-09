from collections import Counter
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

    quotes_ = []
    authors_ = []
    tags_ = []

    for quote in quotes:
        quotes_.append(quote.find("span", class_="text").text)
        authors_.append(quote.find("small", class_="author").text)
        tags_.append(
            ", ".join(
                quote.find("div", class_="tags")
                .text.replace("\n", " ")
                .replace("Tags:", "")
                .strip()
                .split()
            )
        )

    # print(quotes_)
    # print(authors_)
    # print(tags_)

    data = {"quotes": quotes_, "authors": authors_, "tags": tags_}
    df = pd.DataFrame(data)
    print(df)
    print()

    most_common_word = Counter(" ".join(df.get("quotes")).split())
    print(
        f"The most commonly used word from page(s) {page_numbers} in a qoute is: {most_common_word.most_common(1)[0][0]!r}"
    )

    most_frequently_quoted = df.get("authors")
    print(
        f"The most frequently quoted author from page(s) {page_numbers} is: {Counter(most_frequently_quoted).most_common(1)[0][0]!r}"
    )

    print()


get_quotes(1)
