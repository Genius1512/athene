from sys import argv
from rich import print
import beamer
import timetable as tt


def main(args):
    try:
        if args[1] == "beamer":
            beamer.remote([
                "192.168.20.141",
                "close"
            ])

        elif args[1] in ["tt", "timetable"]:
            tt.get_timetable(args[2])
        
        else:
            print(f"[red]Invalid operation '{args[1]}'[/red]")
        
    except IndexError:
        print("[red][Main]: Not enough arguments[/red]")


if __name__ == "__main__":
    main(argv)
