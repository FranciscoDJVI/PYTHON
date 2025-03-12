import reflex as rx

# Componentes
from components.primary_button import primary_button


class Producst(rx.State):
    
    data: list[str] = [
        [1,"laptop", 2000, 1000],
        [2,"mouse",32000, 1000],
        [3,"teclado",42000, 1000],
    ]

    columns: list[str] = ["id", "nombre", "precio", "stock"]

    # Varible para gaurdar la informacion escrita en el input
    search_query: str = ""

    # lista donde se guardaran los datos para mostrar.
    search_result: list[dict]=[]

    @rx.event
    def view(self):
        
        self.search_result = [
            {"id":item[0],"nombre":item[1], "precio":item[2], "stock":item[3]}
            for item in self.data
            if self.search_query.lower() in str(item[1].lower())
        ]
        print(self.search_result)
        
    def handle_summit(self, form_data:dict):
        self.search_query = form_data["search_query"]
        
def search() ->rx.Component:
    return rx.form(
        rx.flex(
            rx.input(
                type="text",
                placeholder="Escibe aqui",
                value=Producst.search_query,
                on_change=Producst.set_search_query,
                name="search_query"
            ),
            primary_button(
                "Buscar",
                "submit",
                Producst.view
            ),
            rx.card(
                rx.data_table(
                    data=Producst.search_result,
                    columns=Producst.columns,
                )
            ),
            spacing="4",
            wrap="wrap",
            justify="center",
            align="center",
            direction="column"
        )
    )