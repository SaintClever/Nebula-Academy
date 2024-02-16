import requests, json, pprint

response = requests.get("https://api.fbi.gov/wanted/v1/list")
# data = json.loads(response.content)
data = response.json()

# pprint.pp(data.keys())
# pprint.pp(type(data["items"]))

for i, most_wanted in enumerate(data):
    # data["items"][i]["images"]
    print(
        f"{data["items"][i]["title"]}\n{data["items"][i]["caution"]}\n{data["items"][i]["details"]}\n{data["items"][i]["files"]}"
    )
    print(225 * "=", '\n')
