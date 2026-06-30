# Tema: Funciones
# Bloque 00 Python
# Teoria de referencia: apuntes.md (misma carpeta)


# Ejercicio 1: define una funcion 'saludar' que imprima "Hola"; llamala dos veces
def saludar():
    print("Hola")

saludar()

# Ejercicio 2: define 'saludar_a' que reciba un nombre por parametro e imprima "Hola" + ese nombre; llamala con dos nombres distintos
def saludar_a(nombre):
    print(f"Hola {nombre}")

saludar_a("Rubén")
saludar_a("Sara")
# Ejercicio 3: define 'sumar' que reciba dos numeros y los IMPRIMA sumados; llamala con 4 y 6
def sumar(num1, num2):
    print(num1 + num2)

sumar(4, 6)

# Ejercicio 4: define 'multiplicar' que reciba dos numeros y DEVUELVA (return) su producto; guarda el resultado en una variable e imprimela
def multiplicar(num1, num2):
    return num1 * num2

print(multiplicar(3, 4))

# Ejercicio 5: usando la funcion del ejercicio 4, multiplica su resultado por 10 en la misma linea e imprimelo (para ver la diferencia de return frente a print)
resultado = multiplicar(3, 5) * 10
print(resultado)

# Ejercicio 6: define 'saludar_idioma' con un parametro 'nombre' y otro 'saludo' con valor por defecto "Hola"; llamala una vez sin el saludo y otra pasando "Buenas"
def saludar_idioma(nombre, saludo="Hola"):
    print(saludo, nombre)

saludar_idioma("Rubén")
saludar_idioma("Rubén", "Buenas")

# Ejercicio 7: define 'sumar_todos' con *args que devuelva la suma de todos los numeros que le pases; pruebala con 3 numeros y luego con 5
def sumar_todos(*numeros):
    total = 0              # empiezo en 0
    for n in numeros:
        total = total + n  # en cada vuelta SUMO el numero actual al total
    return total           # devuelvo al final, FUERA del for

print(sumar_todos(1, 5, 4))
print(sumar_todos(3, 3, 2, 1, 1))

# Ejercicio 8: define 'mostrar_datos' con **kwargs que recorra los datos con .items() e imprima "clave = valor"; llamala con nombre y edad
def mostrar_datos(**datos):
    for clave, valor in datos.items():
        print(clave, "=", valor)

mostrar_datos(nombre="Ruben", edad="20")

# Ejercicio final: define 'es_par' que reciba un numero y DEVUELVA True si es par y False si no (usa return con una condicion); imprime el resultado para el 4 y para el 7
def es_par(num):
    return True if num % 2 == 0 else False

print(es_par(4))
print(es_par(7))
