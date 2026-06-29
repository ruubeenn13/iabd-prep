# Tema: Comprehensions
# Bloque 00 Python
# Teoria de referencia: apuntes.md (misma carpeta)


# Ejercicio 1: variable 'ciudad' con tu ciudad, mostrarla con print
ciudad = "Crevilente"   # string: el texto va siempre entre comillas
print(ciudad)


# Ejercicio 2: lista 'colores' con 3 colores, mostrar el segundo (posicion 1)
colores = ["rojo", "azul", "verde"]
# los indices empiezan en 0, asi que la posicion 1 es el SEGUNDO elemento
print(colores[1])


# Ejercicio 3: numeros = [2, 4, 6], imprimir cada uno sumando 1 (sale 3, 5, 7)
numeros = [2, 4, 6]
# la variable del bucle ('n') debe llamarse distinto a la lista ('numeros');
# si usas el mismo nombre, el bucle pisa la lista y la pierdes
for n in numeros:
    print(n + 1)


# Ejercicio 4: numeros = [1, 2, 3, 4], lista 'dobles' por 2 con for+append (sale [2, 4, 6, 8])
numeros = [1, 2, 3, 4]
dobles = []                  # lista vacia donde voy acumulando los resultados
for n in numeros:
    dobles.append(n * 2)     # append aniade cada resultado al final de la lista
print(dobles)


# Ejercicio 5: numeros = [1, 2, 3, 4], comprehension por 10 (sale [10, 20, 30, 40])
numeros = [1, 2, 3, 4]
# version corta del patron lista-vacia + for + append del ejercicio 4
print([n * 10 for n in numeros])


# Ejercicio 6: lista del 1 al 8, comprehension solo impares (sale [1, 3, 5, 7])
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
# n % 2 es el resto de dividir entre 2; si NO es 0 (!= 0), el numero es impar
print([n for n in numeros if n % 2 != 0])


# Ejercicio 7: palabras = ["sol", "luna", "estrella"], dict {palabra: longitud}
palabras = ["sol", "luna", "estrella"]
# dict comprehension: cada pareja 'clave: valor' es palabra: su longitud (len)
print({p: len(p) for p in palabras})


# Ejercicio 8: nombres = ["ana", "alba", "luis", "alex"], set de primeras letras (sale {'a', 'l'})
nombres = ["ana", "alba", "luis", "alex"]
# un set no admite repetidos: 'a' y 'l' salen una sola vez aunque varios nombres empiecen igual
print({n[0] for n in nombres})


# Ejercicio final: numeros del 1 al 10, comprehension con el cuadrado de los multiplos de 3 (sale [9, 36, 81])
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# transforma (n * n) y filtra (if multiplo de 3) en la misma linea:
# primero el if decide quien pasa, luego a ese se le eleva al cuadrado
print([n * n for n in numeros if n % 3 == 0])
