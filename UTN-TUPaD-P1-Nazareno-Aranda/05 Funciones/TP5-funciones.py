import math

#Ejercicio 1.
def imprimir_hola_mundo():
    print("Hola Mundo!")

#Ejercicio 2.
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

#Ejercicio 3.
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#Ejercicio 4.
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

#Ejercicio 5. 
def segundos_a_horas(segundos):
    return segundos / 3600

#Ejercicio 6.
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

#Ejercicio 7.
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinido (división por cero)"
    return (suma, resta, multiplicacion, division)

#Ejercicio 8.
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

#Ejercicio 9.
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

#Ejercicio 10.
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal.
if __name__ == "__main__":
    # Punto 1.
    imprimir_hola_mundo()
    print()

    # Punto 2.
    nombre_usuario = input("Ingresa tu nombre: ")
    print(saludar_usuario(nombre_usuario))
    print()

    # Punto 3.
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")
    residencia = input("Lugar de residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)
    print()

    # Punto 4.
    radio = float(input("Ingresa el radio de un círculo: "))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"Área del círculo: {area:.2f}")
    print(f"Perímetro del círculo: {perimetro:.2f}")
    print()

    # Punto 5.
    segundos = int(input("Ingresa una cantidad de segundos: "))
    horas = segundos_a_horas(segundos)
    print(f"{segundos} segundos equivalen a {horas:.2f} horas.")
    print()

    # Punto 6.
    numero_tabla = int(input("Ingresa un número para ver su tabla de multiplicar: "))
    tabla_multiplicar(numero_tabla)
    print()

    # Punto 7.
    a = float(input("Primer número para operaciones básicas: "))
    b = float(input("Segundo número: "))
    suma, resta, multiplicacion, division = operaciones_basicas(a, b)
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")
    print()

    # Punto 8.
    peso = float(input("Ingresa tu peso en kg: "))
    altura = float(input("Ingresa tu altura en metros: "))
    imc = calcular_imc(peso, altura)
    print(f"Tu IMC es: {imc:.2f}")
    print()

    # Punto 9.
    celsius = float(input("Temperatura en Celsius: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")
    print()

    # Punto 10.
    n1 = float(input("Primer número para promedio: "))
    n2 = float(input("Segundo número: "))
    n3 = float(input("Tercer número: "))
    promedio = calcular_promedio(n1, n2, n3)
    print(f"El promedio es: {promedio:.2f}")
