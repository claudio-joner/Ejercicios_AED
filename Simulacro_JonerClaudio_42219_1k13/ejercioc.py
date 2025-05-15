# print("Sueldos y aginaldos".upper())
# print("=" * 40 )
#
# mayor,menor = 0,0
# sueldo_promedio = 0 #
#
#
# for mes in range(6):
#     sueldo = int(input("Ingrese a el sueldo:"))
#     sueldo_promedio += sueldo
#     #A
#     if sueldo > mayor:
#         mayor = sueldo
#     #B
#     if sueldo < menor or menor == 0:
#         menor = sueldo
#         mes_sueldo_bajo = mes
#
#     #C
#
#
# if mes_sueldo_bajo +1  == 1:
#     nombre_mes = "Enero"
# elif mes_sueldo_bajo +1 == 2:
#     nombre_mes = "Febrero"
# elif mes_sueldo_bajo +1 == 3:
#     nombre_mes = "Marzo"
# elif mes_sueldo_bajo +1 == 4:
#     nombre_mes = "Abril"
# elif mes_sueldo_bajo +1 == 5:
#     nombre_mes = "Mayo"
# elif mes_sueldo_bajo +1 == 6:
#     nombre_mes = "Junio"
#
#
# sueldo_promedio = sueldo_promedio / (mes + 1)
#
#
#
#
#
# print("El aguinaldo es: ", mayor/2 )
# print("El sueldo mas bajo es: ", nombre_mes)
# print("El promedio del semestre es: ",sueldo_promedio)
#
#
# # Datos y proceso
# total = 0
# primero = True
# semestre = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio")
#
# for mes in semestre:
#     sueldo = float(input("Ingrese sueldo de " + str(mes) + ": "))
#     if primero == True:
#         mayor = sueldo
#         menor = sueldo, mes
#         primero = False
#     else:
#         if sueldo > mayor:
#             mayor = sueldo
#         if sueldo < menor[0]:
#             menor = sueldo, mes
#     total += sueldo
#
# # Resultados
# aguinaldo = mayor / 2
# print("\nEl aguinaldo es de $", aguinaldo)
# print("El menor sueldo fue de $", menor[0], "y lo obtuvo en el mes de", menor[1])
# promedio = round(total / len(semestre), 2)
# print("El sueldo promedio es de $", promedio)
from os import rename

variable= ("100","200","300","400","500","600")

largo = len(variable)

print(largo)
print(variable[5])

for i in variable:
    print(i, end = " | ")

