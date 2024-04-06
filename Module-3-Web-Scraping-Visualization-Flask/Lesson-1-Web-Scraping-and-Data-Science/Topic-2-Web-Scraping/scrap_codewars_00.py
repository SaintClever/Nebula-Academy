from bs4 import BeautifulSoup
import requests
import pandas as pd


def codewars(programming_language: str):
    # Fetch the webpage
    response = requests.get(
        f"https://www.codewars.com/kata/search/{programming_language}"
    )
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

    # Find Kyus
    kyu_levels = soup.find_all("div", class_="inner-small-hex is-extra-wide")
    kyus = [
        int(kyu_level.find("span").text.replace(" kyu", "")) for kyu_level in kyu_levels
    ]

    # Find Kata names
    kata_names = soup.find_all("a", class_="ml-2")
    kata_titles = [kata_name.text for kata_name in kata_names]

    # Find Completed Katas
    kata_data = soup.find_all("span", class_="mr-0 text-ui-text-lc")
    completed = [int(data.text.replace(",", "")) for data in kata_data]

    data = {"kyu": kyus, "title": kata_titles, "completed": completed}
    df = pd.DataFrame(data)

    print(df)
    print()

    print(df.head())
    print()

    programming_language = programming_language.capitalize()
    print("=" * 10, "Based on the FIRST page Codewars.com/kata", "=" * 10)
    average_kyu = df["kyu"].mean()
    print(f"Average {programming_language} Kyu rank completed: {int(average_kyu)}")

    average_number_of_people = df["completed"].mean()
    print(
        f"Average number of people completing a {programming_language} Kata: {int(average_number_of_people):.2f}"
    )

    maximum_katas_completed = df["completed"].max()
    print(f"Maximum {programming_language} Katas completed: {maximum_katas_completed}")

    minimum_katas_completed = df["completed"].min()
    print(f"Minimum {programming_language} Katas completed: {minimum_katas_completed}")
    print()


codewars("python")
