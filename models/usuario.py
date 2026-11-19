from abc import abstractmethod
from typing import ClassVar

from sqlalchemy.orm import validates

from app.extensions import db


class Autor(db.Model):
    __abstract__ = True

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
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(180), unique=True, nullable=False)
    contrasena = db.Column(db.String(255), nullable=False)
    nombre = db.Column(db.String(120), nullable=False)
    fechaDeAlta = db.Column(db.String(40), nullable=False)
    rango = db.Column(db.String(60), nullable=False)
    tipo_usuario = db.Column(db.String(40), nullable=False)
    reputacion = db.Column(db.Integer, nullable=True)
    nivelAdmin = db.Column(db.String(60), nullable=True)

    __mapper_args__ : ClassVar[dict] = {
        "polymorphic_identity": "usuario",
        "polymorphic_on": tipo_usuario,
    }

    def __init__(
        self,
        id: int | None,
        email: str,
        contrasena: str,
        nombre: str,
        fechaDeAlta: str,
        rango: str,
    ):
        if id is None:
            raise ValueError("El ID no puede ser nulo")
        if not email or "@" not in email:
            raise ValueError("El email debe ser válido")
        if not contrasena or not contrasena.strip():
            raise ValueError("La contraseña no puede estar vacía")

        super().__init__(nombre=nombre, fechaDeAlta=fechaDeAlta, rango=rango)
        self.id = id
        self.email = email
        self.contrasena = contrasena

    @validates("email")
    def _validar_email(self, key, value):
        if not value or "@" not in value:
            raise ValueError("El email debe ser válido")
        return value

    def generarRespuesta(self, pregunta):
        pass


class UsuarioPromedio(Usuario):
    __mapper_args__ : ClassVar[dict] = {
        "polymorphic_identity": "promedio",
    }

    def __init__(
        self,
        id: int | None,
        email: str,
        contrasena: str,
        nombre: str,
        fechaDeAlta: str,
        rango: str,
        reputacion: int = 0,
    ):
        super().__init__(
            id=id,
            email=email,
            contrasena=contrasena,
            nombre=nombre,
            fechaDeAlta=fechaDeAlta,
            rango=rango,
        )
        self.reputacion = reputacion


class Administrador(Usuario):
    __mapper_args__ : ClassVar[dict] = {
        "polymorphic_identity": "administrador",
    }

    def __init__(
        self,
        id: int | None,
        email: str,
        contrasena: str,
        nombre: str,
        fechaDeAlta: str,
        rango: str,
        nivelAdmin: str = "Moderador",
    ):
        super().__init__(
            id=id,
            email=email,
            contrasena=contrasena,
            nombre=nombre,
            fechaDeAlta=fechaDeAlta,
            rango=rango,
        )
        self.nivelAdmin = nivelAdmin
