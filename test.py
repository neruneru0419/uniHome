import json

f = open("./Unibodata.json", "r")

unibo_data = json.load(f)
print(unibo_data)
unibo_data["user"] = "parent"
i = json.dumps(unibo_data)
print(i)