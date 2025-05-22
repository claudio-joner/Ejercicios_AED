# #Variables
# acu_seg = 0
#
# print("------------------PRIMER VALOR--------------------")
#
# grados = int(input("Ingresar los valores de grados: "))
# minutos = int(input("Ingresar los valores de minutos: "))
# segundos = int(input("Ingresar los valores de segundos: "))
#
# # 1 grado = 60 minutos  | 1 min = 60 segundos
# grados = grados * 3600
# minutos = minutos * 60
# acu_seg = segundos + minutos + grados
#
# print("------------------SEGUNDO VALOR--------------------")
#
# grados = int(input("Ingresar los valores de grados: "))
# minutos = int(input("Ingresar los valores de minutos: "))
# segundos = int(input("Ingresar los valores de segundos: "))
#
# # 1 grado = 60 minutos  | 1 min = 60 segundos
# grados = grados * 3600
# minutos = minutos * 60
# acu_seg += segundos + minutos + grados
#
#
# #Proceso
# grados = int(acu_seg/3600)
# minutos = int((acu_seg - (grados * 3600))/60)
# segundos = acu_seg - (grados *3600 + minutos* 60)
#
# print(str(grados) +"°")
# print(str(minutos)+"\"")
# print(str(segundos)+"\'")
#


# Sumador angulos
# RESOLUCION CON TUPLAS (I)

print('*' * 30)
print('   Sumador de Angulos')
print('*' * 30)

print('Ingrese el primer angulo:')
grados_a1 = int(input('\tGrados:   '))
minutos_a1 = int(input('\tMinutos:  '))
segundos_a1 = int(input('\tSegundos: '))
angulo1 = (grados_a1, minutos_a1, segundos_a1)

print('Ingrese el segundo ángulo:')
grados_a2 = int(input('\tGrados:   '))
minutos_a2 = int(input('\tMinutos:  '))
segundos_a2 = int(input('\tSegundos: '))
angulo2 = (grados_a2, minutos_a2, segundos_a2)

print()
seg_totales_a1 = angulo1[2] + angulo1[1] * 60 + angulo1[0] * 60**2
seg_totales_a2 = angulo2[2] + angulo2[1] * 60 + angulo2[0] * 60**2

seg_totales_suma = seg_totales_a1 + seg_totales_a2

print()
grados_suma = seg_totales_suma // 60**2
segundos_restantes = seg_totales_suma % 60**2
minutos_suma = segundos_restantes // 60
segundos_suma = segundos_restantes % 60

resultado = (grados_suma, minutos_suma, segundos_suma)
resultado_cadena = str(resultado[0]) + "g " + str(resultado[1]) + '\' ' + str(resultado[2]) + '"'

print('* Resultados')
print('* El ángulo resultante: ', '\n*\t', resultado_cadena)
