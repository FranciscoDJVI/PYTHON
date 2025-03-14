import reflex as rx



class Products(rx.State):
    
    products_data: list[dict] = [
        {"id":1, "nombre":"laptop", "precio":2000, "stock":1000},
        {"id":1, "nombre":"mouse", "precio":2000, "stock":1000},
        {"id":1, "nombre":"teclado", "precio":2000, "stock":1000},
    ]

    columns: list[str]=["id", "nombre","precio", "stock"]

def view_products_data():
    return rx.data_table(
        data=Products.products_data,
        columns=Products.columns,
        search=True,
        resizable=True,
    )