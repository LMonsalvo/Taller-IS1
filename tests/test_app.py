from app import create_app
from app.extensions import db
from models.pregunta import Pregunta
from models.respuesta import Respuesta
from models.usuario import UsuarioPromedio


def test_health_endpoint():
    app = create_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    client = app.test_client()

    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_modelos_basicos():
    app = create_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.app_context():
        db.create_all()
        usuario = UsuarioPromedio(
            id=10,
            email="test_modelos_basicos@example.com",
            contrasena="123",
            nombre="Marcos",
            fechaDeAlta="2026-11-19",
            rango="Estudiante",
        )
        pregunta = Pregunta(
            id=20,
            titulo="Titulo de prueba",
            texto="Texto de prueba",
            fechaDePublicacion="2026-11-19",
            categoria="General",
            autor=usuario,
        )
        respuesta = Respuesta(
            id=30,
            texto="Respuesta de prueba",
            fechaDePublicacion="2026-11-19",
            esAceptada=False,
            autor=usuario,
            pregunta=pregunta,
        )
        respuesta.marcarComoAceptada()

        db.session.add_all([usuario, pregunta, respuesta])
        db.session.commit()

        guardada = db.session.scalars(db.select(Pregunta)).first()
        assert respuesta.esAceptada is True
        assert guardada is not None
        assert guardada.titulo == "Titulo de prueba"
        db.session.remove()
