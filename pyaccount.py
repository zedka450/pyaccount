import json
import hashlib
with open("databank.json", "r") as f:
    data = json.load(f)

def hash_pwd(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()

users = data["users"]
conctdprsn = []

def updt_json():
    with open("databank.json", "w") as f:
        json.dump({"users": users}, f)

def enter(name, password):
    users[name] = hash_pwd(password)
    updt_json()

def exit(name):
    def exit(name):
        if name in conctdprsn:
            conctdprsn.remove(name)
            print(f"{name} disconnected!")
        else:
            print("Can't disconnect, user not connected.")

def connect(name, pwd):
    if name not in data["users"]:
        print("User not found")
    elif hash_pwd(pwd) != data["users"][name]:
        print("Wrong password")
    elif name in conctdprsn:
        print("Already connected")
    else:
        conctdprsn.append(name)
        print("Connected!")

def welcome(name):
    if name in conctdprsn:
        print(f"Welcome {name}!")
    else:
        print("Sorry, you’re not connected to this account.")
