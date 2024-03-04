import pprint, random, json

# from challenges import challenges


class Competitor:
    def __init__(self, name, age, endurance, iq, location):
        self.name = name
        self.age = age
        self.endurance = endurance
        self.iq = iq
        self.location = location

    def get_competitor_info(self):
        return {
            "name": self.name,
            "age": self.age,
            "endurance": self.endurance,
            "iq": self.iq,
            "location": self.location,
        }


class Team:
    def __init__(self, team_name, *members):
        self.team_name = team_name
        self.members = members

    def get_team_info(self):
        team = [
            {
                "name": member.name,
                "age": member.age,
                "endurance": member.endurance,
                "iq": member.iq,
                "location": member.location,
            }
            for member in self.members
        ]
        return {self.team_name: team}


class Survivor:
    def __init__(self, exile_island, tribal_counsel):
        self.exile_island = exile_island
        self.tribal_counsel = tribal_counsel
        self.immunity = False

    def show_teams(self, *teams):
        team_names = " vs. ".join(
            team.team_name.title().replace("_", " ") for team in teams
        )
        return team_names

    def create_challenge(self, *teams):
        team_names = [team.team_name.title() for team in teams]
        print(team_names)

        # challenge = random.choice(challenges)
        # return challenge

        random_game = str(random.randint(0, 123))
        with open("challenges.json") as challenges:
            challenge = json.load(challenges)
            pprint.pprint(challenge[random_game])


nesta = Competitor("Nesta", 30, 75, 100, "Jamaica")
saint_clever = Competitor("Saint. Clever", 36, 65, 100, "New York")

dena = Competitor("Dena", 30, 50, 100, "New York")
sonya = Competitor("Sonya", 25, 65, 100, "New York")

frylock = Competitor("Frylock", 55, 50, 100, "South New Jersey")
meatwad = Competitor("Meatwad", 38, 100, 100, "South New Jersey")
master_shake = Competitor("Master Shake", 38, 70, 100, "South New Jersey")

team_titan = Team("titan", nesta, saint_clever)
pprint.pprint(team_titan.get_team_info())
print()

team_mighty_ducks = Team("mighty_ducks", dena, sonya)
pprint.pprint(team_mighty_ducks.get_team_info())
print()

aqua_teen_hunger_force = Team("aqua_teen_hunger_force", frylock, meatwad, master_shake)
pprint.pprint(aqua_teen_hunger_force.get_team_info())
print()

survivor = Survivor("b", "c")
print(survivor.show_teams(team_titan, team_mighty_ducks, aqua_teen_hunger_force))
print()

print(survivor.create_challenge(team_titan, team_mighty_ducks, aqua_teen_hunger_force))
