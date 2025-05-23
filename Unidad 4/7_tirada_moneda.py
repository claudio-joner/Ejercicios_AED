import random

opcion = input("Elija CARA O CRUZ: ")

moneda = ("CARA","CRUZ")

valor_aleatorio = random.randint(0,1)


if opcion.upper() == moneda[valor_aleatorio]:
    print("Acierto")
else:
    print("No Acerto")


#Otra forma usando choice
print('Tirada de la moneda')
print('=' * 80)

caras = 'cara', 'cruz'

apuesta = int(input('Seleccion que cara desea apostar (0 Cara 1 Cruz): '))
jugada = random.choice(caras)

if jugada == caras[apuesta]:
    print('El jugador ha ganado el juego, acerto, salio', jugada)
else:
    print('El jugador ha perdido el juego salio', jugada, 'y el jugador aposto a', caras[apuesta])