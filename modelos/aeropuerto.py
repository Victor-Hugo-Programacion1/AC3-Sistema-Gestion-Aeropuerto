from excepciones.vuelo_no_disponible_error import VueloNoDisponibleError


class Aeropuerto:

    def __init__(self, nombre, ciudad):
        self._nombre = nombre
        self._ciudad = ciudad
        self._vuelos = []

    def agregar_vuelo(self, vuelo):
        self._vuelos.append(vuelo)

    def buscar_vuelo(self, codigo):

        for vuelo in self._vuelos:
            if vuelo._codigo == codigo:
                return vuelo

        raise VueloNoDisponibleError()

    def mostrar_vuelos(self):

        for vuelo in self._vuelos:
            print(vuelo.mostrar_datos())

    def cantidad_vuelos(self):
        return len(self._vuelos)
