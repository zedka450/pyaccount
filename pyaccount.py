import json
with open("databank.json", "r") as f:
    data = json.load(f)

paswrds = data["paswrdsplc"]
names = data["namesplc"]
conctdprsn = []

def updt_json():
    with open("databank.json", "w") as f:
        json.dump({
            "namesplc": names,
            "paswrdsplc": paswrds
        }, f, indent=2)

def enter(name, paswrd):
    names.append(name)
    paswrds.append(paswrd)
    updt_json()
def exit(name):
    if name in names:
        names.remove(name)
        paswrds.remove(paswrds.index(name))
        updt_json()
    else:
        print("Sorry, you are not registered in our database.")
def connect(name, paswrd):
    if name in names:
        i = names.index(name)
        if paswrds[i] == paswrd and name not in conctdprsn:
            print("Connected!")
            conctdprsn.append(name)
            return
    print("Can't connect, try to create your account or verify if you're not already connected.")
def welcome(name):
    if name in conctdprsn:
        print(f"Welcome {name}!" if name in names else f"Goodbye {name}!")
    else:
        print("Sorry, your not connected to this account.")
