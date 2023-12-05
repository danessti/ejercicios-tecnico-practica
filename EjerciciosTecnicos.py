### 2 ###

# Calentemos motores con un poco de Python
# En este reto pondremos a prueba tu habilidad con Python en un nivel muy básico el problema que te planteamos ahora
# consiste en crear una función que te permita a clasificar los grupos poblacionales de acuerdo a su edad
# (Menor de edad, Adulto, Adulto mayor), aquí están los rangos:

# Menor a 18: Menor de Edad

# Desde los 18 hasta los 60 : Adulto

# Mayor de 60: Adulto Mayor

# Dada la función clasificar_por_edad(edad) en donde edad es un número entero con la edad debes retornar:

# 0 si es menor de Edad

# 1 si es adulto

# 2 si es Adulto Mayor

# Bono: eres capaz de hacerlo sin usar "if"?

def clasificar_por_edad(edad):
    return (edad < 18) * 0 + (18 <= edad < 60) * 1 + (edad >= 60) * 2

    # Ejemplos de uso
    print(clasificaxr_por_edad(15))  # Salida: 0 (Menor de Edad)
    print(clasificar_por_edad(30))  # Salida: 1 (Adulto)
    print(clasificar_por_edad(70))  # Salida: 2 (Adulto Mayor)


### 3 ###

# Una de las series más elegantes en matemáticas
# En la Edad Media, el matemático italiano Fibonacci contaba el crecimiento de una población
# de conejos y descubrió la serie que lleva su nombre.

# Definición:

# La serie de Fibonacci se define recursivamente de la siguiente manera:

# fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)

# Dónde:

# fibonacci(0) = 0, fibonacci(1) = 1

# Ejemplo:

# Calcula fibonacci(3) , sabemos por la definición esto:

# fibonacci(3) = fibonacci(2) + fibonacci(1)

# Pero al mismo tiempo, sabemos que fibonacci(1) = 1 y fibonacci(2) = fibonacci(1) + fibonacci(0)

# Luego reemplazando:

# fibonacci(3) = fibonacci(1) + fibonacci(0) + fibonacci(1)

# fibonacci(3) = 2

# Ejercicio :

# Implemente una función fibonacci(n) en Python que calcula el enésimo elemento de la serie de Fibonacci,
# la función recibe un número entero n que es el índice de la serie de Fibonacci.

# Bonificación : para n grandes n qué problema podría haber con una implementación recursiva?
# ¿Se podría utilizar la programación dinámica para redux el uso de memoria de nuestro algoritmo?
# ¿Qué operaciones podemos estar repitiendo al hacer un algoritmo recursivo?

def fibonacci(n):
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


numero_elementos = 15

print("Secuencia de Fibonacci:")
for i in range(numero_elementos):
    print(fibonacci(i), end=" ")


### 4 ###

# Este código Python tiene errores, ¿puedes encontrarlos?
# Ejecute el código actual, observe el resultado,
# compárelo con la respuesta esperada y corrija el error. Uno a uno hasta llegar a la respuesta, ¡ve por ellos!

def fix_me(nested_list):
    final_list = []
    for idx, a_list in enumerate(nested_list):
        partial_sum = 0
        for basic_element in a_list:
            partial_sum -= basic_element

        if idx % 2 == 0:
            partial_sum *= -1

        final_list.append(partial_sum)

    return final_list
