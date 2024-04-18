from pprint import pprint
from types import NoneType
from bs4 import BeautifulSoup
import pandas as pd
import requests


def get_hokey_data(num):
    response = requests.get(
        f"https://www.scrapethissite.com/pages/forms/?page_num={num}"
    )
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")
    teams = soup.find_all("tr", class_="team")

    (
        team_name,
        year,
        wins,
        losses,
        overtime_losses,
        win_percentage,
        goals_for,
        goals_against,
        diff_text_success,
    ) = [[] for _ in range(9)]

    for team in teams:
        team_name.append(team.find("td", class_="name").text.strip())
        year.append(int(team.find("td", class_="year").text.strip()))
        wins.append(int(team.find("td", class_="wins").text.strip()))
        losses.append(int(team.find("td", class_="losses").text.strip()))
        overtime_losses.append(int(team.find("td", class_="ot-losses").text.strip()))

        # Negative decimals return type None
        win_percentage.append(
            team.find("td", class_="pct text-success").text.strip() or 0
        )

        goals_for.append(int(team.find("td", class_="gf").text.strip()))
        goals_against.append(int(team.find("td", class_="ga").text.strip()))

        # Negative decimals return type None
        diff_text_success.append(
            team.find("td", class_="diff text-success").text.strip() or 0
        )

    df = pd.DataFrame(
        {
            "team_name": team_name,
            "year": year,
            "wins": wins,
            "losses": losses,
            "overtime_losses": overtime_losses,
            "win_percentage": win_percentage,
            "goals_for": goals_for,
            "goals_against": goals_against,
            "diff_text_success": diff_text_success,
        }
    )


for page in range(1, 100):
    get_hokey_data(page)
