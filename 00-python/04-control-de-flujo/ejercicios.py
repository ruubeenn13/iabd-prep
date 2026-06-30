# Tema: Control de flujo
# Bloque 00 Python
# Teoria de referencia: apuntes.md (misma carpeta)


# Ejercicio 1: edad = 20; si es mayor o igual a 18, imprimir "Mayor de edad" (solo el if, sin else)
edad = 20
if edad >= 18:
    print("Mayor de edad")

# Ejercicio 2: edad = 15; if/else que imprima "Mayor de edad" o "Menor de edad" segun corresponda
edad = 15
if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")

# Ejercicio 3: nota = 7; if/elif/else que imprima Sobresaliente (>=9), Notable (>=7), Aprobado (>=5) o Suspenso
nota = 7
if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print ("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")

# Ejercicio 4: edad = 20, tiene_entrada = True; if que imprima "Puede pasar" solo si es mayor de edad Y tiene entrada
edad = 20
tiene_entrada = True
if edad >= 18 and tiene_entrada:
    print("Puede pasar")
else:
    print("No puede pasar")

# Ejercicio 5: con un while, imprimir los numeros del 1 al 5 (acuerdate de cambiar el contador dentro)
print("---------- Ejercicio 5 ----------")
contador = 1
while contador <= 5:
    print(contador)
    contador = contador + 1

# Ejercicio 6: con un for y range(), imprimir los numeros del 0 al 4
print("---------- Ejercicio 6 ----------")
for i in range(5):
    print(i)

# Ejercicio 7: con un for y range(1, 11), imprimir solo los numeros pares (pista: if con n % 2 == 0)
print("---------- Ejercicio 7 ----------")
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# Ejercicio 8: recorrer [1, 2, 3, 4, 5] con un for; usar break para cortar cuando llegues al 4 (imprime 1 2 3)
print("--------- Ejercicio 8 ----------")
for n in [1, 2, 3, 4, 5]:
    if n == 4:
        break
    print(n)

# Ejercicio 9: recorrer [1, 2, 3, 4, 5] con un for; usar continue para saltarte el 3 (imprime 1 2 4 5)
print("---------- Ejercicio 9 ----------")
for n in [1, 2, 3, 4, 5]:
    if n == 3:
        continue
    print(n)

# Ejercicio final: pedir un numero con input(); con if/elif/else, imprimir si es "positivo", "negativo" o "cero"
print("---------- Ejercicio final ----------")
numero = int(input("Digite un número: "))
if numero > 0:
    print(f"{numero} es positivo.")
elif numero < 0:
    print(f"{numero} es negativo.")
else:
    print("Tu número es es cero.")
