# """
# Según la Ley Electoral de la República Argentina, el Presidente y el Vicepresidente se eligen de acuerdo a las siguientes reglas:
#
# Artículo 149. — Resultará electa la fórmula que obtenga más del cuarenta y cinco por ciento (45 %) de los votos afirmativos válidamente emitidos; en su defecto,
# aquella que hubiere obtenido el cuarenta por ciento (40 %) por lo menos de los votos afirmativos válidamente emitidos y, además, existiere una diferencia mayor
# de diez puntos porcentuales respecto del total de los votos afirmativos válidamente emitidos, sobre la fórmula que le sigue en número de votos.
#
# Artículo 150. — Si ninguna fórmula alcanzare esas mayorías y diferencias de acuerdo al escrutinio ejecutado por las Juntas Electorales, y
# cuyo resultado único para toda la Nación será anunciado por la Asamblea Legislativa atento lo dispuesto por el artículo 120 de la presente ley,
# se realizará una segunda vuelta dentro de los treinta (30) días.
#
# Artículo 151. — En la segunda vuelta participarán solamente las dos fórmulas más votadas en la primera, resultando electa la que obtenga mayor
# número de votos afirmativos válidamente emitidos.
#
# Desarrollar un programa que permita ingresar, para los 3 partidos más votados: fórmula (presidente + vice) y cantidad de votos obtenidos.
#
# Luego determinar:
#
# Qué fórmula obtuvo el mayor porcentaje.
# Si la fórmula resulta elegida o se requiere segunda vuelta. En este caso, indicar también quienes participan de la segunda vuelta.
# """
#
#
# #Partidos y porcentajes de votos
# formula1 = input("ingrese la formula 1 (Presidente+Vice): ")
# votos1 = int(input("ingrese el cantidad de votos obtenidos de la 1ra formula:"))
#
# formula2 = input("ingrese la formula (Presidente+Vice): ")
# votos2 = int(input("ingrese el cantidad de votos obtenidos de la 2da formula:"))
#
# formula3 = input("ingrese la formula (Presidente+Vice): ")
# votos3 = int(input("ingrese el cantidad de votos obtenidos de la 3ra formula:"))
#
# votosTotales = votos1 + votos2 + votos3
#
# porcentaje1 = (votos1 * 100) / votosTotales
#
# porcentaje2 = (votos2 * 100) / votosTotales
#
# porcentaje3 = (votos3 * 100) / votosTotales
#
# diferencia1 = 10 >= porcentaje1 - porcentaje3 and porcentaje1 - porcentaje2 >= 10
# diferencia2 = 10 >= porcentaje2 - porcentaje3 and porcentaje2 - porcentaje1 >= 10
# diferencia3 = 10 >= porcentaje3 - porcentaje1 and porcentaje3 - porcentaje2 >= 10
#
#
# if porcentaje1 >= 45:
#     mensaje = formula1
# elif(porcentaje2 >= 45):
#     mensaje = formula2
# elif(porcentaje3 >= 45):
#     mensaje = formula3
# #2da parte del 149
# elif porcentaje1 >= 40 or porcentaje2 >= 40 or porcentaje3 >= 40:
#     #if porcentaje1 >= 0.40 and 0.1 >= porcentaje1 - porcentaje2 and porcentaje1 - porcentaje3 >= 0.1:
#     if diferencia1:
#         mensaje = formula1
#     elif diferencia2:
#         mensaje = formula2
#     elif diferencia3:
#         mensaje = formula3
# else:
#     print("Segunda vuelta")
#     menorSegunda = ""
#     if (porcentaje1 < porcentaje2 and porcentaje1 < porcentaje3 ):
#         #menorSegunda = formula1
#         mensajeSegundaVuelta2 = formula2
#         votos2 = int(input("ingrese el cantidad de votos obtenidos de la 2da formula:"))
#
#         mensajeSegundaVuelta3 = formula3
#         votos3 = int(input("ingrese el cantidad de votos obtenidos de la 3ra formula:"))
#
#         totalVotos = votos2 + votos3
#         p2 = (votos2 *100) / totalVotos
#         p3 = (votos3 / totalVotos) * 100
#
#         if (p2 > p3):
#             mensaje = mensajeSegundaVuelta2
#         else:
#             mensaje = mensajeSegundaVuelta3
#     else:
#         if (porcentaje2 < porcentaje3):
#             #menorSegunda = formula3
#             mensajeSegundaVuelta1 = formula1
#             votos1 = int(input("ingrese el cantidad de votos obtenidos de la 1ra formula:"))
#
#             mensajeSegundaVuelta3 = formula3
#             votos3 = int(input("ingrese el cantidad de votos obtenidos de la 3ra formula:"))
#
#             totalVotos = votos1 + votos3
#             p1 = (votos1 * 100) / totalVotos
#             p3 = (votos3 / totalVotos) * 100
#
#             if (p1 > p3):
#                 mensaje = mensajeSegundaVuelta1
#             else:
#                 mensaje = mensajeSegundaVuelta3
#
#         else:
#             #menorSegunda = formula3
#             mensajeSegundaVuelta2 = formula2
#             votos2 = int(input("ingrese el cantidad de votos obtenidos de la 2da formula:"))
#
#             mensajeSegundaVuelta1 = formula1
#             votos1 = int(input("ingrese el cantidad de votos obtenidos de la 1ra formula:"))
#
#             totalVotos = votos1 + votos2
#             p1 = (votos1 * 100) / totalVotos
#             p2 = (votos2 / totalVotos) * 100
#             if (p1 > p2):
#                 mensaje = mensajeSegundaVuelta1
#             else:
#                 mensaje = mensajeSegundaVuelta2
#
# print("La formula ganadora es: ",mensaje)
#
#
#
#
#     # if (porcentaje1 < porcentaje2 and porcentaje1 < porcentaje3 ):
#     #     menorSegunda = formula1
#     # elif (porcentaje2 < porcentaje1 and porcentaje2 < porcentaje3 ):
#     #     menorSegunda = formula2
#     # #if (porcentaje3 < porcentaje2 and porcentaje3 < porcentaje1  ):
#     # else:
#     #     menorSegunda = formula3
#
#

menor = 0
segundo_menor = 0

for i in range(0,4):
    numero = int(input("Ingrese el numero: "))

    if numero == 0:
        menor = numero
        segundo_menor = numero
    elif numero < menor :
        segundo_menor = menor
        menor = numero
    elif menor < segundo_menor :
        segundo_menor = numero






print("El menor es: ", menor)
print("El 2do menor es: ", segundo_menor)