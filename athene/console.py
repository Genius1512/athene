from pygments import highlight
from rich.console import Console
from rich.theme import Theme
from rich.style import Style


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
    )
})

console = Console(theme=theme, highlight=False)