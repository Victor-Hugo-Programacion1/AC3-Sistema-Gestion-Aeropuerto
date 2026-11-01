class VueloNoDisponibleError(Exception):

    def __init__(self, mensaje="El vuelo solicitado no existe."):
        super().__init__(mensaje)
