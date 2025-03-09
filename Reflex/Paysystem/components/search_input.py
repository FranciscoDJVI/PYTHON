import reflex as rx
from components.primary_button import primary_button


class Producst(rx.State):
    
    data: list[dict]= [
        {"id":1,"nombre":"Laptop","precio": 1000, "stock":10},
        {"id":2,"nombre":"Mouse","precio": 1000, "stock":10},
        {"id":3,"nombre":"Teclado","precio": 1000, "stock":10},
        {"id":4,"nombre":"Monitor","precio": 1000, "stock":10},
        {"id":5,"nombre":"Ups","precio": 1000, "stock":10},
    ]

    columns: list[str] = ["id", "nombre", "precio", "stock"]

    individual_item: list = []
    
    def search_items(self):
        
        for item in self.data:
            self.individual_item = [{"id": item["id"],"nombre": item["nombre"],"precio": item["precio"],"stock": item["stock"],}]
        
            print(self.individual_item)
    
def views_data(item: str):
    return rx.box(
        rx.text(item),
    )

def foreache_ex():
    return rx.grid(
        rx.input(
            placeholder="buscar",
            value=Producst.search_items
        ),
        rx.card(
            primary_button("buscar", "submit", Producst.search_items)
        ),
        rx.data_table(
            data=Producst.data,
            columns=Producst.columns
        )
    )





"""
# Clase para la gestion de prodcutos.
class Products(rx.State):
    # Lista de datos para mostar.
    data: list= [
        ["Laptop",1000, 10],
        ["Mouse", 20, 50],
        ["Teclado", 50, 30],
        ["Monitor", 300, 15],
        ["Audifonos", 100, 20],
        ["Cargador", 30, 40],
        ["Mochila", 50, 25],
        ["Impresora", 200, 10],
        ["Tablet", 400,2000,5],
        ["Smartphone", 600, 10],
    ]
    # Distribucion de las columnas donde se mostrarán los datos guardados en data.
    columns: list[str] = ["nombre", "precio", "stock"]
    # Variable que guarda el nombre del producto a buscar.
    search_query: str = ""
    # Lista para guardar los datos encontrados.
    search_results: list = []

    # Funcion para la Busqueda de producto
    def search_product(self):
        # Muesta en consola el producto con todos los items.
        print(f"Tipo de self.data: {type(self.data)}")
        if self.data and len(self.data) > 0:
            print(f"Ejemplo de un item: {self.data[0]}")
        
        # Asignamos a la variable los items para mostar
        # Recorremos la lista data para verificar si existe el producto.
        self.search_results = [
            {"nombre": item[0], "precio": item[1], "stock": item[2]}
            for item in self.data 
            if self.search_query.lower() in item[0].lower()
        ]
        
        return self.search_product
    
    def handle_submit(self, form_data):
        # Ejecutamos la búsqueda de productos con los criterios actuales
        self.search_product()
        return None

    def set_search_query(self, value):
        # Actualizamos la variable de estado con el nuevo valor del campo de búsqueda
        self.search_query = value
        
# Funcion para renderizar y mostrar en pantalla los datos dentro de una tabla de datos.
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
        rx.card(
            rx.data_table(
                columns=Products.columns,
                data=Products.search_results,            
                resizable=True,                       
            ),
        ),
            spacing="2",
            direction="column",
            justify="center",
            align="center",
            flex_wrap=True,
            
        on_submit=Products.handle_submit,
        ),

# Class para la gestion de la cantidad de productos.
class Quantity(rx.State):
    
    quantity: int = 0
    
    # Funcion para incrementar de 1 en 1 el producto.
    def increment(self):
        self.quantity +=1
    # Funcion para decrementar de 1 en 1 el producto.
    def decrement(self):
        self.quantity -=1
        
# Funcion para renderizar y mostar la cantidad de produtos escogidos en pantalla.
def quantity():
    return rx.hstack(
        primary_button(
            "-",
            "submit",
            Quantity.decrement),
        rx.heading(Quantity.quantity),
        primary_button(
            "+",
            "submit",
            Quantity.increment
        ),
        spacing="4"
    )

class AddProdcut(rx.State):
    
    view_data: list = Products.search_results
    
    view_quantity: int = Quantity.quantity
    
    columns: list[str]=["nombre", "precio", "stock", "cantidad"]
    
    
def views_items():
    return rx.data_table(
        data = Products.data.append({"cantidad": Quantity.quantity})
    )

def add_products():
    return rx.form(
        rx.foreach (AddProdcut.view_data, views_items),
        primary_button("agregar prodcuto", "submit", AddProdcut.,
    )"""