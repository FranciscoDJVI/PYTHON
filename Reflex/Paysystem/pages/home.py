import reflex as rx

# Components
from components.nabvar import nabvar
from components.pay_buuton import pay_button
from components.search_input import view_products_data
from style.style import background as style


@rx.page("/", title="home", description="Principal page")
def home() -> rx.Component:
    return rx.container(
        nabvar("PasySistem"),
        rx.card(
            view_products_data(),
        ),
    )


app = rx.App(style=style)
