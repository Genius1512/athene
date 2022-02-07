from pygments import highlight
from rich.console import Console
from rich.theme import Theme
from rich.style import Style


<<<<<<< HEAD
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
=======
theme = Theme(
    {"error": Style(color="red", bold=True), "standard": Style(color="white")}
)
>>>>>>> 47729eecc8a8b1dfecfbc7330b7e25eecf9a035a

console = Console(theme=theme, highlight=False)
