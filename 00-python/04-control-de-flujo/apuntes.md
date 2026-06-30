# Control de flujo

Bloque 00 Python. Apuntes de referencia de la unidad. El código de ejemplo es solo para entender cada idea. El for ya lo conoces de comprehensions y unpacking; aquí lo nuevo son los condicionales (if/elif/else) y el while.

## Qué es el control de flujo

Hasta ahora tu código se ejecutaba de arriba a abajo, línea por línea. El control de flujo te deja decidir QUE se ejecuta (condicionales) y CUANTAS veces (bucles), en lugar de hacer siempre todo una vez.

## El if: ejecutar algo solo si se cumple una condicion

`if` ejecuta el bloque de dentro solo si la condicion es True. La condicion es una comparacion, de las que viste (devuelve True o False).

```python
edad = 20
if edad >= 18:
    print("Eres mayor de edad")
# Eres mayor de edad
```

Fijate en dos cosas: los dos puntos `:` al final del if, y la sangria (4 espacios) de la linea de dentro. Esa sangria es lo que marca que el print pertenece al if. Si la condicion fuese False, ese print no se ejecutaria y no pasaria nada.

## El else: que hacer si NO se cumple

`else` es el camino alternativo: se ejecuta cuando el if es False.

```python
edad = 15
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
# Eres menor de edad
```

Solo se ejecuta UNO de los dos bloques: o el del if, o el del else, nunca los dos.

## El elif: varios caminos

Cuando hay mas de dos opciones, `elif` (abreviatura de "else if") encadena condiciones. Python las prueba en orden y ejecuta la PRIMERA que sea True; el resto se ignora.

```python
nota = 7
if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")
# Notable
```

Aunque nota >= 5 tambien seria True, no se ejecuta: en cuanto una condicion se cumple (nota >= 7), Python sale del bloque. El orden importa.

## Combinar condiciones

Dentro de un if puedes usar los operadores logicos (and, or, not) que ya viste.

```python
edad = 20
tiene_entrada = True
if edad >= 18 and tiene_entrada:
    print("Puede pasar")
# Puede pasar
```

## El bucle while: repetir MIENTRAS se cumpla algo

El for recorre una coleccion. El while es distinto: repite el bloque MIENTRAS la condicion siga siendo True, y para cuando se vuelve False.

```python
contador = 1
while contador <= 3:
    print(contador)
    contador = contador + 1
# 1
# 2
# 3
```

Paso a paso: contador empieza en 1, la condicion (1 <= 3) es True, imprime y suma 1. Se repite con 2 y con 3. Cuando contador llega a 4, la condicion (4 <= 3) es False y el bucle termina.

Aviso importante: dentro del while TIENES que cambiar algo que acerque la condicion a False (aqui, sumar al contador). Si no, la condicion es siempre True y el bucle no termina nunca (bucle infinito). Es el error clasico del while.

## for vs while

- for: cuando sabes sobre que recorres (una lista, un rango de numeros). "Para cada elemento, haz esto".
- while: cuando repites hasta que pase algo, sin saber cuantas veces. "Mientras se cumpla, sigue".

## range(): generar una secuencia de numeros

Muy usado con el for cuando quieres repetir un numero concreto de veces o recorrer numeros. `range(n)` da los numeros de 0 a n-1.

```python
for i in range(5):
    print(i)
# 0 1 2 3 4   (cada uno en su linea)
```

range tambien acepta inicio y fin: `range(2, 6)` da 2, 3, 4, 5 (el fin no entra, igual que el slicing).

```python
for i in range(1, 4):
    print(i)
# 1 2 3
```

## break y continue (control dentro del bucle)

Dos palabras para afinar un bucle:

```python
# break: corta el bucle del todo
for n in [1, 2, 3, 4, 5]:
    if n == 3:
        break
    print(n)
# 1 2        (al llegar a 3 corta y sale)

# continue: salta a la siguiente vuelta sin terminar la actual
for n in [1, 2, 3, 4, 5]:
    if n == 3:
        continue
    print(n)
# 1 2 4 5    (se salta solo el 3)
```

## Resumen

- if: ejecuta si la condicion es True. Lleva `:` y el bloque va con sangria.
- else: el camino alternativo, si el if es False.
- elif: mas opciones; se ejecuta la primera condicion True, el orden importa.
- Condiciones se combinan con and, or, not.
- while: repite MIENTRAS la condicion sea True; cambia algo dentro o sera infinito.
- for con range(n): repetir o recorrer numeros (0 a n-1).
- break corta el bucle; continue salta a la siguiente vuelta.
