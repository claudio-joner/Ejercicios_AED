from multiprocessing.spawn import prepare

temp_1 = float(input("Ingrese temperatura 1: "))
temp_2 = float(input("Ingrese temperatura 2: "))
temp_3 = float(input("Ingrese temperatura 3: "))

promedio = (temp_3+temp_1+temp_2)/3
mayor = temp_1 > promedio or temp_2 > promedio or temp_3 > promedio
if  mayor:
    mensaje = "Si existe una temperatura mayor"
else:
    mensaje = "No existe una temperatura mayor."
    
print("El promedio es:", promedio)
print(mensaje)