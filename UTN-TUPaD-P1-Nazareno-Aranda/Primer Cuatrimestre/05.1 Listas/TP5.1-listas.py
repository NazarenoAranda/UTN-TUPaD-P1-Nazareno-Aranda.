# EJERCICIO 1

multiples_de_4 = list(range(4, 101, 4))
print(multiples_de_4)


# EJERCICIO 2

mis_elementos = ["música", "programación", "mate", "perfumes", "papitas"]

print(mis_elementos[-2])


# EJERCICIO 3

lista_vacia = []

lista_vacia.append("El")
lista_vacia.append("Perro")
lista_vacia.append("Ladra")

print(lista_vacia)


# EJERCICIO 4

animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
animales[-1] = "oso"

print(animales)


# EJERCICIO 5

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

"""
Este programa realiza los siguientes pasos:

1. Se define una lista llamada 'numeros' con los valores: [8, 15, 3, 22, 7].

2. Se utiliza la función max(numeros) para encontrar el número más grande en la lista, 
   que en este caso es 22.

3. Luego, con el método remove(), se elimina ese número máximo (22) de la lista. 
   El método remove() elimina la primera vez que aparece ese valor en la lista.

4. Finalmente, se imprime la lista resultante, que ya no contiene el número 22.

Resultado esperado en pantalla:
[8, 15, 3, 7]

"""


# EJERCICIO 6

numeros = list(range(10, 31, 5))
print(numeros[:2])


# EJERCICIO 7

autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "corolla"
autos[2] = "civic"
print(autos)

# EJERCICIO 8

dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

# EJERCICIO 9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")

compras[1][1] = "tallarines"

compras[0].remove("pan")

print(compras)

# EJERCICIO 10

lista_anidada = [15, True, [25.5, 57.9, 30.6],False]

print(lista_anidada)