import requests
import json
from os import system
import os
system("title " + "EMAIL CHANGER ")
sessionid = input("Session ID : ")
h = {
    'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US",
    "X-IG-Capabilities": "3brTvw==",
    "X-IG-Connection-Type": "WIFI",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    'Host': 'i.instagram.com',
    'Connection': 'keep-alive',
    "Cookie": "sessionid=" + sessionid
    }
r = requests.get("https://i.instagram.com/api/v1/accounts/current_user/?edit=true", headers=h)
if "pk" in r.text:
    username = json.loads(r.text)["user"]["username"]
    email = json.loads(r.text)["user"]["email"]
    print(username)
    print(email)
    ch = input("\nDo you want to change your email? (y/n): ")
    if ch=='y':
        new = input("New Email : ")
        f = ("email=" + new + "&username=" + username + "&phone_number=&biography=&external_url=&chaining_enabled=on")
        h2 = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "sessionid=" + sessionid,
        "UserAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "x-csrftoken": "ehgf0B7KvFu1Jnx13UHN7aUd40L8IHY2"
        }
        r2 = requests.post("https://www.instagram.com/accounts/edit/", data=f, headers=h2)
        if r2.status_code==200:
            print(f"Changed Email on {username} to {new}")
            input()
        else:
            print("Error")
    elif ch=='n':
        print("Bye Bye!")
    else:
        print("Wrong choice, idiot!")
else:
    print("Error")
