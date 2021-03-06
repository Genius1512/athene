import sys

import requests as req
from bs4 import BeautifulSoup

sys.path.append("../athene")
from athene.console import console
from rich.status import Status


def get_timetable(cl):
    # get data
    spinner = Status(
        status="Fetching timetable...",
        spinner="dots"
    )
    spinner.start()
    resp = req.get(f"https://kslzh.ch/index.php?pid=116&t={cl}")
    spinner.stop()

    soup = BeautifulSoup(resp.text, features="lxml")

    table = soup.select("table")[0]
    rows = table.findAll("tr")

    times = []
    for row in rows:
        if not "Montag" in str(row):
            time = row.findAll("th")[0].getText().split("–")[0]
            times.append(time)
    times = [" " * 9, " " * 9] + times

    timetable = []
    for row in rows:
        foo = []
        subjects = row.findChildren("td")
        for subject in subjects:
            foo.append(subject.getText())
        timetable.append(foo)

    string = ""
    for day in [
        "[cyan]Montag[/cyan]",
        "[cyan]Dienstag[/cyan]",
        "[cyan]Mittwoch[/cyan]",
        "[cyan]Donnerstag[/cyan]",
        "[cyan]Freitag[/cyan]",
    ]:
        while len(day) <= 29:
            day += " "
        string += day
    string += "\n"

    for row in timetable:
        for column in row:
            while len(column) <= 16:
                column += " "
            string += f"[blue]{column}[/blue]"
        string += "\n"

    string = string.split("\n")

    for s in range(len(string)):
        try:
            console.print(f"{times[s]}  {string[s]}")
        except IndexError:
            pass


if __name__ == "__main__":
    get_timetable("W3a")
