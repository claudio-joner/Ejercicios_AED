

AUMENTO = 8/100
DESCUENTO = 2.5/100

nombre_empleado = input("Ingrese el nombre del empleado: ")
area_funcional = input("Ingrese el nombre del area funcional a la que pertenece: ")
sueldo = float(input("Ingrese el sueldo del empleado: "))

nuevo_sueldo = sueldo * (1 + AUMENTO - DESCUENTO)

print("Nombre Empleado: ",nombre_empleado," "*5,"Nuevo Salario $",round(nuevo_sueldo,2))
#print('Nombre empleado:', nombre, '\t\tNuevo sueldo $:', nuevo_sueldo)
print("Área funcional: ",area_funcional)
print("Salario Actual: $",sueldo)