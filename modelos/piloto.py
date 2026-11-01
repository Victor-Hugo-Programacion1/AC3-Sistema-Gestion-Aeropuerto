from modelos.persona import Persona


class Piloto(Persona):

    def __init__(self, nombre, identificacion, licencia, horas_vuelo):
        super().__init__(nombre, identificacion)
        self._licencia = licencia
        self._horas_vuelo = horas_vuelo

    def get_licencia(self):
        return self._licencia

    def get_horas_vuelo(self):
        return self._horas_vuelo

    def realizar_actividad_principal(self):
        return f"El piloto {self._nombre} está dirigiendo un vuelo."

    def mostrar_informacion(self):
        return (
            f"Piloto: {self._nombre} | "
            f"ID: {self._identificacion} | "
            f"Licencia: {self._licencia} | "
            f"Horas de vuelo: {self._horas_vuelo}"
        )