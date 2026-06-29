# Estructuras de datos

Bloque 00 Python. Apuntes de referencia de la unidad. El código de ejemplo es solo para entender cada idea. Parte de esto (listas, diccionarios y sets) ya lo tocaste en comprehensions; aquí queda completo y con lo que faltaba: tuplas, métodos, slicing y operaciones.

## Listas

Una lista es una colección ordenada de valores, entre corchetes y separados por comas. Puede mezclar tipos.

```python
frutas = ["pera", "kiwi", "uva"]
numeros = [10, 20, 30]
```

Accedes a un elemento por su posicion (empieza en 0):

```python
print(frutas[0])    # pera   primero
print(frutas[1])    # kiwi   segundo
```

Con indices negativos cuentas desde el final:

```python
print(frutas[-1])   # uva    ultimo
print(frutas[-2])   # kiwi   penultimo
```

## Slicing (cortar una parte)

`lista[inicio:fin]` te da un trozo, desde inicio hasta fin SIN incluir el fin.

```python
numeros = [10, 20, 30, 40, 50]
print(numeros[1:4])   # [20, 30, 40]   de la posicion 1 a la 3
print(numeros[:2])    # [10, 20]       desde el principio hasta la 1
print(numeros[2:])    # [30, 40, 50]   desde la posicion 2 hasta el final
```

## Metodos de lista

Acciones sobre una lista. Se llaman con un punto: lista.metodo().

```python
numeros = [3, 1, 2]
numeros.append(4)      # aniade 4 al final          -> [3, 1, 2, 4]
numeros.insert(0, 9)   # inserta 9 en la posicion 0 -> [9, 3, 1, 2, 4]
numeros.remove(1)      # quita el primer 1          -> [9, 3, 2, 4]
numeros.pop()          # quita y devuelve el ultimo -> [9, 3, 2]
numeros.sort()         # ordena de menor a mayor    -> [2, 3, 9]
print(len(numeros))    # 3    cuantos elementos tiene
```

## Comprobar si algo esta dentro: in

`in` dice si un valor esta en la lista. Da True o False.

```python
frutas = ["pera", "kiwi"]
print("pera" in frutas)    # True
print("uva" in frutas)     # False
```

## Tuplas

Una tupla es como una lista pero INMUTABLE: una vez creada, no puedes cambiar, aniadir ni quitar nada. Se escribe con parentesis.

```python
punto = (10, 20)
print(punto[0])    # 10    se indexa igual que una lista
```

Intentar modificarla da error:

```python
punto[0] = 99      # ERROR: una tupla no se puede modificar
```

Para que sirve: datos que no deben cambiar (unas coordenadas, una fecha, un par fijo). Si vienes del unpacking, los pares que desempaquetabas eran tuplas. Aviso: una tupla de un solo elemento necesita una coma, (5,), porque (5) sin coma Python lo ve como el numero 5 entre parentesis.

## Diccionarios

Parejas clave-valor. Cada clave apunta a un valor. Se escribe con llaves y clave: valor.

```python
edades = {"ana": 30, "luis": 25}
print(edades["ana"])   # 30    busco por la clave
```

Aniadir o modificar es asignar a una clave:

```python
edades["marco"] = 40   # aniade una pareja nueva
edades["ana"] = 31     # modifica la que ya existia
```

Comprobar si una clave esta:

```python
print("ana" in edades)   # True   (in mira las CLAVES)
```

## Metodos de diccionario

```python
edades = {"ana": 30, "luis": 25}
print(edades.get("ana"))      # 30
print(edades.get("pepe"))     # None   (no existe, pero NO da error)
print(edades.keys())          # las claves
print(edades.values())        # los valores
print(edades.items())         # las parejas (clave, valor)
```

La diferencia que importa: edades["pepe"] da error si la clave no existe; edades.get("pepe") devuelve None sin romper. `.items()` es lo que usabas para recorrer el diccionario con unpacking.

## Sets (conjuntos)

Coleccion SIN repetidos y SIN orden. Llaves, pero sin los dos puntos.

```python
s = {1, 2, 3}
s.add(4)           # aniade un elemento
print(s)           # {1, 2, 3, 4}
```

Si creas un set a partir de una lista con repetidos, los quita:

```python
print(set([1, 2, 2, 3, 3]))   # {1, 2, 3}
```

Aviso importante: un set vacio se crea con set(), NO con {}. Las llaves vacias {} son un diccionario vacio, no un set.

## Operaciones con sets

Como los conjuntos de matematicas:

```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)    # {2, 3}        interseccion (lo que esta en los dos)
print(a | b)    # {1, 2, 3, 4}  union (todo, sin repetir)
print(a - b)    # {1}           diferencia (lo de a que no esta en b)
```

## Resumen

- Lista [ ]: ordenada y modificable. Indices desde 0, negativos desde el final, slicing [a:b].
- Metodos de lista: append, insert, remove, pop, sort, len.
- Tupla ( ): como una lista pero NO se puede modificar.
- Diccionario {clave: valor}: acceso por clave, .get() no rompe, .items() para recorrer.
- Set { } sin dos puntos: sin repetidos ni orden. Vacio es set(). Operaciones & | -.
- in comprueba pertenencia en todos.
