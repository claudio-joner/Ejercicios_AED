"""
1. Complejo de cines
Desarrollar un programa que permita procesar funciones de un complejo de cines. Por cada función se conoce: cantidad de espectadores y
descuento (S/N). La carga termina cuando la cantidad de espectadores sea igual a 0 (cero).

El programa deberá:
a) Calcular la recaudación total del complejo, considerando que el valor de la entrada es de $50 en los días con descuento y $75 en los días sin descuento.

b) Determinar cuántas funciones con descuento se efectuaron y qué porcentaje representan sobre el total de funciones.
"""

cantidad_espectadores = int(input("Ingrese la cantidad de espectadores: "))

total = 0
contador_cantidad_total_funciones= 0
contador_cantidad_funciones_descuento  = 0


while  cantidad_espectadores !=0 :
    descuento = input("La función tiene descuento, Si: S o No: N ")
    if "s" == descuento.lower():
        precio = 50 * cantidad_espectadores
        contador_cantidad_funciones_descuento +=1 # cumple la condicion, funcoin tenga descuento
    else:
        precio = 75 * cantidad_espectadores

    contador_cantidad_total_funciones += 1 # Es una funcion


    porcentaje = (contador_cantidad_funciones_descuento / contador_cantidad_total_funciones) * 100
    # Parte A
    total += precio # total = total + precio
    cantidad_espectadores = int(input("Ingrese la cantidad de espectadores: "))


print("Resultado parte A:", total )
print("Resultado parte B: Porcentaje: ", porcentaje , "| Total: ", contador_cantidad_total_funciones  )