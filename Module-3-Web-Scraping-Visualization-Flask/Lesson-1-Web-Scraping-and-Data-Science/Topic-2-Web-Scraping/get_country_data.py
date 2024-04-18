from bs4 import BeautifulSoup
import pandas as pd
import requests


def get_countries():
    response = requests.get("https://www.scrapethissite.com/pages/simple/")
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")

    countries = soup.find_all("div", class_="col-md-4 country")
    name, capital, population, area = [[] for _ in range(4)]

    for country in countries:
        name.append(country.find("h3").text.strip())
        capital.append(country.find("span", class_="country-capital").text)
        population.append(int(country.find("span", class_="country-population").text))
        area.append(float(country.find("span", class_="country-area").text))

    dataset = pd.DataFrame(
        {"name": name, "capital": capital, "population": population, "area": area}
    )

    print(dataset)


get_countries()
