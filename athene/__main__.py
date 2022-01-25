from sys import argv
from rich import print
import beamer


def main(args):
    try:
        if args[1] == "beamer":
            beamer.remote([
                "192.168.20.141",
                "close"
            ])
        
        else:
            print(f"[red]Invalid operation '{args[1]}'[/red]")
        
    except IndexError:
        print("[red][Main]: Not enough arguments[/red]")


if __name__ == "__main__":
    main(argv)
