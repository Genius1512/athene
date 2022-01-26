from sys import argv
from rich import print
import beamer
import timetable as tt
import getmenu
import data
import uvicorn


def main(args):
    try:
        if args[1] == "beamer":
            beamer.remote([
                "192.168.20.141",
                "close"
            ])

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
        
        else:
            print(f"[red]Invalid operation '{args[1]}'[/red]")
        
    except IndexError:
        print("[red][Main]: Not enough arguments[/red]")


if __name__ == "__main__":
    main(argv)
