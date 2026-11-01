from excepciones.vuelo_lleno_error import VueloLlenoError
from excepciones.equipaje_excedido_error import EquipajeExcedidoError


class Vuelo:

    LIMITE_EQUIPAJE = 23

    def __init__(self, codigo, destino, avion):
        self._codigo = codigo
        self._destino = destino
        self._avion = avion
        self._pasajeros = []
        self._piloto = None
        self._tripulacion = []

    def asignar_piloto(self, piloto):
        self._piloto = piloto

    def agregar_tripulante(self, tripulante):
        self._tripulacion.append(tripulante)

    def agregar_pasajero(self, pasajero):

        if len(self._pasajeros) >= self._avion.get_capacidad():
            raise VueloLlenoError()

        if pasajero.get_equipaje_kg() > self.LIMITE_EQUIPAJE:
            raise EquipajeExcedidoError()

        self._pasajeros.append(pasajero)

    def mostrar_pasajeros(self):
        return self._pasajeros

    def mostrar_tripulacion(self):
        return self._tripulacion

    def mostrar_datos(self):

        return (
            f"Código: {self._codigo}\n"
            f"Destino: {self._destino}\n"
            f"Avión: {self._avion.get_modelo()}\n"
            f"Pasajeros registrados: {len(self._pasajeros)}"
        )
