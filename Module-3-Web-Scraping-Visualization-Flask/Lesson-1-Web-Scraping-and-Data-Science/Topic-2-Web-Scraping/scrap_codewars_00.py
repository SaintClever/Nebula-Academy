from bs4 import BeautifulSoup
import requests
import pandas as pd


def codewars(search_item: str):
    # Fetch the webpage
    response = requests.get(f"https://www.codewars.com/kata/search/{search_item}")
    html_content = response.text

    # Parse the HTML
    soup = BeautifulSoup(html_content, "html.parser")

    # Print the prettified HTML
    # print(soup.prettify())

    # Find the title tag
    title_tag = soup.find("title")

    # Find all paragraph tags
    paragraphs = soup.find_all("p")
    for paragraph in paragraphs:
        print(paragraph.text)
    print()

    # Find elements by class name
    highlighted_texts = soup.find_all(
        "div", class_="list-item-kata bg-ui-section p-4 rounded-lg shadow-md"
    )
    for text in highlighted_texts:
        print(text.text)
    print()

    # Find links
    links = soup.find_all("a", class_="ml-2")
    for link in links:
        print(link.get("href"))
    print()

    kyu_levels = soup.find_all("div", class_="inner-small-hex is-extra-wide")
    kyus = [kyu_level.find("span").text.replace(" kyu", "") for kyu_level in kyu_levels]

    kata_names = soup.find_all("a", class_="ml-2")
    kata_titles = [kata_name.text for kata_name in kata_names]

    kata_data = soup.find_all("span", class_="mr-0 text-ui-text-lc")
    completed = [data.text for data in kata_data]

    data = {"Kyu": kyus, "Title": kata_titles, "Completed": completed}
    df = pd.DataFrame(data)

    print(df)
    print()

    print(df.head())
    print()

    print(df.max())
    print()

    print(df.min())
    print()


codewars("c#")
