class Avion:

    def __init__(self, matricula, modelo, capacidad):
        self._matricula = matricula
        self._modelo = modelo
        self._capacidad = capacidad

    def get_matricula(self):
        return self._matricula

    def get_modelo(self):
        return self._modelo

    def get_capacidad(self):
        return self._capacidad

    def mostrar_datos(self):
        return (
            f"Matrícula: {self._matricula} | "
            f"Modelo: {self._modelo} | "
            f"Capacidad: {self._capacidad}"
        )