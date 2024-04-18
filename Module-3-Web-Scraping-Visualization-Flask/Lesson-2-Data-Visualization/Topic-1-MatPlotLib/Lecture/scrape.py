import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
# Function to scrape data
def scrape_hockey_data():
    url = "https://www.scrapethissite.com/pages/forms/?page_num={}&per_page=100"
    all_teams = []

    #6 pages of data
    #https://www.scrapethissite.com/pages/forms/?per_page=100
    for page in range(1, 7):
        response = requests.get(url.format(page))
        print("Fetching page:", url.format(page), "Status code:", response.status_code)
        soup = BeautifulSoup(response.text, 'html.parser')
        teams = soup.find_all(class_="team")
        print("Number of teams found:", len(teams))
        
        for team in teams:
            extracted_data = {
                'Team Name': team.find(class_="name").get_text(strip=True),
                'Year': int(team.find(class_="year").get_text(strip=True)),
                'Wins': int(team.find(class_="wins").get_text(strip=True)),
                'Losses': int(team.find(class_="losses").get_text(strip=True)),
                'OT Losses': int(team.find(class_="ot-losses").get_text(strip=True) or '0'),
                'Win Percentage': float(team.find(class_="pct").get_text(strip=True)),
                'Goals For': int(team.find(class_="gf").get_text(strip=True)),
                'Goals Against': int(team.find(class_="ga").get_text(strip=True)),
                'Goal Differential': int(team.find(class_="diff").get_text(strip=True))
            }
            all_teams.append(extracted_data)
    return pd.DataFrame(all_teams)

# Scrape the data
df_hockey = scrape_hockey_data()


# Basic Analysis
# 1. Rank teams based on win percentage in a specific year, 2010
top_teams_2010 = df_hockey[df_hockey['Year'] == 2010].sort_values(by='Win Percentage', ascending=False)

# 2. Trend analysis for a specific team over the years
team_trend = df_hockey[df_hockey['Team Name'] == "Calgary Flames"]  # Example team

# print(top_teams_2010,'top teams')
print(team_trend[['Year', 'Wins', 'Goal Differential', 'Win Percentage']],'team_trend')

###############################################################################################################

# Visualization 

# 2. team_trend is loaded with the Calgary Flames data as per the previous assignment
plt.figure(figsize=(10, 5))
plt.plot(team_trend['Year'], team_trend['Win Percentage'], marker='o')
plt.title("Calgary Flames - Win Percentage Over Years")
plt.xlabel("Year")
plt.ylabel("Win Percentage")
plt.grid(True)
plt.savefig('winPercentage.png')

#2.2 Bar charts for categorical data
# plt.figure(figsize=(24, 24))
# plt.bar(top_teams_2010['Team Name'], top_teams_2010['Win Percentage'])
# plt.title("Win Percentage of NHL Teams in 2010")
# plt.xlabel("Team Name")
# plt.xticks(rotation=90)  # Rotate team names for better visibility
# plt.ylabel("Win Percentage")
# plt.show()


# 3. advanced Goal Differentials
# plt.figure(figsize=(10, 6))
# plt.scatter(df_hockey['Goals For'], df_hockey['Goals Against'], c=df_hockey['Goal Differential'], cmap='coolwarm', s=100)
# plt.colorbar(label='Goal Differential')  # Adds a color bar to indicate goal differential
# plt.title("Goal For vs. Goal Against (Colored by Goal Differential)")
# plt.xlabel("Goals For")
# plt.ylabel("Goals Against")
# plt.grid(True)
# plt.show()