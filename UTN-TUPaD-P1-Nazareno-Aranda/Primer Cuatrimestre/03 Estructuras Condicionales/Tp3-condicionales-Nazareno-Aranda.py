# Ejercicio 1

edad = int(input("Ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad.")

# Ejercicio 2

nota = float(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
 
 # Ejercicio 3

numero = int(input("Ingrese un número par: "))

if numero % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")

# Ejercicio 4

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# Ejercicio 5

contraseña = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

# Ejercicio 6

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print(f"Números aleatorios: {numeros_aleatorios}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")

if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
else:
    print("Sin sesgo")

# Ejercicio 7

texto = input("Ingrese una frase o palabra: ")

if texto[-1].lower() in "aeiou":
    texto += "!"

print(texto)

# Ejercicio 8

nombre = input("Ingrese su nombre: ")

print("Seleccione una opción:")
print("1. Nombre en mayúsculas")
print("2. Nombre en minúsculas")
print("3. Nombre con la primera letra en mayúscula")

opcion = input("Ingrese 1, 2 o 3: ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción no válida, por favor ingrese 1, 2 o 3.")

# Ejercicio 9

magnitud = float(input("Ingrese la magnitud del terremoto en la escala de Richter: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:  # magnitud >= 7
    print("Extremo (puede causar graves daños a gran escala)")

# Ejercicio 10

hemisferio = input("Ingrese el hemisferio en el que se encuentra (N/S): ").strip().upper()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día del mes: "))

if hemisferio not in ["N", "S"]:
    print("Hemisferio no válido. Debe ingresar 'N' para Norte o 'S' para Sur.")
else:
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        estacion_norte = "Invierno"
        estacion_sur = "Verano"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        estacion_norte = "Primavera"
        estacion_sur = "Otoño"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        estacion_norte = "Verano"
        estacion_sur = "Invierno"
    else:  # Desde 21 de septiembre hasta 20 de diciembre
        estacion_norte = "Otoño"
        estacion_sur = "Primavera"

    if hemisferio == "N":
        print(f"Usted se encuentra en la estación: {estacion_norte}")
    else:
        print(f"Usted se encuentra en la estación: {estacion_sur}")

# Trabajo finalizado por: Nazareno Aranda , mail: nazapro13@outlook.com
