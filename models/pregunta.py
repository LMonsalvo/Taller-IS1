from app.extensions import db

# Le dice a SQLAlchemy que esta clase corresponde a la tabla "preguntas" y define
# qué columnas va a tener (clave primaria, campos obligatorios y relación con usuarios).
class Pregunta(db.Model):
    __tablename__ = "preguntas"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    texto = db.Column(db.Text, nullable=False)
    fechaDePublicacion = db.Column(db.String(40), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=True)

    # Recibe los datos al crear una Pregunta y verifica que título, texto y categoría
    # sean válidos antes de avanzar (si no, lanza ValueError).
    def __init__(
        self,
        id: int | None,
        titulo: str,
        texto: str,
        fechaDePublicacion: str,
        categoria,
        autor=None,
    ):
        if titulo is None or not titulo.strip():
            raise ValueError("El titulo de la pregunta no puede estar vacio")
        if texto is None or not texto.strip():
            raise ValueError("El texto de la pregunta no puede estar vacio")
        if categoria is None:
            raise ValueError("La pregunta debe tener una categoria")

        self.id = id
        self.titulo = titulo
        self.texto = texto
        self.fechaDePublicacion = fechaDePublicacion
        self.categoria = categoria
        self.autor = autor
        if autor is not None and getattr(autor, "id", None) is not None:
            self.usuario_id = autor.id
