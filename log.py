from datetime import datetime
Greeting = True
user = input()
if user == "child":
    username = "こども"
elif user == "parent":
    username = "りょうしん"
elif user == "grandparent":
    username = "そふぼ"
with open("./UniboLog.txt", "a") as f:
    if Greeting:
        f.write(username+"    "+datetime.now().strftime("%Y/%m/%d %H:%M:%S")+"\n「おはよう」とあいさつをしました\n")
