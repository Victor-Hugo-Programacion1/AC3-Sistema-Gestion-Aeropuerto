# Sistema de Gestión de Aeropuerto

## Proyecto Final - Programación I

### Integrantes

•	Víctor Hugo Zapata Flórez
•	Samuel Hernando Silva Navarro
•	Yoan Manuel Poveda Sotelo

## Descripción del Proyecto

El Sistema de Gestión de Aeropuerto es una aplicación desarrollada en Python utilizando los principios de Programación Orientada a Objetos (POO).
El sistema permite gestionar información relacionada con vuelos, pasajeros, pilotos, tripulación y aeronaves, simulando operaciones básicas que pueden presentarse dentro de un aeropuerto.
Durante el desarrollo del proyecto se implementaron conceptos como:
•	Encapsulamiento
•	Herencia
•	Clase abstracta
•	Sobrescritura de métodos
•	Polimorfismo
•	Composición
•	Excepciones personalizadas

## Objetivo

Desarrollar un sistema que permita aplicar de forma práctica los conceptos estudiados durante el módulo de Programación Orientada a Objetos, mediante la representación de un entorno aeroportuario.

## Estructura del Proyecto

AC3-Sistema-Gestion-Aeropuerto
│
├── docs
│   ├── UML_AC3_v1.mmd
│   ├── UML_AC3_v1.png
│   ├── UML_AC3_v1.svg
│   └── Documento_Decisiones_Diseno.docx
│
├── excepciones
│   ├── equipaje_excedido_error.py
│   ├── vuelo_lleno_error.py
│   └── vuelo_no_disponible_error.py
│
├── modelos
│   ├── aeropuerto.py
│   ├── avion.py
│   ├── pasajero.py
│   ├── persona.py
│   ├── piloto.py
│   ├── tripulante.py
│   └── vuelo.py
│
├── main.py
├── README.md
└── .gitignore

## Clases Implementadas

### Clase Abstracta

•	Persona

### Clases Derivadas

•	Pasajero
•	Piloto
•	Tripulante

### Clases del Sistema

•	Avion
•	Vuelo
•	Aeropuerto

### Excepciones Personalizadas

•	VueloLlenoError
•	EquipajeExcedidoError
•	VueloNoDisponibleError

## Conceptos de Programación Orientada a Objetos Aplicados

### Encapsulamiento

Los atributos de las clases fueron definidos de forma protegida mediante el uso del guion bajo (_) y se implementaron métodos de acceso cuando fue necesario.

### Herencia

Las clases:
•	Pasajero
•	Piloto
•	Tripulante
heredan de la clase abstracta Persona.

### Clase Abstracta

La clase Persona fue implementada utilizando la librería abc y define comportamientos comunes para las clases derivadas.

### Sobrescritura

Las clases derivadas implementan de manera específica los métodos:
•	realizar_actividad_principal()
•	mostrar_informacion()

### Polimorfismo

Se implementó mediante una colección heterogénea de objetos Persona recorrida utilizando un único ciclo.

### Composición

La clase Vuelo administra pasajeros, piloto, tripulación y avión, representando las relaciones de composición dentro del sistema.

### Excepciones Personalizadas

Se implementaron excepciones específicas para controlar errores propios del dominio aeroportuario.

## UML

El diagrama UML del proyecto se encuentra disponible en la carpeta:
docs/
Archivos:
•	UML_AC3_v1.png
•	UML_AC3_v1.svg
•	UML_AC3_v1.mmd

## Requisitos

•	Python 3.x
•	Visual Studio Code (opcional)
•	Git (opcional para desarrollo colaborativo)

## Ejecución

1.	Clonar el repositorio.
git clone <URL_DEL_REPOSITORIO>
2.	Ingresar al directorio del proyecto.
cd AC3-Sistema-Gestion-Aeropuerto
3.	Ejecutar el programa principal.
python main.py

## Funcionalidades Implementadas

•	Registro de vuelos.
•	Gestión de pasajeros.
•	Gestión de pilotos.
•	Gestión de tripulación.
•	Administración de aeronaves.
•	Búsqueda de vuelos.
•	Control de capacidad de vuelos.
•	Validación de peso de equipaje.
•	Manejo de excepciones personalizadas.
•	Demostración de polimorfismo.

## Estado del Proyecto

✅ Diseño finalizado
✅ UML elaborado
✅ Implementación funcional completada
✅ Excepciones personalizadas implementadas
✅ Pruebas iniciales realizadas
✅ Documentación elaborada

## Autoría

Proyecto desarrollado para la Actividad Colaborativa N.° 3 de Programación I mediante trabajo colaborativo.