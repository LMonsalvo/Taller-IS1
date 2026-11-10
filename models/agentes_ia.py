import random
from datetime import datetime
from estrategias_ia import Strategy

# Cuando tu compañero suba los cambios, estas importaciones conectarán automáticamente
from usuario import Autor 
from respuesta import Respuesta
from pregunta import Pregunta

class Hashtags:
    def __init__(self, tipoHash: str):
        self.tipoHash = tipoHash

class AgenteIA(Autor):
    def __init__(self, nombre: str, fechaDeAlta: str, rango: str, modelo: str, estado: str, etiqueta: str, estrategia: Strategy):
        # Inicializa la clase padre (Autor) con la firma exacta que armo tu compañero
        super().__init__(nombre=nombre, fechaDeAlta=fechaDeAlta, rango=rango)
        
        self.modelo = modelo
        self.estado = estado
        self.etiqueta = etiqueta
        self.estrategia = estrategia

    def setEstrategia(self, s: Strategy):
        self.estrategia = s

    def deberResponder(self, p: Pregunta) -> bool:
        # Verifica si el bot fue etiquetado en la pregunta (ej: "@BotAyuda")
        return self.etiqueta in p.texto

    def generarRespuesta(self, p: Pregunta) -> Respuesta:
        if self.deberResponder(p):
            # Delegamos la creacion del texto al patron Strategy
            texto_generado = self.estrategia.generadorTexto(p.texto) 
            
            # Generamos datos autocompletados para instanciar la Respuesta
            fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            id_aleatorio = random.randint(1000, 9999)
            
            return Respuesta(
                id=id_aleatorio,
                texto=texto_generado,
                fechaDePublicacion=fecha_actual,
                esAceptada=False,
                autor=self
            ) 
        
        return None