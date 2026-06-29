# Unpacking (desempaquetado)

Bloque 00 Python. Apuntes de referencia de la unidad. El código de ejemplo es solo para entender cada idea.

## Qué es el unpacking

Asignar varias variables a la vez, repartiendo los valores de una lista (o cualquier secuencia). Pones varios nombres a la izquierda, separados por comas, y Python reparte en orden.

```python
a, b = [1, 2]
print(a)        # 1
print(b)        # 2
```

El primer valor va a la primera variable, el segundo a la segunda, y así. Funciona con los valores que sean:

```python
x, y, z = [10, 20, 30]
print(x)        # 10
print(z)        # 30
```

## El número tiene que cuadrar

Hace falta tantas variables como valores. Ni más ni menos, o Python da error.

```python
a, b = [1, 2]          # bien: 2 variables, 2 valores
a, b = [1, 2, 3]       # ERROR: sobran valores (too many values to unpack)
a, b, c = [1, 2]       # ERROR: faltan valores (not enough values to unpack)
```

Si ves ese error, cuenta variables a la izquierda y valores a la derecha.

## Intercambiar dos variables

Cambiar dos valores de sitio es una sola línea, sin variable auxiliar. A la derecha el orden nuevo, a la izquierda los nombres.

```python
a = 1
b = 2
a, b = b, a
print(a)        # 2
print(b)        # 1
```

En Java esto necesita una variable temporal. Aquí no.

## Capturar el resto: el operador estrella

Una estrella `*` delante de una variable hace que esa recoja todo lo que sobre, en forma de lista.

```python
primero, *resto = [1, 2, 3, 4]
print(primero)  # 1
print(resto)    # [2, 3, 4]
```

La variable con estrella SIEMPRE es una lista, aunque sobre uno solo o nada:

```python
primero, *resto = [1, 2]
print(resto)    # [2]   (lista de un elemento)

primero, *resto = [1]
print(resto)    # []    (lista vacia)
```

## La estrella al final o en medio

No tiene que ser la primera variable. Recoge "lo que quede" tras repartir las fijas.

```python
*inicio, ultimo = [1, 2, 3, 4]
print(inicio)   # [1, 2, 3]
print(ultimo)   # 4

primero, *medio, ultimo = [1, 2, 3, 4, 5]
print(primero)  # 1
print(medio)    # [2, 3, 4]
print(ultimo)   # 5
```

## Unpacking dentro de un bucle for

Si cada elemento de una lista es a su vez una pareja, puedes desempaquetarla en el propio for, dándole dos nombres. Mucho más cómodo que usar pareja[0] y pareja[1].

```python
parejas = [[1, "uno"], [2, "dos"]]
for numero, texto in parejas:
    print(numero, texto)
# 1 uno
# 2 dos
```

En cada vuelta, numero coge el primero de la pareja y texto el segundo.

## enumerate: posición y valor a la vez

Cuando recorres una lista y necesitas también la posición de cada elemento, `enumerate` da pares de (posicion, valor) que desempaquetas en el for. Numera desde 0.

```python
frutas = ["pera", "kiwi", "uva"]
for indice, fruta in enumerate(frutas):
    print(indice, fruta)
# 0 pera
# 1 kiwi
# 2 uva
```

Es la forma correcta de tener el índice. Nada de llevar un contador a mano.

## Unpacking de un diccionario

Un diccionario se recorre con `.items()`, que da pares de (clave, valor). Se desempaquetan igual.

```python
edades = {"ana": 30, "luis": 25}
for nombre, edad in edades.items():
    print(nombre, edad)
# ana 30
# luis 25
```

nombre coge la clave, edad coge el valor. Es el patrón estándar para recorrer un diccionario entero.

## Resumen

- Básico: `a, b = [1, 2]` (el número de variables y de valores debe cuadrar)
- Intercambio: `a, b = b, a` (sin variable auxiliar)
- La estrella `*` recoge el resto en una lista, vaya delante, en medio o al final
- En bucles: desempaquetas cada elemento en el propio for (`for k, v in ...`)
- `enumerate(lista)` da (posición, valor); `dict.items()` da (clave, valor)

Nota: `*args` y `**kwargs` (número variable de argumentos) también son unpacking, pero van con las funciones. Se ven en el tema de funciones, no aquí.
