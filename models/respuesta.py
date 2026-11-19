from app.extensions import db


class Respuesta(db.Model):
    __tablename__ = "respuestas"

    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.Text, nullable=False)
    fechaDePublicacion = db.Column(db.String(40), nullable=False)
    esAceptada = db.Column(db.Boolean, nullable=False, default=False)
    pregunta_id = db.Column(db.Integer, db.ForeignKey("preguntas.id"), nullable=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=True)

    def __init__(
        self,
        id: int | None,
        texto: str,
        fechaDePublicacion: str,
        esAceptada: bool = False,
        autor=None,
        pregunta=None,
    ):
        if texto is None or not texto.strip():
            raise ValueError("El texto de la respuesta no puede estar vacío")

        self.id = id
        self.texto = texto
        self.fechaDePublicacion = fechaDePublicacion
        self.esAceptada = esAceptada
        self.autor = autor
        self.pregunta = pregunta
        if autor is not None and getattr(autor, "id", None) is not None:
            self.usuario_id = autor.id
        if pregunta is not None and getattr(pregunta, "id", None) is not None:
            self.pregunta_id = pregunta.id

    def marcarComoAceptada(self):
        self.esAceptada = True
