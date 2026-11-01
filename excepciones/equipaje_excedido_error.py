class EquipajeExcedidoError(Exception):

    def __init__(self, mensaje="El peso del equipaje excede el límite permitido."):
        super().__init__(mensaje)