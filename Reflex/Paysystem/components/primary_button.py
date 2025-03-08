import reflex as rx


def primary_button(title: str, type: str, action) -> rx.Component:
    return rx.button(
        title,
        variant="surface",
        type=type,
        on_click=action
    )
