COSTO =  20

monto = float(input("Ingrese el monto del dinero a depositar: "))

monto_final = monto *1.023 - COSTO

print("El interes generado sera de: ", round(monto_final,2))
