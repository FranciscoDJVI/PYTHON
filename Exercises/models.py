# clases para cada tipo de usuario.
class User:
    """
    Clase que representa a un usuario con nombre, apellido y edad.
    """
    def __init__(self, user_name="", user_lastname="", user_age=0):
        """
        Inicializa un nuevo usuario.
        
        Args:
            user_name (str): Nombre del usuario
            user_lastname (str): Apellido del usuario
            user_age (int): Edad del usuario
        """
        self.user_name = user_name
        self.user_lastname = user_lastname
        self.user_age = user_age if isinstance(user_age, int) else 0
    
    def __str__(self):
        """
        Devuelve una representación en cadena del usuario.
        """
        return f"Usuario: {self.user_name} {self.user_lastname}, Edad: {self.user_age}"
    
    def __repr__(self):
        """
        Devuelve una representación del objeto para depuración.
        """
        return f"User(user_name='{self.user_name}', user_lastname='{self.user_lastname}', user_age={self.user_age})"
    
    def get_full_name(self):
        """
        Devuelve el nombre completo del usuario.
        """
        return f"{self.user_name} {self.user_lastname}"
    
    def update_info(self, user_name=None, user_lastname=None, user_age=None):
        """
        Actualiza la información del usuario.
        
        Args:
            user_name (str, optional): Nuevo nombre del usuario
            user_lastname (str, optional): Nuevo apellido del usuario
            user_age (int, optional): Nueva edad del usuario
        """
        if user_name is not None:
            self.user_name = user_name
        if user_lastname is not None:
            self.user_lastname = user_lastname
        if user_age is not None and isinstance(user_age, int):
            self.user_age = user_age

class UserDB:
    """
    Clase que almacena credenciales de usuario (nombre de usuario y contraseña).
    """
    def __init__(self, user_name_db="", user_password_db=""):
        """
        Inicializa nuevas credenciales de usuario.
        
        Args:
            user_name_db (str): Nombre de usuario para autenticación
            user_password_db (str): Contraseña del usuario
        """
        self.user_name_db = user_name_db
        self.user_password_db = user_password_db
    
    def __str__(self):
        """
        Devuelve una representación en cadena de las credenciales.
        """
        return f"UserDB: {self.user_name_db}"
    
    def __repr__(self):
        """
        Devuelve una representación del objeto para depuración.
        """
        return f"UserDB(user_name_db='{self.user_name_db}', user_password_db='****')"
    
    def validate_credentials(self, username, password):
        """
        Valida si las credenciales proporcionadas coinciden con este usuario.
        
        Args:
            username (str): Nombre de usuario a validar
            password (str): Contraseña a validar
            
        Returns:
            bool: True si las credenciales coinciden, False en caso contrario
        """
        return self.user_name_db == username and self.user_password_db == password
    
    def update_password(self, new_password):
        """
        Actualiza la contraseña del usuario.
        
        Args:
            new_password (str): Nueva contraseña
        """
        self.user_password_db = new_password
