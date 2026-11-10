class Respuesta: 
    def __init__(self, id: int, texto: str, fechaDePublicacion: str, esAceptada: bool, autor=None ):
        
        if texto is None or not texto.strip(): 
            raise ValueError("El texto de la respuesta no puede estar vacío")

        self.id = id
        self.texto = texto
        self.fechaDePublicacion = fechaDePublicacion
        self.esAceptada = esAceptada
        self.autor = autor

    def marcarComoAceptada(self):
        self.esAceptada = True

        