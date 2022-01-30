import json
import os
from rich import print
import requests as req


data = json.loads(req.get("https://genius1512.github.io/athene/files/data.json").text)

def get(identifier: str):
    new_data = data["teachers"] if 3 <= len(identifier) <= 4 else data["students"]

    if identifier in new_data:
        print(f"{identifier}'s profile:")
        for attribute in new_data[identifier]:
            print(f"    {attribute}: {new_data[identifier][attribute]}")


def search(term: str):
    for key in data["teachers"]:
        if term in key or term in data["teachers"]["id"] or term in data["teachers"]["name"] or term in data["teachers"]["hash"]:
            print(key)

    for key, data["students"] in data["students"]:
        if term in key or term in data["students"]["id"] or term in data["students"]["name"] or term in data["students"]["hash"] or term in data["students"]["class"]:
            print(key)
