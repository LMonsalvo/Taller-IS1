class Usuario: 
    def __init__(self, id: int, nombre: str, email: str):

        if not nombre or not nombre.strip():
            raise ValueError("El nombre del usuario no puede estar vacío")

        if not email or not email.strip():
            raise ValueError("El email del usuario no puede estar vacío")

        self.id = id
        self.nombre = nombre
        self.email = email