import reflex as rx
from components.primary_button import primary_button

class Products(rx.State):
    data: list= [
        ["Laptop",1000, 10],
        ["Mouse", 20, 50],
        ["Teclado", 50, 30],
        ["Monitor", 300, 15],
        ["Audifonos", 100, 20],
        ["Cargador", 30, 40],
        ["Mochila", 50, 25],
        ["Impresora", 200, 10],
        ["Tablet", 400, 5],
        ["Smartphone", 600, 10],
    ]
    columns: list[str] = ["nombre", "precio", "stock"]
    
    search_query: str = ""
    search_results: list = []

    prodcuts_cant: int = 0

    def search_product(self):
        print(f"Tipo de self.data: {type(self.data)}")
        if self.data and len(self.data) > 0:
            print(f"Ejemplo de un item: {self.data[0]}")
        
        self.search_results = [
            {"nombre": item[0], "precio": item[1], "stock": item[2]}
            for item in self.data 
            if self.search_query.lower() in item[0].lower()
        ]

    def handle_submit(self, form_data):
        # Ejecutamos la búsqueda de productos con los criterios actuales
        self.search_product()
        return None

    def set_search_query(self, value):
        # Actualizamos la variable de estado con el nuevo valor del campo de búsqueda
        self.search_query = value

    def handle_summit_addition_cant_product(self):
        
        self.prodcuts_cant += 1
    
    def handle_summit_sustration_cant_product(self):
        
        self.prodcuts_cant -= 1

def table_products():
    return rx.form(
        rx.flex(
            rx.input(
                placeholder="Buscar productos",
                variant="classic",
                value=Products.search_query,
                on_change=Products.set_search_query,
                width="500hv",
                auto_complete=True,
            ),
            rx.card(
            rx.button(
                "Buscar",
                variant="solid",
                type="submit",
            ),
        ),
            spacing="4",
            direction="row",
            justify="center",
            align="center",
        ),
        rx.form(
                rx.card(
                    rx.data_table(
                        columns=Products.columns,
                        data=Products.search_results,            
                        resizable=True,                       
                        ),
                        rx.card(
                            primary_button("-", type="submit"),
                        ),
                        on_submit=Products.handle_summit_sustration_cant_product,
                    ),
                        rx.card(
                            rx.input(
                            placeholder="Cantidad",
                            variant="classic",
                            width="100hv",
                            value=Products.prodcuts_cant,
                            on_change=Products.set_prodcuts_cant,
                            ),
                        ),
                        rx.card(
                            primary_button("+", type="submit"),
                        ),
                        on_submit=Products.handle_summit_addition_cant_product,
        ),
            spacing="2",
            direction="column",
            justify="center",
            align="center",
            flex_wrap=True,
            
        on_submit=Products.handle_submit,
        )