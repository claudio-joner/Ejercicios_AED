import random


random.seed(5)

billete = random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),
random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),
random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),
random.randint(1,100),random.randint(1,100),random.randint(1,100)

numero_1 = int(input("Ingrese el valor del numero: "))
numero_2 = int(input("Ingrese el valor del numero: "))
numero_3 = int(input("Ingrese el valor del numero: "))

if numero_3 not in billete or numero_2 not in billete or numero_1 not in billete:
    print("El jugador tiene mala suerte, no marcó ninguna casilla")
else:
    print("El jugador marcó algún numero de la tarjeta")