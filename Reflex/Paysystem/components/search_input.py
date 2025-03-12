import reflex as rx

# Componentes
from components.primary_button import primary_button


# Clase que contine los productos y los metodos para buscar los productos.
class Producst(rx.State):
    data: list[str] = [
        [1, "laptop", 2000, 1000],
        [2, "mouse", 32000, 1000],
        [3, "teclado", 42000, 1000],
    ]

    columns: list[str] = ["id", "nombre", "precio", "stock"]

    columns_quatity: list[str] = ["id", "nombre", "precio", "stock", "cantidad"]
    # Varible para gaurdar la informacion escrita en el input
    search_query: str = ""

    # lista donde se guardaran los datos para mostrar.
    search_result: list[dict] = []

    search_result_with_quantity: list[dict] = []

    list_producst: list[list] = []

    @rx.event
    def view(self):
        self.search_result = [
            {"id": item[0], "nombre": item[1], "precio": item[2], "stock": item[3]}
            for item in self.data
            if self.search_query.lower() in str(item[1].lower())
        ]
        print(f"Productos individuales {self.search_result}")

    def handle_summit(self, form_data: dict):
        self.search_query = form_data["search_query"]

    quantity: int = 0

    def increment(self):
        self.quantity += 1

    def decremet(self):
        self.quantity -= 1

    def handle_quantity(self, quantity_final: int):
        self.quantity = quantity_final

    def view_prodcuts_wwith_quantity(self):
        self.search_result_with_quantity = [
            {
                "id": item[0],
                "nombre": item[1],
                "precio": item[2],
                "stock": item[3],
                "cantidad": self.quantity,
            }
            for item in self.data
            if self.search_query.lower() in str(item[1].lower())
        ]
        self.list_producst.append(self.item)
        print(self.list_producst)


def search() -> rx.Component:
    return rx.form(
        rx.flex(
            rx.input(
                type="text",
                placeholder="Escibe aqui",
                value=Producst.search_query,
                on_change=Producst.set_search_query,
                name="search_query",
            ),
            primary_button("Buscar", "submit", Producst.view),
            rx.card(
                rx.data_table(
                    data=Producst.search_result,
                    columns=Producst.columns,
                )
            ),
            rx.card(
                primary_button("+", "submit", Producst.increment),
                rx.heading(Producst.quantity),
                primary_button("-", "submit", Producst.decremet),
            ),
            rx.card(
                primary_button(
                    "agregar producto", "submit", Producst.view_prodcuts_wwith_quantity
                ),
                rx.card(
                    rx.data_table(
                        data=Producst.search_result_with_quantity,
                        columns=Producst.columns_quatity,
                    )
                ),
                
            ),  
            spacing="4",
            wrap="wrap",
            justify="center",
            align="center",
            direction="row",
        )
    )
