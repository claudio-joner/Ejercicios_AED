jornada = input("Ingrese una opc: 1- representa Diurno y 2- representa Nocturno ")
horas_trabajadas =  int(input("Ingrese la cantidad de horas trabajadas: "))

if jornada == 2:
    sueldo = horas_trabajadas * 40.6
elif jornada == 1:
    sueldo = horas_trabajadas * 35.5
else:
    print("Opción Incorrecta.")

print("El sueldo es: ", sueldo)