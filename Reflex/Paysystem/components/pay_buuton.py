import reflex as rx

def pay_button(title: str) -> rx.Component:
    return rx.button(
        title,
        variant="solid",
    )

