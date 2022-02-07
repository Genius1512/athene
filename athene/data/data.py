import json
import os
import requests as req

import sys
sys.path.append("../athene")
from athene.console import console

data = json.loads(req.get("https://genius1512.github.io/athene/files/data.json").text)
# when getting profile
def get(identifier: str):
    new_data = (
        data["teachers"] if 3 <= len(identifier) <= 4 else data["students"]
    )  # teacher or student?

    if identifier in new_data:
        console.print(f"{identifier}'s profile:", style="standard")
        for attribute in new_data[identifier]:
            console.print(f"    {attribute}: {new_data[identifier][attribute]}", style="standard")


def search(term: str):
    # search through teachers
    had_output = False
    for key in data["teachers"]:
        if (
            term in key
            or term in data["teachers"][key]["id"]
            or term in data["teachers"][key]["name"]
            or term in data["teachers"][key]["hash"]
        ):
            had_output = True
            console.print(key, style="standard")
    # search through students
    for key in data["students"]:
        if (
            term in key
            or term in data["students"][key]["id"]
            or term in data["students"][key]["name"]
            or term in data["students"][key]["hash"]
            or term in data["students"][key]["class"]
        ):
            had_output = True
            console.print(key, style="standard")

    if not had_output:
        console.print("No profiles matched your search", style="warning")
