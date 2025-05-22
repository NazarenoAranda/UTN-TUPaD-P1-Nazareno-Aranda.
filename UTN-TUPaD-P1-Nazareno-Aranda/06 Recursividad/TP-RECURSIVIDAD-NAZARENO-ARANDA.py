#Ej 1

def factorial(n):
    if n == 0 or n == 1:  # Caso base
        return 1
    else:  # Caso recursivo
        return n * factorial(n - 1)

# Pedimos un número al usuario
limite = int(input("Ingrese un número entero positivo: "))
print(f"Factoriales del 1 al {limite}:")
for i in range(1, limite + 1):
    print(f"{i}! = {factorial(i)}")

#Ej 2

def fibonacci(n):
    if n == 0:  # Caso base
        return 0
    elif n == 1:  # Caso base
        return 1
    else:  # Caso recursivo
        return fibonacci(n - 1) + fibonacci(n - 2)

# Pedimos al usuario un número
limite = int(input("Ingrese la cantidad de términos de la serie de Fibonacci: "))
print(f"Serie de Fibonacci hasta la posición {limite - 1}:")
for i in range(limite):
    print(f"F({i}) = {fibonacci(i)}")

'''
Esta version es la mas simple, pero no es eficiente para 
valores grandes porque repite muchos calculos.
'''
#Ej 3

def potencia(base, exponente):
    if exponente == 0:  # Caso base
        return 1
    else:  # Caso recursivo
        return base * potencia(base, exponente - 1)

# Pedimos los valores al usuario
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
resultado = potencia(base, exponente)

print(f"{base}^{exponente} = {resultado}")


#Ej 4

def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Pedimos un número al usuario
numero = int(input("Ingrese un número entero positivo: "))

# Caso especial para 0
if numero == 0:
    print("0 en binario es: 0")
else:
    binario = decimal_a_binario(numero)
    print(f"{numero} en binario es: {binario}")


#Ej 5

def es_palindromo(palabra):
    if len(palabra) <= 1:  # Caso base
        return True
    elif palabra[0] != palabra[-1]:  # Comparación entre extremos
        return False
    else:
        return es_palindromo(palabra[1:-1])  # Llamada recursiva al interior

# Pedimos al usuario una palabra
palabra = input("Ingrese una palabra sin espacios ni tildes: ").lower()

if es_palindromo(palabra):
    print(f"'{palabra}' es un palíndromo.")
else:
    print(f"'{palabra}' no es un palíndromo.")


#Ej 6

def suma_digitos(n):
    if n < 10:  # Caso base: un solo dígito
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

# Pedimos un número al usuario
numero = int(input("Ingrese un número entero positivo: "))
resultado = suma_digitos(numero)

print(f"La suma de los dígitos de {numero} es: {resultado}")


#Ej 7 

def contar_bloques(n):
    if n == 1:  # Caso base
        return 1
    else:  # Caso recursivo
        return n + contar_bloques(n - 1)

# Pedimos al usuario el número de bloques en el nivel más bajo
nivel_base = int(input("Ingrese la cantidad de bloques en el nivel más bajo: "))
total = contar_bloques(nivel_base)

print(f"Para construir la pirámide con base de {nivel_base} bloques, se necesitan {total} bloques en total.")


#Ej 8

def contar_digito(numero, digito):
    if numero == 0:  # Caso base
        return 0
    elif numero % 10 == digito:  # Coincidencia
        return 1 + contar_digito(numero // 10, digito)
    else:  # No hay coincidencia
        return contar_digito(numero // 10, digito)

# Pedimos datos al usuario
numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese el dígito que desea contar (0-9): "))

# Validamos el dígito
if 0 <= digito <= 9:
    cantidad = contar_digito(numero, digito)
    print(f"El dígito {digito} aparece {cantidad} veces en el número {numero}.")
else:
    print("Error: el dígito debe estar entre 0 y 9.")

#Trabajo realizado por: Nazareno Aranda-mail:nazapro13@outlook.com
