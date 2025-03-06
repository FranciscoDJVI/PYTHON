import re
from models import User
from models import UserDB


class Credentials:
    def __init__(self):
        """Inicializa la clase Credentials con una lista vacía para almacenar usuarios."""
        self.users_db = []
    
    def save_user(self):
        """Crea un usuario con información básica y lo almacena en la lista de usuarios."""
        # Crear una instancia de User con los datos de entrada
        user_name = input("Nombre: ")
        user_lastname = input("Apellido: ")  # Corregido: Apelliod -> Apellido
        user_age = input("Edad: ")
        
        user_data = User(user_name, user_lastname, user_age)
        
        # Almacenar los datos del usuario en un formato más organizado
        user_info = {
            "name": user_data.user_name,
            "lastname": user_data.user_lastname,
            "age": user_data.user_age
        }
        
        # Guardar solo la información necesaria
        print(f"Usuario registrado: {user_info}")
        return user_info
    
    def generate_user_db(self):
        """Genera credenciales para un usuario y las almacena en la base de datos."""
        # Verificamos si necesitamos crear un nuevo usuario
        user_info = self.save_user()
        
        # Crear una instancia de UserDB para almacenar credenciales
        user_db = UserDB()
        
        # Generar nombre de usuario a partir de las primeras letras del nombre y apellido
        character_1 = user_info["name"][0:3]  # Corregido: chacracter_1 -> character_1
        character_2 = user_info["lastname"][0:3]  # Corregido: chacracter_2 -> character_2
        
        user_db.user_name_db = character_1 + character_2
        
        # Solicitar contraseña al usuario
        user_db.user_password_db = input(
            "cree una contraseña de max. 8 caracteres: "
        )
        
        # Crear un nuevo diccionario para este usuario específico
        new_user_db = {
            "user": user_db.user_name_db,
            "password": user_db.user_password_db,
            "info": user_info
        }
        
        # Añadir el nuevo usuario a la base de datos
        self.users_db.append(new_user_db)
        
        print(f"Usuario {new_user_db['user']} creado exitosamente")
        print(f"Usuarios en la BD: {len(self.users_db)}")
        
        return self.users_db
    
    def sign_in(self):
        """
        Permite a un usuario iniciar sesión ingresando su nombre de usuario y contraseña.
        Verifica si las credenciales ingresadas coinciden con alguna credencial guardada en users_db.
        """
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        
        # Verificar si users_db está vacío
        if not self.users_db:
            print("No hay usuarios registrados. Por favor, registre un usuario primero.")
            return False
        
        # Recorrer users_db para encontrar credenciales coincidentes
        for user in self.users_db:
            if user["user"] == username and user["password"] == password:
                print(f"Inicio de sesión exitoso. Bienvenido {username}!")
                return True
        
        # Si no se encuentra ninguna coincidencia
        print("Credenciales incorrectas. Por favor intente nuevamente.")
        return False
