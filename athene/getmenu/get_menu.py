from bs4 import BeautifulSoup
import requests as req
import sys
sys.path.append("../athene")
from athene.console import console
from rich.status import Status

# TODO: Get day (as word: "Montag")

# get menu function
def get_menu(day_ind):
    if day_ind == "today":
        day_ind = 1
    # fetch site
    spinner = Status(
        status="Fetching menu...",
        spinner="aesthetic"
    )
    spinner.start()
    data = req.get("https://kanti-limmattal.sv-restaurant.ch/de/menuplan/").text
    spinner.stop()

    # cleanup
    soup = BeautifulSoup(data, features="lxml")
    todays_menu = soup.find("div", {"id": f"menu-plan-tab{day_ind}"})
    menus = todays_menu.findAll("div", {"class": "menu-item"})

    # get all menus
    console.print(f"Menu am nächsten {day_ind}\n", style="blue")
    for menu in menus:
        title = menu.find(
            "h2", {"class": "menu-title"}
        ).getText()  # get title => Spaghetti Bolognese
        description = menu.find(
            "p", {"class": "menu-description"}
        ).getText()  # get description => Spaghetti mit einer Fleischsauce
        price = (
            menu.findAll("span", {"class": "price"})[1]
            .find("span", {"class": "val"})
            .getText()
        )  # get price => 10.50

        is_vegetarian = (
            len(menu.findAll("span", {"class": "label label-vegetarian has-infobox"}))
            > 0
        )
        is_vegan = (
            len(menu.findAll("span", {"class": "label label-vegan has-infobox"})) > 0
        )
        food_type = ""
        if is_vegetarian:
            food_type = "(Vegetarisch)"
        elif is_vegan:
            food_type = "(Vegan)"

        console.print(
            f"""[blue]{title} {food_type}[/blue]

[white]{description}[/white]

[red]Price: {price}[/red]


"""
        )


if __name__ == "__main__":
    get_menu("today")
