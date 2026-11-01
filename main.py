from modelos.aeropuerto import Aeropuerto
from modelos.avion import Avion
from modelos.vuelo import Vuelo
from modelos.pasajero import Pasajero
from modelos.piloto import Piloto
from modelos.tripulante import Tripulante

from excepciones.vuelo_lleno_error import VueloLlenoError
from excepciones.equipaje_excedido_error import EquipajeExcedidoError
from excepciones.vuelo_no_disponible_error import VueloNoDisponibleError


def main():

    aeropuerto = Aeropuerto("Aeropuerto Internacional", "Cali")

    avion1 = Avion("HK1234", "Airbus A320", 2)
    avion2 = Avion("HK5678", "Boeing 737", 3)

    vuelo1 = Vuelo("AV001", "Bogotá", avion1)
    vuelo2 = Vuelo("AV002", "Medellín", avion2)

    aeropuerto.agregar_vuelo(vuelo1)
    aeropuerto.agregar_vuelo(vuelo2)

    piloto1 = Piloto("Carlos Ruiz", "1001", "PIL-001", 5000)
    piloto2 = Piloto("Andrea Torres", "1002", "PIL-002", 3200)

    tripulante1 = Tripulante("Laura Gómez", "2001", "Auxiliar")
    tripulante2 = Tripulante("Juan Pérez", "2002", "Jefe de Cabina")

    pasajero1 = Pasajero("Pedro Díaz", "3001", "R001", 20)
    pasajero2 = Pasajero("Ana Rojas", "3002", "R002", 18)
    pasajero3 = Pasajero("Luis Mora", "3003", "R003", 30)

    vuelo1.asignar_piloto(piloto1)
    vuelo1.agregar_tripulante(tripulante1)
    vuelo1.agregar_tripulante(tripulante2)

    print("\n=== POLIMORFISMO ===")

    personas = [
        piloto1,
        tripulante1,
        pasajero1
    ]

    for persona in personas:
        print(persona.realizar_actividad_principal())

    print("\n=== REGISTRO DE PASAJEROS ===")

    try:
        vuelo1.agregar_pasajero(pasajero1)
        vuelo1.agregar_pasajero(pasajero2)

        print("Pasajeros registrados correctamente.")

    except Exception as e:
        print(e)

    print("\n=== PRUEBA EQUIPAJE EXCEDIDO ===")

    try:
        vuelo1.agregar_pasajero(pasajero3)

    except EquipajeExcedidoError as e:
        print(e)

    print("\n=== PRUEBA VUELO LLENO ===")

    pasajero4 = Pasajero("Mario López", "3004", "R004", 15)

    try:
        vuelo1.agregar_pasajero(pasajero4)

    except VueloLlenoError as e:
        print(e)

    print("\n=== BÚSQUEDA DE VUELOS ===")

    try:
        vuelo_encontrado = aeropuerto.buscar_vuelo("AV001")
        print(vuelo_encontrado.mostrar_datos())

    except VueloNoDisponibleError as e:
        print(e)

    print("\n=== PRUEBA VUELO INEXISTENTE ===")

    try:
        aeropuerto.buscar_vuelo("AV999")

    except VueloNoDisponibleError as e:
        print(e)


if __name__ == "__main__":
    main()