import random
#Variables
numero = (0,1,2,3,4,5,6,7,8,9)

patente= input("Ingrese patente: ")

valor_azar = random.choice(numero)
ultimo_numero = int(patente[-1])
if ultimo_numero in numero and ultimo_numero == valor_azar:
    tarifa = 50
else:
    tarifa = 90

if ultimo_numero == 7:
    tarifa_final = tarifa * 0.5
else:
    tarifa_final = tarifa * 0.9


print("La patente es:",patente)
print("Valor al azar:",valor_azar)
print("La Tarifa:",tarifa_final)
