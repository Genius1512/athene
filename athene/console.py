from pygments import highlight
from rich.console import Console
from rich.style import Style
from rich.theme import Theme

theme = Theme({
    "standard": Style(
        color="white"
    ),
    "success": Style(
        color="green",
        bold=True,
        underline=True
    ),
    "warning": Style(
        color="yellow"
    ),
    "error": Style(
        color="red",
        bold=True,
        underline=True
    ),
    "debug": Style(
        color="purple",
        bold=True,
        underline=True
    )
})

console = Console(theme=theme, highlight=False)
