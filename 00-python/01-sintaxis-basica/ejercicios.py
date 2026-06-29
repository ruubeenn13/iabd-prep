# Tema: Sintaxis basica
# Bloque 00 Python
# Teoria de referencia: apuntes.md (misma carpeta)


# Ejercicio 1: variable 'nombre' (texto) y 'edad' (numero), imprimir las dos
nombre = "Rubén"
edad = 19
print("Soy", nombre, "y tengo", edad, "años")

# Ejercicio 2: una variable de cada tipo (int, float, str, bool), imprimir el type() de cada una
num = 3
numdec = 25.4
nombre = "Rubén"
esHombre = True
print(type(num), type(numdec), type(nombre), type(esHombre))

# Ejercicio 3: a = 17, b = 5; imprimir suma, division /, division entera //, resto % y a ** 2
a = 17
b = 5
print(a + b, a / b, a // b, a % b, a ** 2)

# Ejercicio 4: texto = "42" (string); convertir a entero, sumar 8, imprimir (sale 50)
texto = "42"
print(int(texto) + 8)

# Ejercicio 5: pedir un numero con input(), convertir a entero, imprimir su doble
numero = int(input("Digita un número: "))
print(numero * 2)

# Ejercicio 6: edad = 20; imprimir edad > 18 y en otra linea edad == 18 (salen True y False)
edad = 20
print(edad > 18, edad == 18)

# Ejercicio 7: edad = 20, tiene_carnet = True; imprimir (edad >= 18 and tiene_carnet) y (edad < 18 or tiene_carnet)
edad = 20
tiene_carnet = True
print(edad >= 18 and tiene_carnet, edad < 18 or tiene_carnet)

# Ejercicio 8: nombre = "Ruben", edad = 25; f-string que imprima "Me llamo Ruben y mi edad es 25"
nombre = "Rubén"
edad = 25
print(f"Me llamo {nombre} y tengo {edad} años")

# Ejercicio final: pedir nombre y año de nacimiento (input), calcular edad (2026 - año), imprimir con f-string "Hola NOMBRE, tu edad es EDAD"
nombre = input("¿Cómo te llamas? ")
ano_nacimiento = int(input("¿En qué año naciste? "))
edad = 2026 - ano_nacimiento
print(f"Hola {nombre}, tu edad es: {edad}")
