import json

with open("mtjs-cars.json") as jsf:
    data = json.load(jsf)

for key in data["Cars"]:
    del key["drat"]

with open("new-cars.json", "w") as f:
    json.dump(data, f, indent=2)

