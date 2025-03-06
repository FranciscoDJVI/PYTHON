from datetime import datetime


class Event:
    def __init__(self):
        self.event: dict = {}  # Diccionario para almacenar los eventos(nombre: fecha)
        self.list_events: list = []  # Lista de dicionarios.

    def create_event(self):
        self.name_event = input("Ingrese el nombre del evento: ")
        self.date_event = input("Ingresa la fecha del evento (dd-mm-aaaa): ")
        self.date_format = "%d-%m-%Y"

        # Comprovacion para el ingreso de la fecha en el formato correcto.
        try:
            self.date_object = datetime.strptime(self.date_event, self.date_format)
        except:
            print("Formato de fecha correcto. Use dd-mm-aaaa.")
            return

        event_data = {
            "name": self.name_event,
            "date": self.date_object,
        }  # Cracion de diccionario nuevo para cada interacion.

        # Comprovacion para los eventos existentes con fechas iguales.
        if (
            self.name_event in self.event
            and self.event[self.name_event] == self.date_object
        ):
            print(f"El evento {self.name_event} con esa fecha ya existe.😪")
            return
        # Comprovacion para evento existente con fecha diferente.
        elif self.name_event in self.event:
            print(f"El evento {self.name_event} ya existe, pero con otra fecha.")

        self.event[self.name_event] = self.date_object
        self.list_events.append(event_data)
        print(f"Evento {self.name_event} creado con èxito.")

    def view_event(self):
        # Comprovacion para poder mostrar eventos.
        try:
            if len(self.list_events) == 0:
                print("No hay enventos para mostrar")
            else:
                for index, event in enumerate(self.list_events):
                    print(f"Index:{index} --> Event:{event}")
        except:
            print("Crea algun evento, para poder mostralo")
            return

    def delete_event(self):
        # Comprovacion para poder eliminar eventos.
        try:
            if len(self.list_events) == 0:
                print("No hay eventos guardados para eliminar")
            else:
                self.index_event_delete = int(
                    input("Ingrese indice del evento a eliminar: ")
                )
                for index, event in enumerate(self.list_events):
                    if self.index_event_delete != index:
                        raise ValueError("Evento no encontrado")
                del self.list_events[index]
        except:
            print("Crea algun evento, para poder eliminar")
            return

    def update_event(self):
        # Comprovacion para poder Actualizar enventos.
        try:
            if len(self.list_events) == 0:
                print("No hay eventos guardados para Actualizar")
            else:
                self.index_event_for_update = int(
                    input("Ingrese el indice del evento a Actualizar: ")
                )
                for index, event in enumerate(self.list_events):
                    if self.index_event_for_update != index:
                        print("Evento no encontrado")
                    else:
                        del self.list_events[self.index_event_for_update]

                    self.name_event_update = input(
                        "Ingrese el nuevo nombre para el evento: "
                    )
                    self.date_event_update = input(
                        "Ingrese la nueva fecha para el evento: "
                    )

                    self.date_format = "%d-%m-%Y"

                    self.date_object = datetime.strptime(
                        self.date_event_update, self.date_format
                    )
                    # Creaccion de un nuevo diccionario para cada actuaizacion.
                    new_event = {self.name_event_update: self.date_object}
                    self.list_events.append(new_event)
            return self.list_events
        except:
            print("Crea algun evento para poder Actualizar")
            return


event = Event()

while True:
    print("-----MENU-----\n")
    print("1.Crear evento")
    print("2.Ver eventos")
    print("3.Eliminar evento")
    print("4.Actualizar evento")
    print("5.Salir\n")

    option = input("\nIngrese una opción: ")

    match option:
        case "1":
            event.create_event()
        case "2":
            event.view_event()
        case "3":
            event.delete_event()
        case "4":
            event.update_event()
        case "5":
            print("Saliendo del programa...")
            break
        case _:
            print("Opción no válida")
