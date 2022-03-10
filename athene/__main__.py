from sys import argv

from console import *
import data


def get_help(action: str = "all"):
    pass


def main(args):
    try:
        if args[1] == "data":
            console.print("Data")

        elif args[1] == "help":
            console.print("Help")
            try:
                get_help(args[2])
            except IndexError:
                get_help()

        else:
            console.error("Invalid action")

    except IndexError:
        console.error("Not enough arguments")


if __name__ == "__main__":
    main(argv)
