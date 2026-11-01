from abc import ABC, abstractmethod


class Persona(ABC):

    def __init__(self, nombre, identificacion):
        self._nombre = nombre
        self._identificacion = identificacion

    def get_nombre(self):
        return self._nombre

    def get_identificacion(self):
        return self._identificacion

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_identificacion(self, identificacion):
        self._identificacion = identificacion

    def obtener_datos(self):
        return f"Nombre: {self._nombre} | Identificación: {self._identificacion}"

    @abstractmethod
    def realizar_actividad_principal(self):
        pass

    @abstractmethod
    def mostrar_informacion(self):
        pass