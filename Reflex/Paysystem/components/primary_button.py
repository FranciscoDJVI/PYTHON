import reflex as rx


def primary_button(title: str) -> rx.Component:
    return rx.button(
        title,
        variant="classic",
    )
