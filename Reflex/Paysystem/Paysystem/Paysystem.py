import reflex as rx
from rxconfig import config

# Pages
from pages.home import home


class State(rx.State):
    """The app state."""

    ...


app = rx.App()
app.add_page(home)
