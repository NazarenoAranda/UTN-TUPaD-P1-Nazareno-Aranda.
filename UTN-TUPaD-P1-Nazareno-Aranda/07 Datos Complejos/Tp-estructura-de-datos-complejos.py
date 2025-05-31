#Ej 1

precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300


print(precios_frutas)

#Ej 2

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)


#Ej 3

precios_frutas = {
    'Banana': 1330,
    'Ananá': 2500,
    'Melón': 2800,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1700,
    'Pera': 2300
}

frutas = list(precios_frutas.keys())
print(frutas)


#Ej 4

contactos = {}

for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    numero = input(f"Ingresá el número de {nombre}: ")
    contactos[nombre] = numero

consulta = input("Ingresá el nombre del contacto a buscar: ")
if consulta in contactos:
    print(f"Número de {consulta}: {contactos[consulta]}")
else:
    print("Contacto no encontrado.")


#Ej 5

frase = input("Ingresá una frase: ")
palabras = frase.split()

palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("Recuento:", recuento)


#Ej 6

alumnos = {}

for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    notas = []
    for j in range(3):
        nota = int(input(f"Ingresá la nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno} - Promedio: {promedio:.2f}")


#Ej 7

parcial1 = {'Ana', 'Juan', 'Luis'}
parcial2 = {'Luis', 'Sofía', 'Ana'}

ambos = parcial1 & parcial2

solo_uno = parcial1 ^ parcial2

al_menos_uno = parcial1 | parcial2

print("Ambos:", ambos)
print("Solo uno:", solo_uno)
print("Al menos uno:", al_menos_uno)


#Ej 8

stock = {}

while True:
    print("\n--- Menú de Stock ---")
    print("1. Consultar stock")
    print("2. Agregar stock")
    print("3. Salir")
    opcion = input("Elegí una opción: ")

    if opcion == "1":
        prod = input("Nombre del producto: ")
        if prod in stock:
            print(f"Stock de {prod}: {stock[prod]}")
        else:
            print("Producto no encontrado.")

    elif opcion == "2":
        prod = input("Nombre del producto: ")
        cantidad = int(input("Cantidad a agregar: "))
        if prod in stock:
            stock[prod] += cantidad
        else:
            stock[prod] = cantidad
        print(f"Stock actualizado: {stock[prod]} unidades de {prod}")

    elif opcion == "3":
        print("Saliendo del sistema de stock.")
        break
    else:
        print("Opción inválida.")


#Ej 9

agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"
}

dia = input("Ingresá el día: ")
hora = input("Ingresá la hora (ej: 10:00): ")

clave = (dia, hora)

if clave in agenda:
    print(f"Actividad: {agenda[clave]}")
else:
    print("No hay actividad programada.")


#Ej 10

original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago"
}

invertido = {}
for pais, capital in original.items():
    invertido[capital] = pais

print("Diccionario invertido:", invertido)