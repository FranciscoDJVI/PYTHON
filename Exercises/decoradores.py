# No es necesario importar Credentials aquí, se pasará como un parámetro


class Decorate:
    def __init__(self, credentials_instance):
        """
        Inicializa la clase Decorate con una instancia de Credentials.

        Args:
            credentials_instance: Una instancia de la clase Credentials
                                 que contiene los datos de usuarios.
        """
        self.credentials = credentials_instance

    def sign_in(self):
        """
        Permite a un usuario iniciar sesión ingresando su nombre de usuario y contraseña.
        Utiliza el método sign_in de la instancia de Credentials.
        """
        # Delegar la autenticación a la instancia de Credentials
        return self.credentials.sign_in()

    def generate_user(self):
        """
        Genera un nuevo usuario con credenciales.
        Utiliza el método generate_user_db de la instancia de Credentials.
        """
        return self.credentials.generate_user_db()


user: str = "admin"
password: str = "1234"


# Decorador para la autenticacion del usuario
def authenticated(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return result

    return wrapper


# Decorador para darle 3 intentos de ingresar las credenciales correctas al usuario.
def login_attempts(function):
    def wrapper(*args, **kwargs):
        # Inicializamos la variable de los intentos a cero.
        attempts: int = 0
        result = False

        while attempts < 3:
            # Asignamos la funcion a la variable result para confirmar en cada bucle si es True o False.
            result = function(*args, **kwargs)
            # Si es True --> damos acceso.
            if result:
                print("Access granted...")
                break
            # Si el Fase --> negamos el acceso.
            else:
                attempts += 1
                remaining = 3 - attempts
                if (
                    remaining > 0
                ):  # --> Cuando la variable remaining llego a cero se cerrara el programa por que ha alcanzado el maximo de intentos.
                    print(f"You have {remaining} attempts, try again...")

        return result

    return wrapper


@login_attempts
@authenticated
def sign_in():
    user = input("User: ")
    password = input("Password: ")

    if user == "admin" and password == "1234":
        print("Welcome...")
        return True
    else:
        print("Access Denied...")
        return False


# Ejecuta el flujo de autenticación cuando se ejecuta el scrip
if __name__ == "__main__":
    sign_in()
