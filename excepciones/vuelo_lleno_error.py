class VueloLlenoError(Exception):

    def __init__(self, mensaje="El vuelo ha alcanzado su capacidad máxima."):
        super().__init__(mensaje)