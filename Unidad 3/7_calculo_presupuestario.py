presupuesto = float(input("Ingresar presupuesto: "))

presupuesto_urg = round(presupuesto * 0.37,2)
presupuesto_ped = round(presupuesto * 0.42,2)
presupuesto_trau = round(presupuesto * 0.21,2)

print("Presupuesto Urgencias: $",presupuesto_urg)
print("Presupuesto Pediatria: $",presupuesto_ped)
print("Presupuesto Traumatologia: $",presupuesto_trau)