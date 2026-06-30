# Tema: Modulos y manejo de errores
# Bloque 00 Python
# Teoria de referencia: apuntes.md (misma carpeta)

import math
from math import pi
import random

# Ejercicio 1: importa el modulo math e imprime la raiz cuadrada de 81 con math.sqrt()
print(math.sqrt(81))

# Ejercicio 2: usando 'from math import', importa solo pi e imprimelo (sin poner math. delante)
print(pi)

# Ejercicio 3: importa random e imprime un numero al azar entre 1 y 6 con random.randint()
print(random.randint(1, 6))

# Ejercicio 4: importa random y elige al azar un elemento de la lista ["cara", "cruz"] con random.choice()
print(random.choice(["cara", "cruz"]))

# Ejercicio 5: mete int("hola") dentro de un try; en el except, imprime "Eso no es un numero"
try:
    print(int("Hola"))
except ValueError:
    print("Eso no es un número válido")

# Ejercicio 6: intenta dividir 10 / 0 dentro de un try; captura el ZeroDivisionError e imprime "No se puede dividir entre cero"
try:
    print(10 / 0)
except ZeroDivisionError:
    print("No se puede dividir entre cero")

# Ejercicio 7: pide un numero con input() dentro de un try,
# convierte a int e imprime su doble; si el usuario mete una letra,
# captura el ValueError e imprime "Tienes que escribir un numero"
try:
    numero = int(input("Digite un número: "))
    print(numero * 2)
except ValueError:
    print("Tienes que escribir un número.")

# Ejercicio 8: crea un diccionario {"ana": 30};
# dentro de un try intenta acceder a la clave "pepe" (que no existe);
# captura el KeyError e imprime "Esa clave no existe"
persona = {"ana": 30}
try:
    persona["pepe"]
except KeyError:
    print("Esa clave no existe")

# Ejercicio final: pide dos numeros al usuario con input() y divide el primero entre el segundo;
# controla con try/except DOS errores posibles: que metan una letra (ValueError) y que el segundo sea cero (ZeroDivisionError),
# con un mensaje distinto para cada uno
try:
    num1 = int(input("Digite un número: "))
    num2 = int(input("Digite otro número: "))

    print(num1 / num2)
except ValueError:
    print("Debes escribir un número.")
except ZeroDivisionError:
    print("Debes escribir un número que no sea cero.")
