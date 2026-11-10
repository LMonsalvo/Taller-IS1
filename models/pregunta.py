class Pregunta:
    def __init__(self, id: int, titulo: str, texto: str,
                 fechaDePublicacion: str, categoria, autor=None):
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