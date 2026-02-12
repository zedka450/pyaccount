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
    if name in users:
        print("User alerady exists.")
    else:
        users[name] = {
            "password": hash_pwd(password),
            "data": {}
        }
        updt_json()
        print("User created successfully.")

def set_data(name, key, value):
    if name not in users:
        print("User not found")
        return
    if name in conctdprsn:
        users[name]["data"][key] = value
        updt_json()
        print(f"Data '{key}' added to user {name} successfully.")
    else:
        print("Can't add data, user is not connected")

def get_data(name, key):
    if name not in users:
        print("User not found")
        return
    if name in conctdprsn:
        return users[name]["data"].get(key, None)
    else:
        print("Can't read data, user is not connected")

def exit(name):
    if name in conctdprsn:
        conctdprsn.remove(name)
        print(f"{name} disconnected!")
    else:
        print("Can't disconnect, user not connected.")

def connect(name, pwd):
    if name not in data["users"]:
        print("User not found")
    elif hash_pwd(pwd) != data["users"][name]["password"]:
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
