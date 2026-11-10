from abc import ABC, abstractmethod

class Autor(ABC):
    def __init__(self, nombre: str, fechaDeAlta: str, rango: str):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        if not fechaDeAlta or not fechaDeAlta.strip():
            raise ValueError("La fecha de alta no puede estar vacía")
        if not rango or not rango.strip():
            raise ValueError("El rango no puede estar vacío")
            
        self.nombre = nombre
        self.fechaDeAlta = fechaDeAlta
        self.rango = rango

    @abstractmethod
    def generarRespuesta(self, pregunta):
        pass


class Usuario(Autor):
    def __init__(self, id: int, email: str, contrasena: str, nombre: str, fechaDeAlta: str, rango: str):
        super().__init__(nombre=nombre, fechaDeAlta=fechaDeAlta, rango=rango)
        if id is None:
            raise ValueError("El ID no puede ser nulo")
        if not email or "@" not in email:
            raise ValueError("El email debe ser válido")
        if not contrasena or not contrasena.strip():
            raise ValueError("La contraseña no puede estar vacía")
            
        self.id = id
        self.email = email
        self.contrasena = contrasena

    def generarRespuesta(self, pregunta):
        pass


class UsuarioPromedio(Usuario):
    def __init__(self, id: int, email: str, contrasena: str, nombre: str, fechaDeAlta: str, rango: str, reputacion: int = 0):
        super().__init__(id=id, email=email, contrasena=contrasena, nombre=nombre, fechaDeAlta=fechaDeAlta, rango=rango)
        self.reputacion = reputacion


class Administrador(Usuario):
    def __init__(self, id: int, email: str, contrasena: str, nombre: str, fechaDeAlta: str, rango: str, nivelAdmin: str = "Moderador"):
        super().__init__(id=id, email=email, contrasena=contrasena, nombre=nombre, fechaDeAlta=fechaDeAlta, rango=rango)
        self.nivelAdmin = nivelAdmin