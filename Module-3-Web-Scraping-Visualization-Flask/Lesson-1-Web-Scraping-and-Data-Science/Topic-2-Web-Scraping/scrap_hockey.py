import requests
from bs4 import BeautifulSoup
import pandas as pd


# Function to scrape data
def scrape_hockey_data():
    url = "https://www.scrapethissite.com/pages/forms/?page_num={}&per_page=100"
    all_teams = []

    # 6 pages of data
    # https://www.scrapethissite.com/pages/forms/?per_page=100
    for page in range(1, 7):
        response = requests.get(url.format(page))
        print("Fetching page:", url.format(page), "Status code:", response.status_code)
        soup = BeautifulSoup(response.text, "html.parser")
        teams = soup.find_all(class_="team")
        print("Number of teams found:", len(teams))

        for team in teams:
            extracted_data = {
                "Team Name": team.find(class_="name").get_text(strip=True),
                "Year": int(team.find(class_="year").get_text(strip=True)),
                "Wins": int(team.find(class_="wins").get_text(strip=True)),
                "Losses": int(team.find(class_="losses").get_text(strip=True)),
                "OT Losses": int(
                    team.find(class_="ot-losses").get_text(strip=True) or "0"
                ),
                "Win Percentage": float(team.find(class_="pct").get_text(strip=True)),
                "Goals For": int(team.find(class_="gf").get_text(strip=True)),
                "Goals Against": int(team.find(class_="ga").get_text(strip=True)),
                "Goal Differential": int(team.find(class_="diff").get_text(strip=True)),
            }
            all_teams.append(extracted_data)
    return pd.DataFrame(all_teams)


# Scrape the data
df_hockey = scrape_hockey_data()


# Basic Analysis
# 1. Rank teams based on win percentage in a specific year, 2010
top_teams_2010 = df_hockey[df_hockey["Year"] == 2010].sort_values(
    by="Win Percentage", ascending=False
)

# 2. Calculate average goal differential per season
average_goal_diff = df_hockey.groupby("Year")["Goal Differential"].mean()
# 3. Trend analysis for a specific team over the years
team_trend = df_hockey[df_hockey["Team Name"] == "Calgary Flames"]  # Example team

print(top_teams_2010, "top teams")
print(average_goal_diff, "avg_goal_diff")
print(team_trend[["Year", "Wins", "Goal Differential", "Win Percentage"]], "team_trend")
