import json
import os
from rich import print
import requests as req

data = json.loads(req.get("https://genius1512.github.io/athene/files/data.json").text)
# when getting profile
def get(identifier: str):
    new_data = (
        data["teachers"] if 3 <= len(identifier) <= 4 else data["students"]
    )  # teacher or student?

    if identifier in new_data:
        print(f"{identifier}'s profile:")
        for attribute in new_data[identifier]:
            print(f"    {attribute}: {new_data[identifier][attribute]}")


def search(term: str):
    # search through teachers
    for key in data["teachers"]:
        if (
            term in key
            or term in data["teachers"][key]["id"]
            or term in data["teachers"][key]["name"]
            or term in data["teachers"][key]["hash"]
        ):
            print(key)
    # search through students
    for key in data["students"]:
        if (
            term in key
            or term in data["students"][key]["id"]
            or term in data["students"][key]["name"]
            or term in data["students"][key]["hash"]
            or term in data["students"][key]["class"]
        ):
            print(key)
