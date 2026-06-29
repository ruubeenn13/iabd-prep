# Sintaxis básica

Bloque 00 Python. Apuntes de referencia de la unidad. El código de ejemplo es solo para entender cada idea.

## Variables

Una variable es un nombre que guarda un valor para reutilizarlo. Se asigna con `=` y se puede cambiar cuando quieras.

```python
edad = 25
edad = 30        # reasignada, ahora vale 30
nombre = "Ruben"
```

Reglas del nombre: letras, numeros y guion bajo, sin empezar por numero. Por convencion se usa snake_case (minusculas y guion bajo): mi_variable. Distingue mayusculas de minusculas: edad y Edad son variables distintas.

## Tipos de datos basicos

Todo valor tiene un tipo. Los cuatro basicos:

```python
entero = 25           # int, numero entero
decimal = 3.14        # float, numero con decimales
texto = "hola"        # str, cadena de texto (entre comillas)
booleano = True       # bool, solo True o False
```

`type(x)` te dice el tipo de un valor:

```python
print(type(25))       # <class 'int'>
print(type("hola"))   # <class 'str'>
```

## Operadores aritmeticos

```python
print(7 + 3)      # 10         suma
print(7 - 3)      # 4          resta
print(7 * 3)      # 21         multiplicacion
print(7 / 3)      # 2.333...   division (SIEMPRE da float)
print(7 // 3)     # 2          division entera (se queda con la parte de abajo)
print(7 % 3)      # 1          resto (modulo)
print(7 ** 2)     # 49         potencia (7 al cuadrado)
```

Los dos que mas se confunden: `/` siempre da decimal (float), `//` da el entero de abajo. Y `%` es el resto, que ya viste para saber si un numero es par.

## Conversion de tipos (casting)

Cambiar un valor de un tipo a otro con `int()`, `float()`, `str()`.

```python
print(int("42"))      # 42      texto a entero
print(float("3.14"))  # 3.14    texto a decimal
print(str(100))       # "100"   numero a texto
```

`int("hola")` da error: solo convierte texto que represente un numero. `int(3.9)` da 3 (corta los decimales, no redondea).

## Leer datos del usuario: input()

`input()` para la ejecucion y espera a que el usuario escriba. Devuelve SIEMPRE texto (str), aunque escriba un numero.

```python
nombre = input("Como te llamas? ")
print(nombre)
```

Para usarlo como numero hay que convertirlo:

```python
edad = int(input("Tu edad: "))    # leo texto y lo paso a entero
print(edad + 1)
```

## Operadores de comparacion

Comparan dos valores y dan un booleano (True o False).

```python
print(5 > 3)     # True    mayor que
print(5 < 3)     # False   menor que
print(5 >= 5)    # True    mayor o igual
print(5 <= 4)    # False   menor o igual
print(5 == 5)    # True    igual que (DOBLE igual)
print(5 != 3)    # True    distinto de
```

Cuidado: `==` compara (pregunta si son iguales), `=` asigna (da un valor a una variable). Son cosas distintas.

## Operadores logicos (and, or, not)

Combinan condiciones.

```python
print(True and False)   # False   'and': verdadero solo si los DOS lo son
print(True or False)    # True    'or': verdadero si AL MENOS uno lo es
print(not True)         # False   'not': invierte el valor
```

Con comparaciones:

```python
edad = 20
print(edad > 18 and edad < 65)   # True   esta entre 18 y 65
```

## f-strings (formatear texto)

La forma comoda de meter variables dentro de un texto. Pones una `f` antes de las comillas y la variable entre llaves `{ }`.

```python
nombre = "Ruben"
edad = 25
print(f"Me llamo {nombre} y mi edad es {edad}")
# Me llamo Ruben y mi edad es 25
```

Sin f-string tendrias que ir cortando el texto con comas; con f-string queda en una sola cadena legible.

## Resumen

- Variable: nombre = valor, reasignable, snake_case.
- Tipos: int, float, str, bool. type(x) lo dice.
- Aritmeticos: + - \* / (da float), // (entero), % (resto), \*\* (potencia).
- Conversion: int(), float(), str().
- input() devuelve siempre str; convierte si necesitas numero.
- Comparacion (== != < > <= >=) y logicos (and or not) dan booleanos.
- f-string: f"texto {variable}".
