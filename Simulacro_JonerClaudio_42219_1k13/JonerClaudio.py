"""
Desarrolle un programa completo en Python que permita generar una sucesión de 20000 números enteros aleatorios,
usando como semilla del generador el numero 49 (es decir random.seed(49)). Los valores de cada uno de esos 20000
números deben estar entre 1 y 45000 (incluidos ambos) (DEBE usar random.randint(1, 45000) para generar esos números).

A modo de elemento de control, y para que cada estudiante sepa si la secuencia que está generando es la correcta,
indicamos aquí cuánto debe valer la suma de todos los números generados con el mecanismo indicado:

Suma de todos los números generados: 451459554
A partir de esa sucesión el programa debe:


Indicar cuantos números eran múltiplos de 5, cuántos eran múltiplos de 7 y cuántos eran múltiplos de 9.
Indicar el mayor entre todos aquellos números cuyo último dígito sea mayor o igual a 5 pero menor o igual a 8.
Indicar cuantos números generados son pares menores a 15000.
Indicar el porcentaje entero que representa el punto anterior sobre el total de números procesados.

Aclaración 1: NO se pide el porcentaje redondeado, sino el porcentaje truncado, sin decimales.
Aclaración 2: en el cálculo de este porcentaje, haga primero la multiplicación que corresponda, y luego la división.
Cuando finalice, en las consignas que siguen en este mismo cuestionario, se le pedirá que informe cada uno de estos
resultados, y también se le pedirá que suba el archivo de código fuente con el programa desarrollado (por lo que tenga
muy presente en donde dejó ese archivo). Entienda: Si NO sube su código fuente, los profesores procederán a reprobar
manualmente su parcial. Habrá también UNA pregunta de opciones múltiples referida a este mismo enunciado o a
temas relacionados con él.


"""
import math

"""35
Indicar cuantos números eran múltiplos de 5, cuántos eran múltiplos de 7 y cuántos eran múltiplos de 9.ok
Indicar el mayor entre todos aquellos números cuyo último dígito sea mayor o igual a 5 pero menor o igual a 8.
Indicar cuantos números generados son pares menores a 15000.
Indicar el porcentaje entero que representa el punto anterior sobre el total de números procesados.
"""
import random

random.seed(49)

total= 0
multiplos_cinco =0
multiplos_siete =0
multiplos_nueve =0
pares = 0
mayor = 0

for numero in range(20000):
    numero = random.randint(1, 45000)

    if numero % 5 == 0:
        multiplos_cinco += 1    # multiplos_cinco = multiplos_cinco + 1

    if numero % 7 == 0:
        multiplos_siete += 1

    if numero % 9 == 0:
        multiplos_nueve += 1

    if numero > mayor:
        ultimo_digito = numero % 10 # 0 1 2 3 4 5 6 7 8 9 %100 2 % 1000 3
        if 5<= ultimo_digito <= 8 : # numero>= 5 and numero <= 8
            mayor = numero


    if numero % 2 == 0 and numero < 15000:
        pares += 1

    total += numero
    #451459554

    porcentaje = int((pares / 20000) * 100)

    indice = str(porcentaje).index(".")

[0: ]
print(total)
print(indice)

#PRINTS
print("Multiplos de 5 son: ", multiplos_cinco)
print("Multiplos de 7 son: ", multiplos_siete)
print("Multiplos de 9 son: ", multiplos_nueve)
print("El numero mayor es: ", mayor)
print("Cantidad de pares son: ", pares)
print("Proncentaje: ", porcentaje)



