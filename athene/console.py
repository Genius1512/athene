from rich import print


class console:
    @staticmethod
    def print(string: str):
        print(f"{string}")

    def error(string: str):
        print(f"[red]{string}[/red]")

