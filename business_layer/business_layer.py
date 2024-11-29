from data_layer import DataLayer
from cryptography.fernet import Fernet


class BusinessLayer:
    def __init__(self):
        self.data_layer = DataLayer()
        self.key = self.load_key()

    def load_key(self):
        """Carga la clave de encriptación desde el archivo clave.key"""
        with open("clave.key", "rb") as key_file:
            return key_file.read()

    def encrypt_password(self, password: str) -> str:
        """Encripta una contraseña usando la clave de encriptación."""
        fernet = Fernet(self.key)
        return fernet.encrypt(password.encode()).decode()

    def add_password(self, service: str, username: str, password: str):
        """Encripta la contraseña antes de enviarla a la capa de datos."""
        encrypted_password = self.encrypt_password(password)
        self.data_layer.add_password(service, username, encrypted_password)

    def get_passwords(self):
        """Obtiene contraseñas encriptadas y devuelve una lista de diccionarios."""
        passwords = self.data_layer.get_passwords()
        return [
            {
                "id": password["id"],
                "service": password["service"],
                "username": password["username"],
                "password": password["password"],  # Contraseña encriptada
            }
            for password in passwords
        ]

    def update_password(self, password_id: int, new_password: str):
        """Actualiza una contraseña específica (encriptada)."""
        encrypted_password = self.encrypt_password(new_password)  # Encripta la nueva contraseña
        self.data_layer.update_password(password_id, encrypted_password)  # Llama al método de DataLayer

    def delete_password(self, password_id: int):
        """Elimina una contraseña por ID."""
        self.data_layer.delete_password(password_id)
