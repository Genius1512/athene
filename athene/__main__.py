# imports
from sys import argv
from rich import print
import beamer
import timetable as tt
import getmenu
import data
import uvicorn
from os import system


# dict for help texts
help = {
    "data": """Get a user's profile information: athene data get <identifier>
      Search for a given term: athene data search <term>
      Launch API on <ip> <port>: athene data api <ip> <port>; defaults: 127.0.0.1 and 8000
""",
    "timetable": """Alternative: tt; Get timetable of given class: athene timetable <class>
""",
    "menu": """Get todays menu in the canteen: athene menu
""",
    "hashgrabber": """Start api server to catch data by hash_one_liner.txt
"""
}


# function to get help page
def get_help(operation: str = "all"):
    if operation == "all":
        for i in help:
            print(f"{i}: {help[i]}")
    else:
        try:
            print(f"{operation}: {help[operation]}")
        except KeyError:
            print("[red]Invalid operation[/red]")


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

            else:
                print(f"[red]Invalid operation '{args[2]}'[/red]")

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

        elif args[1] == "help":
            try:
                get_help(args[2])
            except IndexError:
                get_help()

        else:
            print(f"[red]Invalid operation '{args[1]}'[/red]")

    except IndexError:
        print(
            "[red][Main]: Not enough arguments[/red]"
        )  # any command has not enough arguments to perform its operation


def main(args):
    if len(args) == 1:
        while True:
            command = input("> ")
            if command == "exit":
                break
            elif command == "clear":
                system("cls")
            command = ["foo"] + command.split(" ")
            run(command)
    else:
        run(args)


if __name__ == "__main__":
    main(argv)
