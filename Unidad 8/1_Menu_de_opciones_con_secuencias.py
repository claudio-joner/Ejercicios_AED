# mensaje = "LAS OPCIONES SON -A:Calculo de suma de cuadrados -B:Contar cantidad de Palabras -C:Mayo impar o par -D:Salir"
#
# opciones = input("Ingrese una opcion: ").upper()
# concatenador = ""
# while opciones != "D":
#     if (opciones == "A"):
#         print("Opcion A ")
#     elif (opciones == "B"):
#         texto = input("Ingrese el texto, debe finalizar en . ")
#         while texto[-1] != ".":
#             concatenador +=" " + texto
#             texto = input("Ingrese el texto, debe finalizar en . ")
#
#         print(concatenador)
#     elif (opciones == "C"):
#         print("Opcion A ")
#     else:
#         print("Opcion Incorrecta.")
#
#     opciones = input("Ingrese una opcion: ").upper()
#
# print("Saliendo del menu")
#
from http.client import HTTPException

texto = "mundo."

print(texto)

print(texto[0:len(texto)-1])