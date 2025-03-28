#Tp 1 Estructuras Secuenciales
#Ej:1
print("“Hola Mundo!”. ")

#Ej:2
nombre = input("Ingresa tu nombre: ")

print(f"Hola {nombre}!")

#Ej:3
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#Ej:4
import math

radio = float(input("Ingresa el radio del círculo: "))

area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")

'''
Si queremos redeondear a solo 2 decimales el resultado podriamos utilizar en la:
Linea 8 este codigo: print(f"El área del círculo es: {area:.2f}")
Linea 9 este codigo: print(f"El perímetro del círculo es: {perimetro:.2f}")

'''

#Ej:5
segundos = int(input("Ingresa la cantidad de segundos: "))

horas = segundos / 3600  

print(f"{segundos} segundos equivalen a {horas:.2f} horas.")


#Ej:6
numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))

for i in range(1, 11): 
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#Ej:7
num1 = int(input("Ingresa el primer número entero (distinto de 0): "))
num2 = int(input("Ingresa el segundo número entero (distinto de 0): "))

if num1 == 0 or num2 == 0:
    print("Los números no deben ser 0. Intenta de nuevo.")
else:
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    if num2 != 0:
        division = num1 / num2
    else:
        division = "Indefinido (no se puede dividir entre 0)"

    print(f"La suma de {num1} y {num2} es: {suma}")
    print(f"La resta de {num1} y {num2} es: {resta}")
    print(f"La multiplicación de {num1} y {num2} es: {multiplicacion}")
    print(f"La división de {num1} y {num2} es: {division}")

#Ej:8
peso = float(input("Ingresa tu peso en kilogramos: "))

altura = float(input("Ingresa tu altura en metros: "))

imc = peso / (altura ** 2)

print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")

#Ej:9
celsius = float(input("Ingresa la temperatura en grados Celsius: "))

fahrenheit = (9/5) * celsius + 32

print(f"La temperatura en Fahrenheit es: {fahrenheit:.2f}")

#Ej:10
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
numero3 = float(input("Ingresa el tercer número: "))

promedio = (numero1 + numero2 + numero3) / 3

print(f"El promedio de los tres números es: {promedio:.2f}")