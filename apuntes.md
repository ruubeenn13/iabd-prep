# Apuntes IABD Prep

Notas personales del periodo de preparación. Las vamos ampliando sobre la marcha: cada concepto con su explicación, su sintaxis y ejemplos, para poder volver a consultarlo más adelante.

El código de ejemplo de estos apuntes es solo de referencia para entender cada idea. Los ejercicios los escribo y los entiendo yo.

## Índice

- Bloque 00 Python
  - Comprehensions

## Bloque 00 Python

### Comprehensions

#### Para qué sirven

Tienes una colección y quieres otra colección sacada de ella: transformar cada elemento, quedarte solo con algunos, o las dos cosas a la vez. Es lo que se hace constantemente al manipular datos, y lo que harás todo el rato más adelante con pandas y Spark. Una comprehension es la forma corta e idiomática que tiene Python de hacerlo.

#### El bucle de siempre (versión larga)

Antes de la versión corta, la de toda la vida, que ya conoces:

```python
numeros = [1, 2, 3, 4]

# objetivo: una lista nueva con cada numero multiplicado por 10
resultado = []                # lista vacia donde voy metiendo los resultados
for n in numeros:             # recorro la lista, en cada vuelta n es un elemento
    resultado.append(n * 10)  # append mete el valor al final de la lista

print(resultado)              # [10, 20, 30, 40]
```

Recordatorio de las piezas: `[]` es una lista vacía, `for n in numeros` recorre la lista (en cada vuelta `n` es el elemento actual) y `.append(x)` mete `x` al final.

#### La misma operación en una línea

Python deja comprimir ese patrón de lista vacía más for más append en una sola línea. Eso es una comprehension. No es un concepto nuevo: es el mismo bucle, encogido.

```python
numeros = [1, 2, 3, 4]
resultado = [n * 10 for n in numeros]
print(resultado)              # [10, 20, 30, 40]
```

#### De dónde sale cada pieza

Las dos versiones juntas:

```python
# bucle
resultado = []
for n in numeros:
    resultado.append(n * 10)

# comprehension
resultado = [n * 10 for n in numeros]
```

- Los corchetes `[ ]` son el `resultado = []` y el `.append()` fundidos en uno.
- Lo de delante, `n * 10`, es exactamente lo que antes metías en el append: lo que quieres guardar en cada vuelta.
- Lo del medio, `for n in numeros`, es el bucle copiado tal cual.

Lo que cuesta viniendo de Java: escribes primero QUÉ guardas y después DE DÓNDE lo sacas. En el bucle, el `n * 10` está al final, dentro del append. En la comprehension, ese mismo `n * 10` salta al principio.

Forma de leerla en voz alta: "dame n por 10, para cada n en numeros".

#### Filtrar con un if al final

Para quedarte solo con los elementos que cumplen una condición, añades un `if` al final.

```python
numeros = [1, 2, 3, 4, 5, 6]
resultado = [n for n in numeros if n % 2 == 0]
print(resultado)              # [2, 4, 6]
```

El operador `%` da el resto de una división. `n % 2 == 0` significa "n es par" (4 % 2 es 0, 5 % 2 es 1). Es la forma estándar de preguntar si un número es par.

#### Las tres posiciones (toda la regla)

```python
[  n        for n in numeros    if n % 2 == 0  ]
#  guardas  recorres            filtras (opcional)
#  delante  en medio            al final
```

Esa es la regla entera: lo que guardas delante, el bucle en medio, el filtro detrás. El filtro es opcional.

Transformar y filtrar a la vez:

```python
resultado = [n ** 2 for n in numeros if n % 2 == 0]
print(resultado)              # [4, 16, 36]
# n ** 2 es n al cuadrado (dos asteriscos seguidos es potencia)
```

#### Diccionarios (dict comprehension)

Un diccionario es una colección de parejas clave-valor, un mapa donde a cada clave le corresponde un valor. Es el equivalente al HashMap de Java. Se construye con llaves `{}` y, en la parte de delante, `clave: valor` separados por dos puntos.

```python
nombres = ["ana", "luis", "alba"]
longitudes = {nombre: len(nombre) for nombre in nombres}
print(longitudes)             # {"ana": 3, "luis": 4, "alba": 4}
# len(x) devuelve cuantos caracteres tiene x
```

Lo único nuevo es `nombre: len(nombre)`: la clave antes de los dos puntos, el valor después. El for y el if opcional funcionan igual que en una lista.

#### Conjuntos (set comprehension)

Un set es una colección sin elementos repetidos y sin orden, útil cuando quieres valores únicos. También usa llaves `{}`, pero SIN los dos puntos. Eso es lo único que lo distingue de un dict por fuera.

```python
palabras = ["sol", "luna", "mar", "sol"]
iniciales = {p[0] for p in palabras}
print(iniciales)              # {"s", "l", "m"}
# p[0] es el primer caracter de p (las posiciones empiezan en 0)
# "sol" aparece dos veces pero la "s" sale una sola vez
```

#### El envoltorio es lo único que cambia entre los tres

- `[ ... ]` es una lista
- `{ clave: valor ... }` es un diccionario (lleva dos puntos)
- `{ ... }` es un set (sin dos puntos)

#### Cosas a tener en cuenta

- Si una comprehension no se entiende de un vistazo, vuelve al bucle for. Lo legible gana siempre. Una comprehension ilegible es peor que un bucle claro.
- No modifica la colección original: crea una nueva. Después de ejecutarla, la lista de partida sigue intacta.
- Existe otra forma con `if/else` puesto DELANTE en vez de al final, pero eso sirve para elegir entre dos valores, no para filtrar. Se verá aparte cuando toque.
