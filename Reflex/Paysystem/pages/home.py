import reflex as rx

# Components
from components.nabvar import nabvar
from components.primary_button import primary_button
from components.pay_buuton import pay_button
from components.search_input import table_products

from style.style import background as style


@rx.page("/", title="home", description="Principal page")
def home() -> rx.Component:
    return rx.container(
        nabvar("Bienvenido a la pagina Principal"),
        rx.hstack(
            primary_button("buscar")),
        rx.card(
            table_products(),
        ),
        rx.hstack(
            pay_button("agregar pago")
        )
    )


app = rx.App(style=style)
