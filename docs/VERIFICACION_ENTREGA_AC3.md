# Verificación de Entrega AC3

## Propósito

Este registro documenta las comprobaciones mínimas realizadas sobre el proyecto Sistema de Gestión de Aeropuerto antes de su entrega final.

## Comprobaciones del proyecto

- [ ] El repositorio contiene las carpetas `modelos`, `excepciones` y `docs`.
- [ ] El archivo principal `main.py` se encuentra en la raíz del proyecto.
- [ ] El programa se ejecuta con el comando `python main.py`.
- [ ] La ejecución demuestra polimorfismo con Pasajero, Piloto y Tripulante.
- [ ] Se comprueba el registro normal de pasajeros.
- [ ] Se prueba `EquipajeExcedidoError`.
- [ ] Se prueba `VueloLlenoError`.
- [ ] Se prueba `VueloNoDisponibleError`.
- [ ] El diagrama UML está disponible en formatos MMD, PNG y SVG.
- [ ] El Documento de Decisiones de Diseño está incluido en la carpeta `docs`.
- [ ] El archivo README contiene descripción, estructura, ejecución y funcionalidades.

## Resultado esperado de la ejecución

La ejecución debe finalizar sin traceback y debe mostrar resultados para polimorfismo, registro de pasajeros, validación de equipaje, capacidad máxima del vuelo y búsqueda de vuelos.

## Alcance de esta verificación

Este archivo registra los criterios revisados y no modifica la implementación funcional del sistema.
