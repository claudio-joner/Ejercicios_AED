"""
Desarrollar un programa que cargue por teclado una cadena de
aracteres que se supone representa una fecha en formato 'dd/mm/aaaa',
y muestre por separado el día, el mes y el año.
Ejemplo: si la cadena ingresada es '16/03/2016'
el programa debe mostrar: 'Día: 16  -  Mes: 03  -  Año: 2016'.

"""
from operator import concat

# fecha = str(input("Ingrese la fecha:"))
#
# dia = fecha [0:2]
# mes = fecha [3:5]
# anio = fecha[6:10]
#
# print("Dia:",dia,"| Mes:", mes,"| Anio:", anio)

"""
Desarrollar un programa que cargue por teclado un importe (cantidad de dinero) expresado como número en coma flotante y muestre un mensaje con 
esa cantidad pero en dos formatos: en uno debe 
aparecer precedida por el signo '$' y en el otro debe aparecer precedida por la palabra "pesos".
"""
valor = 1450


pesos = "$" + str(valor)
pesos_2 = concat("$",)

print(pesos_2)