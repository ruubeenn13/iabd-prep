# Tema: Unpacking (desempaquetado)
# Bloque 00 Python
# Teoria de referencia: apuntes.md (misma carpeta)


# Ejercicio 1: lista [100, 200], desempaquetar en 'primero' y 'segundo', imprimir las dos (sale 100 y 200)
numeros = [100, 200]
a, b = numeros          # unpacking: reparto los valores DE la lista en dos variables
print(a, b)


# Ejercicio 2: escribir 'a, b = [1, 2, 3]', ejecutar y leer el error; luego arreglarlo con la variable que falta (a, b, c = ...)
a, b, c = [1, 2, 3]     # 3 variables para 3 valores: cuadra. con solo 2 daria 'too many values to unpack'
print(a, b, c)


# Ejercicio 3: x = "hola", y = "adios"; intercambiarlas para que x valga "adios" e y "hola", imprimir las dos
x = "hola"
y = "adios"
x, y = y, x             # intercambio en una linea, sin variable auxiliar
print(x, y)


# Ejercicio 4: lista [10, 20, 30, 40, 50]; primer numero en 'cabeza', resto en 'cola' con estrella (sale 10 y [20, 30, 40, 50])
numeros = [10, 20, 30, 40, 50]
cabeza, *cola = numeros     # la estrella recoge todo lo que sobra en una lista
print("Cabeza: ", cabeza)
print("Cola: ", cola)


# Ejercicio 5: lista [1, 2, 3, 4, 5, 6]; primero en 'primero', ultimo en 'ultimo', medio en 'centro' (sale 1, 6 y [2, 3, 4, 5])
numeros = [1, 2, 3, 4, 5, 6]
primero, *medio, ultimo = numeros   # la estrella en medio coge lo que queda entre el primero y el ultimo
print("Primero:", primero, " | Úlimo: ", ultimo, " | Medio: ", medio)


# Ejercicio 6: personas = [["ana", 30], ["luis", 25]]; recorrer desempaquetando en 'nombre' y 'edad', imprimir ambos (sale ana 30, luis 25)
personas = [["ana", 30], ["luis", 25]]
for nombre, edad in personas:   # cada elemento es una pareja; la desempaqueto en el propio for
    print(nombre, edad)


# Ejercicio 7: colores = ["rojo", "verde", "azul"]; recorrer con enumerate, imprimir posicion y color (sale 0 rojo, 1 verde, 2 azul)
colores = ["rojo", "verde", "azul"]
for indice, color in enumerate(colores):    # enumerate da (posicion, valor) en cada vuelta, numerando desde 0
    print(indice, color)


# Ejercicio 8: dict {"sol": 3, "luna": 4, "mar": 3}; recorrer con .items() desempaquetando en 'palabra' y 'longitud' (sale sol 3, luna 4, mar 3)
palabras = {"sol": 3, "luna": 4, "mar": 3}
for palabra, longitud in palabras.items():  # .items() da las parejas (clave, valor) del diccionario
    print(palabra, longitud)


# Ejercicio final: alumnos = [["ana", [8, 9]], ["luis", [5, 7]]]; recorrer desempaquetando en 'nombre' y 'notas', imprimir nombre y notas
alumnos = [["ana", [8, 9]], ["luis", [5, 7]]]
for nombre, notas in alumnos:   # cada elemento es nombre + una lista de notas (una lista dentro de otra)
    print(nombre, notas)
