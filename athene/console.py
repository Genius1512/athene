from pygments import highlight
from rich.console import Console
from rich.theme import Theme
from rich.style import Style


theme = Theme({
    "error": Style(
        color="red",
        bold=True
    ),
    "standard": Style(
        color="white"
    )
})

console = Console(theme=theme, highlight=False)