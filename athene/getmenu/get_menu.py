from bs4 import BeautifulSoup
import requests as req
from rich import print
from datetime import datetime

# TODO: Get day (as word: "Montag")


def get_menu(day_ind):
    if day_ind == "today":
        day_ind = 1
    
    data = req.get("https://kanti-limmattal.sv-restaurant.ch/de/menuplan/").text

    soup = BeautifulSoup(data, features="lxml")
    todays_menu = soup.find("div", {"id": f"menu-plan-tab{day_ind}"})
    menus = todays_menu.findAll("div", {"class": "menu-item"})

    print(f"[blue]Menu am nächsten {day_ind}\n")
    for menu in menus:
        title = menu.find("h2", {"class": "menu-title"}).getText()
        description = menu.find("p", {"class": "menu-description"}).getText()
        price = menu.findAll("span", {"class": "price"})[1].find("span", {"class": "val"}).getText()

        is_vegetarian = len(menu.findAll("span", {"class": "label label-vegetarian has-infobox"})) > 0
        is_vegan = len(menu.findAll("span", {"class": "label label-vegan has-infobox"})) > 0    
        food_type = ""
        if is_vegetarian:
            food_type = "(Vegetarisch)"
        elif is_vegan:
            food_type = "(Vegan)"

        print(f"""[blue]{title} {food_type}[/blue]

[white]{description}[/white]

[red]Price: {price}[/red]


""")


if __name__ == "__main__":
    get_menu("today")