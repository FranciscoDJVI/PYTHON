import reflex as rx

# Definición de la clase Products que gestiona el estado de la aplicación
# Esta clase hereda de rx.State, lo que permite que sus atributos sean reactivos y se actualicen automáticamente en la interfaz de usuario.
# Products maneja la lógica de búsqueda y almacenamiento de productos en la aplicación.
class Products(rx.State):
    # Datos iniciales de productos para la aplicación
    # Esta lista contiene diccionarios con información de cada producto, incluyendo:
    # - name: Nombre del producto (string)
    # - price: Precio del producto (número)
    # - stock: Cantidad disponible en inventario (número)
    data: list = [{
        "name": "Arroz",
        "price": 100,
        "stock": 10,
    }, {
        "name": "Frijol",
        "price": 200,
        "stock": 20,
    }, {
        "name": "Mazana",
        "price": 300,
        "stock": 30,
    }]
    # Definición de las columnas que se mostrarán en la tabla de resultados
    # Esta lista contiene los nombres en español que se utilizarán como encabezados en la tabla de datos
    columns: list = ["nombre", "precio", "stock"]
    # Variable para almacenar el texto de búsqueda ingresado por el usuario
    # Se inicializa como una cadena vacía y se actualiza cuando el usuario escribe en el campo de búsqueda
    search_query: str = ""
    # Lista que almacenará los resultados filtrados de la búsqueda
    # Se actualiza después de realizar una búsqueda y contiene los productos que coinciden con el criterio
    search_results: list = []

    # Método principal para realizar la búsqueda de productos
    # Este método filtra los productos según el texto ingresado en el campo de búsqueda
    def search_product(self):
        # Filtrar productos según la consulta de búsqueda
        # Añadimos print para depurar el tipo de datos en self.data
        print(f"Tipo de self.data: {type(self.data)}")
        if self.data and len(self.data) > 0:
            print(f"Ejemplo de un item: {self.data[0]}")
        
        # Realizamos la búsqueda filtrando los productos que contienen la consulta en su nombre
        # Para cada producto encontrado, creamos un nuevo diccionario con las claves en español
        # que corresponden a las columnas definidas anteriormente
        self.search_results = [
            {"nombre": item["name"], "precio": item["price"], "stock": item["stock"]} 
            for item in self.data 
            if self.search_query.lower() in item["name"].lower()
        ]

    # Manejador del evento de envío del formulario
    # Este método se ejecuta cuando el usuario hace clic en el botón de búsqueda o presiona Enter
    # Recibe los datos del formulario (aunque no los utiliza directamente) y llama al método de búsqueda
    def handle_submit(self, form_data):
        # Ejecutamos la búsqueda de productos con los criterios actuales
        self.search_product()
        # En Reflex, los manejadores de eventos deben devolver None o un objeto Events
        # Devolvemos None para indicar que no hay más acciones después de la búsqueda
        return None

    # Función para actualizar la consulta de búsqueda
    # Este método se ejecuta cada vez que el usuario escribe en el campo de búsqueda
    # Recibe el valor actual del campo y actualiza la variable search_query en el estado
    def set_search_query(self, value):
        # Actualizamos la variable de estado con el nuevo valor del campo de búsqueda
        self.search_query = value

# Función principal que crea la interfaz de usuario para la búsqueda de productos
# Esta función define la estructura y componentes del formulario de búsqueda y la tabla de resultados
def table_products():
    # Creamos un formulario que agrupará todos los elementos de la interfaz
    # El formulario permite capturar eventos de envío y gestionar los campos de entrada
    return rx.form(
        # Campo de entrada para que el usuario escriba su consulta de búsqueda
        # Este componente incluye:
        # - Un texto de marcador de posición (placeholder) que se muestra cuando el campo está vacío
        # - Una variante de estilo "classic" para la apariencia del campo
        # - Vinculación al valor actual de la consulta de búsqueda en el estado
        # - Un evento on_change que actualiza el estado cada vez que el usuario escribe
        rx.flex(
            rx.input(
                placeholder="Buscar productos",
                variant="classic",
                value=Products.search_query,
                on_change=Products.set_search_query,
                width="500hv",
            ),
        # Componente Card que contiene el botón de búsqueda
        # Utilizamos un card para agrupar y dar estilo al botón dentro del formulario
            rx.card(
            # Botón que el usuario puede presionar para iniciar la búsqueda
            # Configurado como tipo "submit" para que active el evento on_submit del formulario
            # Tiene una variante de estilo "solid" para darle un aspecto destacado
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
        # Tabla de datos que muestra los resultados de la búsqueda
        # Este componente utiliza:
        # - Las columnas definidas en el estado Products.columns como encabezados
        # - Los datos filtrados en Products.search_results como filas de la tabla
        # La tabla se actualiza automáticamente cuando cambian los resultados de búsqueda
        rx.data_table(
            columns=Products.columns,
            data=Products.search_results,
        ),
        # Evento que se activa cuando se envía el formulario (al hacer clic en el botón o presionar Enter)
        # Está vinculado al método handle_submit de la clase Products, que procesa la búsqueda
        on_submit=Products.handle_submit,
    )
