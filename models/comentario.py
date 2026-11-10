class Comentario: 
    def __init__(self, id: int, texto: str, fecha: str, autor=None):
        
        if texto is None or not texto.strip():
            raise ValueError("El texto del comentario no puede estar vacío")

        self.id = id
        self.texto = texto
        self.fecha = fecha
        self.autor = autor