from modelos.persona import Persona


class Tripulante(Persona):

    def __init__(self, nombre, identificacion, cargo):
        super().__init__(nombre, identificacion)
        self._cargo = cargo

    def get_cargo(self):
        return self._cargo

    def realizar_actividad_principal(self):
        return f"El tripulante {self._nombre} está atendiendo pasajeros."

    def mostrar_informacion(self):
        return (
            f"Tripulante: {self._nombre} | "
            f"ID: {self._identificacion} | "
            f"Cargo: {self._cargo}"
        )