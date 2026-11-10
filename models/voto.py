class Voto:
    VALORES_VALIDOS = (1, -1)

    def __init__(self, idVoto: int, valor: int, usuario=None,
                 pregunta=None, respuesta=None):
        if (pregunta is None) == (respuesta is None):
            raise ValueError("El voto debe asociarse a una pregunta o a una respuesta, no a ambas ni a ninguna")
        self.idVoto = idVoto
        self.valor = valor
        self.usuario = usuario
        self.pregunta = pregunta
        self.respuesta = respuesta

    @property
    def valor(self) -> int:
        return self._valor

    @valor.setter
    def valor(self, nuevo_valor: int):
        if nuevo_valor not in self.VALORES_VALIDOS:
            raise ValueError("El valor del voto solo puede ser +1 o -1")
        self._valor = nuevo_valor