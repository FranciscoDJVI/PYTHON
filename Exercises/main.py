from credentials import Credentials
from decoradores import Decorate
import decoradores

# Crea una instancia de Credentials
credentials = Credentials()

# Crea una instancia de Decorate pasándole la instancia de Credentials
decorate = Decorate(credentials)
while True:
    print("1.Crear usuario")
    print("2.Generar usuario")
    print("3.Iniciar sesion")
    print("4.Salir")

    option = input("Elije una opcion: ")

    match option:
        case "1":
            credentials.save_user()
        case "2":
            generated_data = decorate.generate_user()
            print(generated_data)
        case "3":
            decorate.sign_in()
        case "4":
            print("Saliendo del programa....")
            break
        case _:
            print("Opcion invalidad. intenta nuevamente...")
