# Labo6
Laboratorio 6 de Callbacks en Python y Funciones Lambda en Python.
# Laboratorio 6 - Principios de Informática

Universidad de Costa Rica  
Curso: Principios de Informática  
Estudiante: Kryssia Martínez  
Carne: B84636  
Profesora: Carolina Trejos  
Fecha: 2/12/2023

---

## Descripción del Proyecto

Este proyecto consiste en la implementación de dos ejercicios utilizando Python. Cada ejercicio aborda conceptos específicos, como callbacks y funciones lambda.

### Ejercicio 1: Callbacks en Python

- Archivos:
  - `datamanager.py`: Contiene la clase `RealTimeDataManager`.
  - `main.py`: Contiene el código principal para el Ejercicio 1.

- Funcionalidad:
  - Simula una gestión de eventos simple utilizando callbacks.
  - La clase `RealTimeDataManager` notifica cambios de datos en tiempo real.

### Ejercicio 2: Funciones Lambda en Python

- Archivo:
  - `calculadora.py`: Contiene funciones para operaciones matemáticas.

- Funcionalidad:
  - Extiende un menú utilizando funciones lambda para realizar operaciones matemáticas.

---

## Git y Branches

- Branches:
  - `ejercicio1`: Branch para el Ejercicio 1.
  - `ejercicio2`: Branch para el Ejercicio 2.
  - `main`: Branch principal.

- Ejemplos de Comandos Git:

  ```bash
  git clone <>
  git checkout -b ejercicio1
  git add .
  git commit -m "Agregando branch 1 para el Ejercicio 1"
  git checkout main
  git checkout -b ejercicio2
  git add .
  git commit -m "Agregando branch 2 para el Ejercicio 2"
  git checkout main
  git merge ejercicio1
  git merge ejercicio2
  git push origin main
## Resultados y Discusión

### Ejercicio 1: Callbacks en Python

- Resultados:
  - La implementación de la clase `RealTimeDataManager` permite la notificación de cambios de datos en tiempo real.
  - Los suscriptores pueden registrarse y cancelar su suscripción correctamente.
  - Se simula con éxito la actualización de datos periódicamente.

### Ejercicio 2: Funciones Lambda en Python

- Resultados:
  - Se extendió el menú de `ejecutar_operacion` utilizando funciones lambda para invocar cada operación.
  - Las operaciones de suma, resta, multiplicación y división se ejecutan correctamente.
  - Se proporcionó un menú amigable para el usuario con opciones de operación.

---

## Ramas Git

- Listado de Ramas:

  ```bash
  * ejercicio1
    ejercicio2
    main
