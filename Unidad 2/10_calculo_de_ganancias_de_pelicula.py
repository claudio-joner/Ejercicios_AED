total_recaudacion = float(input("Ingrese la recaudacion total de la pelicula: "))
actor = input("Ingrese el nombre del actor: ")
porcentaje = float(input("Ingrese el porcentaje: "))

monto_a_pagar = total_recaudacion * (porcentaje/100)

print("Actor: ",actor)
print("Sueldo: ",monto_a_pagar)