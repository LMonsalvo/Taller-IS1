class Reporte:
    def __init__(self, id: int, motivo: str, estado: str = "pendiente",
                 usuario=None, publicacion=None):
        self.id = id
        self.motivo = motivo
        self.estado = estado
        self.usuario = usuario
        self.publicacion = publicacion
        self.revisor = None

    def asignar_revisor(self, administrador):
        self.revisor = administrador
        self.estado = "en revision"