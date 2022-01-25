import json
import os
from rich import print


data = json.load(open(r"C:\Users\silva\Projects\py-athene\athene\data\data\data.json", "r"))

def get(identifier: str):
    new_data = data["teachers"] if 3 <= len(identifier) <= 4 else data["students"]

    if identifier in new_data:
        print(f"""{identifier}'s profile:
    Name: {new_data[identifier]['name']}
    ID: {new_data[identifier]['id']}
    Hash: {new_data[identifier]['hash']}""")
    if not 3 <= len(identifier) <= 4:
        print(f"    Class: {new_data[identifier]['class']}")
    else:
        print("[red]Profile not found[/red]")


def search(term: str):
    for key in data["teachers"]:
        if term in key or term in data["teachers"]["id"] or term in data["teachers"]["name"] or term in data["teachers"]["hash"]:
            print(key)

    for key, data["students"] in data["students"]:
        if term in key or term in data["students"]["id"] or term in data["students"]["name"] or term in data["students"]["hash"] or term in data["students"]["class"]:
            print(key)
