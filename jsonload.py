import json
with open("UniboRoboData.json", "r") as f:
    a = json.load(f)
    a["head_sensor"] =True
    print(a)