# Tema: Estructuras de datos
# Bloque 00 Python
# Teoria de referencia: apuntes.md (misma carpeta)


# Ejercicio 1: lista de 4 frutas; imprimir la primera y la ultima (la ultima con indice negativo -1)
frutas = ["pera", "manzana", "plátano", "naranja"]
print(frutas[0], frutas[-1])

# Ejercicio 2: numeros = [10, 20, 30, 40, 50]; con slicing, imprimir los tres del medio (sale [20, 30, 40])
numeros = [10, 20, 30, 40, 50]
print(numeros[1:4])

# Ejercicio 3: crear una lista vacia, aniadir 3 numeros con append, imprimir su longitud con len()
numeros = []
numeros.append(10)
numeros.append(20)
numeros.append(30)
print(len(numeros))

# Ejercicio 4: colores = ["rojo", "verde", "azul"]; imprimir si "rojo" esta en la lista y si "negro" esta (True, False)
colores = ["rojo", "verde", "azul"]
print("rojo" in colores, "negro" in colores)

# Ejercicio 5: crear una tupla con 3 numeros, imprimir el segundo
numeros = (10, 20, 30)
print(numeros[1])

# Ejercicio 6: dict {nombre: edad} con 2 personas; aniadir una tercera con dict[clave] = valor; imprimir el dict
personas = {"Rubén": 20, "Sara": 18}
personas["Leo"] = 20
print(personas)

# Ejercicio 7: del dict anterior, imprimir el .get() de un nombre que NO existe (sale None)
print(personas.get("Silvia"))

# Ejercicio 8: crear un set a partir de la lista [1, 2, 2, 3, 3, 3]; imprimir (sale {1, 2, 3})
print(set([1, 2, 2, 3, 3, 3]))

# Ejercicio 9: a = {1, 2, 3}, b = {2, 3, 4}; imprimir la interseccion (a & b) y la union (a | b)
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b, a | b)

# Ejercicio final: personas = [("ana", 30), ("luis", 25)] (lista de tuplas); recorrerla y construir un dict {nombre: edad}; imprimir
personas = [("ana", 30), ("luis", 25)]
resultado = {}
for nombre, edad in personas:
    resultado[nombre] = edad

print(resultado)
