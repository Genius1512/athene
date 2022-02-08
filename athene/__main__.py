# imports
import sys
from sys import argv

sys.path.append("../athene")
from os import system

import uvicorn
import requests as req

import beamer
import data
import getmenu
import timetable as tt
from athene.console import console
from rich.markdown import Markdown
from rich.status import Status

# dict for help texts
help = {
    "data": """Get a user's profile information: athene data get <identifier>
      Search for a given term: athene data search <term>
      Launch API on <ip> <port>: athene data api <ip> <port>; defaults: 127.0.0.1 and 8000
      Download raw JSON data: athene data download
""",
    "timetable": """Alternative: tt; Get timetable of given class: athene timetable <class>
""",
    "menu": """Get todays menu in the canteen: athene menu
""",
    "hashgrabber": """Start api server to catch data by hash_one_liner.txt
""",
}


# function to get help page
def get_help(operation: str = "all"):
    if operation == "all":
        for i in help:
            console.print(f"{i}: {help[i]}")
    else:
        try:
            console.print(f"{operation}: {help[operation]}")
        except KeyError:
            console.print("Invalid operation", style="error")


# Entry Point
def run(args):
    try:
        if args[1] == "beamer":
            beamer.remote(["192.168.20.141", "close"])

        elif args[1] in ["tt", "timetable"]:
            tt.get_timetable(args[2])

        elif args[1] == "menu":
            getmenu.get_menu("today")

        elif args[1] == "data":
            if args[2] == "get":
                data.get(args[3])

            elif args[2] == "search":
                data.search(args[3])

            elif args[2] == "api":
                try:
                    host = args[3]
                except IndexError:
                    host = "127.0.0.1"
                try:
                    port = int(args[4])
                except IndexError:
                    port = 8000

                uvicorn.run("data.api:app", host=host, port=port)

            elif args[2] == "download":
                data.download()

            else:
                console.print(f"Invalid operation '{args[2]}'", style="error")

        elif args[1] == "hashgrabber":
            try:
                host = args[3]
            except IndexError:
                host = "127.0.0.1"
            try:
                port = int(args[4])
            except IndexError:
                port = 8000

            uvicorn.run("hashgrabber.hash_grabber:app", host=host, port=port)

        elif args[1] == "md":
            if args[2] == "contributing":
                link = "https://genius1512.github.io/athene/CONTRIBUTING.md"
            elif args[2] == "readme":
                link = "https://genius1512.github.io/athene/README.md"
            else:
                console.print("Invalid Markdown identifier", style="error")
                return
            
            spinner = Status(
            status="Fetching markdown",
            spinner="aesthetic"
            )
            spinner.start()
            resp = req.get(link).text
            spinner.stop()

            console.print(Markdown(resp))

        elif args[1] == "help":
            try:
                get_help(args[2])
            except IndexError:
                get_help()

        else:
            console.print(f"Invalid operation '{args[1]}'", style="error")

    except IndexError:
        console.print(
            "Not enough arguments", style="error"
        )  # any command has not enough arguments to perform its operation


def main(args):
    if len(args) == 1:
        while True:
            command = input("> ")
            if command == "exit":
                break
            elif command == "clear":
                system("cls")
                continue
            command = ["foo"] + command.split(" ")
            run(command)
    else:
        run(args)


if __name__ == "__main__":
    main(argv)
