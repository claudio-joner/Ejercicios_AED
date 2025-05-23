import random

palo = ("E","B","O","C")
numero =("1","2","3","4","5","6","7","10","11","12")
contador = 0
for p in palo:
    for valor in numero:
        print(valor+p)
        contador += 1


print(contador)

print("-"*30+"GENERACION CARTAS"+"-"*30)

bandera_as_esp = False
bandera_1ra_vuelta = True
bandera_iguales = False

mayor = None
for i in range(3):
    carta = numero[random.randint(0,9)] + palo[random.randint(0,3)]
    if carta == "1E":
        bandera_as_esp = True

    if bandera_1ra_vuelta and mayor is None:
        carta_1 = carta
        bandera_1ra_vuelta = False
        mayor = carta_1
    elif not(bandera_1ra_vuelta):
        carta_2 = carta
        bandera_1ra_vuelta = True

if carta[-1] == carta_1[-1]:
    bandera_iguales = True
    valor_carta = int(carta[0:len(carta)-1])
    valor_carta_1 = int(carta_1[0:len(carta_1)-1])
    if valor_carta > valor_carta_1:
        mayor = carta
    else:
        mayor = carta_1
elif carta[-1] == carta_2[-1]:
    bandera_iguales = True
    valor_carta = int(carta[0:len(carta)-1])
    valor_carta_2 = int(carta_2[0:len(carta_2)-1])
    if valor_carta > valor_carta_2:
        mayor = carta
    else:
        mayor = carta_2
elif carta_1[-1] == carta_2[-1]:
    bandera_iguales = True
    valor_carta_1 = int(carta_1[0:len(carta_1)-1])
    valor_carta_2 = int(carta_2[0:len(carta_2)-1])
    if valor_carta_2 > valor_carta_1:
        mayor = carta_2
    else:
        mayor = carta_1


print("Las cartas son: ",carta_1,carta_2,carta)
if bandera_as_esp:
    print("Tiene el AS de ESPADAS")
if bandera_iguales :
    print("La carta mayor es : ", mayor)



