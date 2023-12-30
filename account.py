import json
from calculator import random_string
import os
def login(username, password):
    accounts = json.loads(open("accounts.json").read())
    for account in accounts:
        if account[0] == username and account[1] == password:
            return True
    return False
def signup(username, password):
    accounts = json.loads(open("accounts.json").read())
    accounts.append([username, password, random_string(40)])
    open("accounts.json", "w").write(json.dumps(accounts))
    return True
def remove(username,password):
    accounts = json.loads(open("accounts.json").read())
    for account in accounts:
        if account[0] == username and account[1] == password:
            accounts.remove(account)
            open("accounts.json", "w").write(json.dumps(accounts))
            os.remove("profiles/" + account[0] + ".png")
            return True
    return False
def name_check(username):
    accounts = json.loads(open("accounts.json").read())
    for account in accounts:
        if account[0] == username:
            return False
    return True
def gettoken(name,password):
    accounts = json.loads(open("accounts.json").read())
    for account in accounts:
        if account[0] == name and account[1] == password:
            return account[2]
    return False
def getdatatoken(token):
    accounts = json.loads(open("accounts.json").read())
    for account in accounts:
        if account[2] == token:
            return account
    return False
def addmessage(token, message):
    posts = json.loads(open("post.json").read())
    posts.append({"post": message, "who": getdatatoken(token)[0]})
    open("post.json", "w").write(json.dumps(posts))

            