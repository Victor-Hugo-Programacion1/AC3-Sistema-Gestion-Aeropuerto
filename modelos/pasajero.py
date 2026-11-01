from modelos.persona import Persona


class Pasajero(Persona):

    def __init__(self, nombre, identificacion,
                 numero_reserva, equipaje_kg):

        super().__init__(nombre, identificacion)

        self._numero_reserva = numero_reserva
        self._equipaje_kg = equipaje_kg

    def get_numero_reserva(self):
        return self._numero_reserva

    def get_equipaje_kg(self):
        return self._equipaje_kg

    def realizar_actividad_principal(self):
        return f"El pasajero {self._nombre} se encuentra abordando el vuelo."

    def mostrar_informacion(self):

        return (
            f"Pasajero: {self._nombre} | "
            f"ID: {self._identificacion} | "
            f"Reserva: {self._numero_reserva} | "
            f"Equipaje: {self._equipaje_kg} kg"
        )