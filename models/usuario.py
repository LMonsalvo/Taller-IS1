from abc import ABC

class Usuario:
    def __init__(self, id: int, email: str, contrasena: str):
        if id is None:
            raise ValueError("El ID no puede ser nulo")
        if not email or "@" not in email:
            raise ValueError("El email debe ser válido")
        if not contrasena or not contrasena.strip():
            raise ValueError("La contraseña no puede estar vacía")
            
        self.id = id
        self.email = email
        self.contrasena = contrasena

    def generar_respuesta_ip(self, pregunta):
        pass


class Autor(ABC, Usuario):
    def __init__(self, id: int, email: str, contrasena: str, nombre: str, fecha_de_alta: str, rango: str = "Principiante"):
        super().__init__(id, email, contrasena)
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        if not fecha_de_alta or not fecha_de_alta.strip():
            raise ValueError("La fecha de alta no puede estar vacía")
        
        self.nombre = nombre
        self.fecha_de_alta = fecha_de_alta
        self.rango = rango

    def generar_respuesta_ip(self, pregunta):
        pass