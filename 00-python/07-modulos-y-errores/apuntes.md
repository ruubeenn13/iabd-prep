# Modulos y manejo de errores

Bloque 00 Python. Apuntes de referencia de la unidad. El código de ejemplo es solo para entender cada idea. Es la última unidad de Python base, y va de dos cosas: usar código que ya viene hecho (modulos) y controlar los errores para que no te tiren el programa.

## Parte 1: Modulos

## Qué es un modulo

Un modulo es un archivo de Python lleno de funciones y herramientas ya hechas, listas para usar. En vez de programar todo desde cero, importas un modulo y aprovechas lo que trae. Python viene con muchos de serie (la libreria estandar): para matematicas, fechas, numeros aleatorios, etc.

## import: traer un modulo entero

Con `import` cargas el modulo, y luego usas sus funciones poniendo el nombre del modulo, un punto y la funcion.

```python
import math

print(math.sqrt(16))    # 4.0    raiz cuadrada
print(math.pi)          # 3.141592653589793
```

`math.sqrt` se lee "la funcion sqrt que vive dentro de math". El punto es el mismo de siempre: "algo que esta dentro de".

## from ... import: traer solo una parte

Si solo necesitas una funcion concreta, la importas directamente y la usas sin el prefijo del modulo.

```python
from math import sqrt

print(sqrt(25))    # 5.0    ya no hace falta poner math.
```

Las dos formas valen. `import math` deja claro de donde viene cada cosa (math.sqrt); `from math import sqrt` es mas corto si usas esa funcion muchas veces.

## Ejemplo con otro modulo: random

```python
import random

print(random.randint(1, 6))      # un numero al azar entre 1 y 6 (como un dado)
print(random.choice(["cara", "cruz"]))   # elige uno al azar de la lista
```

No tienes que memorizar que trae cada modulo. Lo importante es entender el mecanismo: importas y usas. Cuando necesites algo (una raiz, una fecha, un aleatorio), buscas que modulo lo hace.

## Tus propios archivos como modulos

Cualquier archivo .py tuyo puede importarse desde otro. Si tienes utilidades.py con una funcion, desde otro archivo haces `from utilidades import mi_funcion`. Asi se reparte un programa en varios archivos. Por ahora solo necesitas saber que se puede; lo usaras de verdad en proyectos mas grandes.

## Parte 2: Manejo de errores

## Qué es una excepcion

Cuando algo va mal en tiempo de ejecucion (divides entre cero, conviertes "hola" a numero, accedes a una clave que no existe), Python lanza un ERROR y, si no haces nada, el programa se corta ahi de golpe. Esos errores se llaman excepciones.

```python
numero = int("hola")    # ValueError: el programa peta aqui y no sigue
```

## try / except: atrapar el error

`try` envuelve el codigo que PODRIA fallar. `except` es el plan B: lo que se ejecuta SI falla, en vez de cortar el programa.

```python
try:
    numero = int("hola")
    print(numero)
except:
    print("Eso no es un numero valido")

# Eso no es un numero valido
```

En vez de petar, el programa entra en el except, hace lo que le digas y sigue vivo. Es la forma de controlar lo que puede salir mal sin que se caiga todo.

## Capturar un tipo de error concreto

Es mejor decir QUE error esperas, en lugar de atrapar cualquier cosa a ciegas. Pones el nombre del error despues de except.

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir entre cero")

# No se puede dividir entre cero
```

Errores comunes que te encontraras: ValueError (conversion invalida, como int("hola")), ZeroDivisionError (dividir entre cero), KeyError (clave que no existe en un diccionario), IndexError (posicion que no existe en una lista), TypeError (mezclar tipos incompatibles, como sumar texto y numero).

Atrapar el tipo concreto es mejor que un except pelado: si pones except a secas, ocultas TODOS los errores, incluso los que no esperabas, y eso esconde fallos de verdad.

## Un caso practico tipico: validar input

Lo que mas vas a usar: pedir un numero al usuario y controlar que no meta una letra.

```python
try:
    edad = int(input("Tu edad: "))
    print("El año que viene tendras", edad + 1)
except ValueError:
    print("Tienes que escribir un numero")
```

Si el usuario escribe "veinte", en vez de petar, salta el except y le avisas.

## else y finally (opcionales)

Dos anadidos al try:

```python
try:
    numero = int("42")
except ValueError:
    print("Error de conversion")
else:
    print("Todo fue bien:", numero)    # se ejecuta SOLO si no hubo error
finally:
    print("Esto se ejecuta siempre")   # haya error o no
```

`else` corre si el try salio bien. `finally` corre siempre, pase lo que pase (util para cerrar cosas). De momento con try/except te sobra; estos dos son para cuando los necesites.

## Resumen

- import modulo: carga un modulo entero; usas sus funciones con modulo.funcion().
- from modulo import funcion: trae solo esa funcion, se usa sin prefijo.
- Modulos utiles de serie: math (matematicas), random (aleatorios), y muchos mas.
- Una excepcion es un error en ejecucion que corta el programa si no lo controlas.
- try envuelve lo que puede fallar; except es el plan B si falla, y evita que el programa pete.
- Mejor capturar el error concreto (ValueError, ZeroDivisionError, KeyError, IndexError, TypeError) que un except a ciegas.
- else corre si no hubo error; finally corre siempre.
