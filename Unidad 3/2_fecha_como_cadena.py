from pyexpat.errors import messages

fecha = input("Ingrese una fecha con el siguiente formato: ")

# indice= fecha.find("/")
# dia = fecha[0:fecha.find("/")]
# fecha = fecha[indice+1: len(fecha)]
# mes = fecha[0:fecha.find("/")]
# indice= fecha.find("/")
# anio = fecha[indice+1:len(fecha)]
#
# print(dia)
# print(mes)
# print(anio)



# Pedir al usuario que ingrese una fecha en formato 'dd/mm/aaaa'
fecha = input("Ingrese una fecha en formato 'dd/mm/aaaa': ")

# Variables para almacenar día, mes y año
dia = ""
mes = ""
año = ""

# Contador para identificar en qué parte estamos (día, mes o año)
parte = 0

# Recorrer la cadena caracter por caracter
for char in fecha:
    if char == '/':  # Si encontramos '/', pasamos a la siguiente parte
        parte += 1
    else:
        if parte == 0:
            dia += char
        elif parte == 1:
            mes += char
        else:
            año += char

# Mostrar los resultados
print(f"Día: {dia}  -  Mes: {mes}  -  Año: {año}")
