import reflex as rx


def primary_button(title: str, type: str) -> rx.Component:
    return rx.button(
        title,
        variant="classic",
        type=type,
    )
