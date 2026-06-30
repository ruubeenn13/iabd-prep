# Funciones

Bloque 00 Python. Apuntes de referencia de la unidad. El código de ejemplo es solo para entender cada idea. Esta es la unidad central de Python base: casi todo lo que escribas de aquí en adelante vivirá dentro de funciones.

## Qué es una funcion

Una funcion es un bloque de codigo con nombre que puedes ejecutar cuantas veces quieras. En vez de repetir las mismas lineas, las metes en una funcion y la llamas por su nombre. Sirve para no repetirte y para ordenar el codigo en piezas con sentido.

Ya has usado funciones que vienen hechas: print(), len(), int(), range(). Ahora vas a crear las tuyas.

## Definir y llamar una funcion

Se define con `def`, un nombre, parentesis y dos puntos. El cuerpo va con sangria (4 espacios), igual que en los if.

```python
def saludar():
    print("Hola")

saludar()    # Hola
```

Dos pasos distintos: DEFINIR la funcion (con def) no ejecuta nada, solo la crea. Se ejecuta cuando la LLAMAS, escribiendo su nombre con parentesis: saludar(). Puedes llamarla las veces que quieras.

```python
saludar()    # Hola
saludar()    # Hola
```

## Parametros: pasar informacion a la funcion

Un parametro es un dato que la funcion recibe para trabajar con el. Va dentro de los parentesis.

```python
def saludar(nombre):
    print("Hola", nombre)

saludar("Ruben")    # Hola Ruben
saludar("Sara")     # Hola Sara
```

`nombre` es el parametro (el hueco). "Ruben" es el argumento (el valor real que le pasas al llamar). La misma funcion sirve para cualquier nombre.

Puedes tener varios parametros, separados por comas:

```python
def sumar(a, b):
    print(a + b)

sumar(3, 5)    # 8
```

## return: que la funcion DEVUELVA un resultado

Hasta aqui las funciones solo imprimian. Pero normalmente quieres que la funcion CALCULE algo y te lo DEVUELVA para usarlo despues. Eso es `return`.

```python
def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print(resultado)        # 8
```

Diferencia clave entre print y return:

- print solo MUESTRA en pantalla; el valor se pierde, no lo puedes reutilizar.
- return DEVUELVE el valor a quien llamo la funcion, y lo puedes guardar en una variable y seguir operando.

```python
doble = sumar(3, 5) * 2    # uso el valor devuelto en otra operacion
print(doble)               # 16
```

Cuando Python llega a un return, sale de la funcion ahi mismo; las lineas que haya despues no se ejecutan.

## Una funcion sin return

Si una funcion no tiene return (como la de saludar que solo hace print), Python devuelve por defecto None (el valor "nada"). Es normal para funciones que solo hacen una accion y no calculan nada.

## Parametros por defecto

Puedes dar a un parametro un valor por defecto, que se usa si al llamar no pasas ese argumento.

```python
def saludar(nombre, saludo="Hola"):
    print(saludo, nombre)

saludar("Ruben")              # Hola Ruben      (usa el saludo por defecto)
saludar("Ruben", "Buenas")    # Buenas Ruben    (lo cambias al pasarlo)
```

Los parametros con valor por defecto van SIEMPRE despues de los que no lo tienen.

## Argumentos por nombre

Al llamar puedes indicar el nombre del parametro, asi no dependes del orden:

```python
def dividir(a, b):
    return a / b

print(dividir(b=2, a=10))    # 5.0   (da igual el orden porque los nombras)
```

## \*args: numero variable de argumentos

A veces no sabes cuantos argumentos te van a pasar. Con un asterisco delante de un parametro, la funcion los recoge TODOS en una tupla.

```python
def sumar_todos(*numeros):
    total = 0
    for n in numeros:
        total = total + n
    return total

print(sumar_todos(1, 2, 3))       # 6
print(sumar_todos(1, 2, 3, 4))    # 10
```

`numeros` aqui es una tupla con todo lo que pases. El nombre puede ser cualquiera; la convencion es llamarlo `args` (`*args`). Esto es el mismo unpacking con estrella que ya viste, ahora aplicado a los argumentos de una funcion.

## \*\*kwargs: argumentos con nombre variables

Con DOS asteriscos, la funcion recoge los argumentos que le pases CON NOMBRE, en un diccionario.

```python
def mostrar_datos(**datos):
    for clave, valor in datos.items():
        print(clave, "=", valor)

mostrar_datos(nombre="Ruben", edad=20)
# nombre = Ruben
# edad = 20
```

`datos` es un diccionario {nombre: "Ruben", edad: 20}. La convencion es llamarlo `kwargs` (`**kwargs`, de keyword arguments). Recorrerlo con .items() es justo lo que practicaste en unpacking.

## Resumen

- Definir: `def nombre(parametros):` y el cuerpo con sangria.
- Llamar: `nombre(argumentos)`. Definir no ejecuta; llamar si.
- Parametro es el hueco; argumento es el valor real que pasas.
- return DEVUELVE un valor para reutilizarlo (distinto de print, que solo muestra). Sin return, la funcion devuelve None.
- Parametros por defecto: `def f(x, y=10):`, van despues de los normales.
- Argumentos por nombre: `f(y=2, x=1)`, no dependen del orden.
- `*args`: recoge muchos argumentos sueltos en una tupla.
- `**kwargs`: recoge argumentos con nombre en un diccionario.
