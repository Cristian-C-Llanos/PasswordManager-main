import sqlite3

class DataLayer:
    def __init__(self):
        # Base de datos en memoria (puedes cambiar ":memory:" a un archivo si deseas persistencia)
        self.connection = sqlite3.connect(":memory:", check_same_thread=False)
        self._initialize_database()

    def _initialize_database(self):
        """Crea la tabla para almacenar las contraseñas."""
        with self.connection as conn:
            conn.execute("""
                CREATE TABLE passwords (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    service TEXT NOT NULL,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL -- Aquí se almacenarán contraseñas encriptadas
                )
            """)

    def add_password(self, service: str, username: str, password: str):
        """Agrega una nueva contraseña encriptada."""
        with self.connection as conn:
            conn.execute("""
                INSERT INTO passwords (service, username, password)
                VALUES (?, ?, ?)
            """, (service, username, password))

    def get_passwords(self):
        """Obtiene todas las contraseñas de la base de datos."""
        with self.connection as conn:
            rows = conn.execute("SELECT id, service, username, password FROM passwords").fetchall()
            return [
                {"id": row[0], "service": row[1], "username": row[2], "password": row[3]}
                for row in rows
            ]

    def update_password(self, password_id: int, new_password: str):
        """Actualiza la contraseña por ID en la base de datos."""
        with self.connection as conn:
            conn.execute("""
                UPDATE passwords
                SET password = ?
                WHERE id = ?
            """, (new_password, password_id))

    def delete_password(self, password_id: int):
        """Elimina una contraseña por ID."""
        with self.connection as conn:
            conn.execute("""
                DELETE FROM passwords
                WHERE id = ?
            """, (password_id,))
