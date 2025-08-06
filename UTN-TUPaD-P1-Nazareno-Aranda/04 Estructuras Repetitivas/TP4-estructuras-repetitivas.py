#Ejercicio 1

for i in range(101):
    print(i)


#Ejercicio 2

numero = int(input("Ingresa un número entero: "))
cantidad_digitos = len(str(abs(numero)))
print(f"El número tiene {cantidad_digitos} dígitos.")


#Ejercicio 3

inicio = int(input("Ingresa el primer número: "))
fin = int(input("Ingresa el segundo número: "))

if inicio > fin:
    inicio, fin = fin, inicio

suma = 0
for i in range(inicio + 1, fin):
    suma += i

print(f"La suma de los números entre {inicio} y {fin}, excluyéndolos, es: {suma}")


#Ejercicio 4

total = 0

while True:
    numero = int(input("Ingresa un número entero (0 para terminar): "))
    if numero == 0:
        break
    total += numero

print(f"La suma total es: {total}")


#Ejercicio 5

import random

numero_secreto = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1
    if intento == numero_secreto:
        print(f"¡Correcto! Adivinaste en {intentos} intento(s).")
        break
    else:
        print("Incorrecto, intenta de nuevo.")


#Ejercicio 6

for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)


#Ejercicio 7

numero = int(input("Ingresa un número entero positivo: "))

if numero < 0:
    print("El número debe ser positivo.")
else:
    suma = 0
    for i in range(1, numero + 1):
        suma += i
    print(f"La suma de los números de 0 hasta {numero} es: {suma}")


#Ejercicio 8

cantidad_numeros = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

for _ in range(cantidad_numeros):
    numero = int(input("Ingresa un número entero: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"\nResultados:")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")


#Ejercicio 9

cantidad_numeros = 100  

suma = 0

for _ in range(cantidad_numeros):
    numero = int(input("Ingresa un número entero: "))
    suma += numero

media = suma / cantidad_numeros

print(f"\nLa media de los {cantidad_numeros} números ingresados es: {media}")


#Ejercicio 10

numero = int(input("Ingresa un número entero: "))

numero_invertido = int(str(abs(numero))[::-1])

if numero < 0:
    numero_invertido = -numero_invertido

print(f"El número invertido es: {numero_invertido}")
