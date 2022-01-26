from sys import argv
from rich import print as rprint
import requests


def print(arg):
    rprint("[Beamer]: " + str(arg))


def parse_key(key: str):
    try:
        return {
            "close": "3B",
            "vidmute": "3E",
            "freeze": "47",
            "voldown": "57",
            "volup": "56",

            "srcpc": "43",
            "srcvid": "46",
            "srcsvid": "45",
            "srclan": "8A",
            "srcbnc": "40",
            "srchdmi": "1D"
        }[key]
    except KeyError:
        return None


def remote(args):
    ip = args[0]
    key = parse_key(args[1])
    if key == None:
        print("Invalid key")
        return
    url = f"http://{ip}:80/cgi-bin/webconf.dll?KEY={key}"
    headers = {"Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": f"http://{ip}/cgi-bin/webconf.dll?page=13", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}

    try:
        resp = requests.get(url, headers)
    except requests.exceptions.ConnectionError:
        print("Connection failed")
        return
    print("Successfull")
    print(resp.text)


if __name__ == "__main__":
    remote(argv[1:])
