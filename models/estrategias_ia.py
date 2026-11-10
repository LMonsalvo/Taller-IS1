from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def generadorTexto(self, prompt: str) -> str:
        pass

class Gemini(Strategy):
    def __init__(self, apiKey: str, nombreModelo: str):
        self.apiKey = apiKey
        self.nombreModelo = nombreModelo

    def generadorTexto(self, prompt: str) -> str:
        # Logica futura de conexion con API
        return f"[Gemini {self.nombreModelo}] procesando: {prompt}"

class OpenAI(Strategy):
    def __init__(self, apiKey: str, modelo: str):
        self.apiKey = apiKey
        self.modelo = modelo

    def generadorTexto(self, prompt: str) -> str:
        # Logica futura de conexion con API
        return f"[OpenAI {self.modelo}] procesando: {prompt}"

class StrategyLocal(Strategy):
    def __init__(self, rutaModelo: str, dispositivo: str):
        self.rutaModelo = rutaModelo
        self.dispositivo = dispositivo

    def generadorTexto(self, prompt: str) -> str:
        # Logica futura de modelo local
        return f"[Modelo Local {self.rutaModelo} en {self.dispositivo}] procesando: {prompt}"