precio = float (input("Ingrese el precio del medicamento: "))

descuento = precio * 0.35

precio_con_descuento = precio - descuento

print("Precio sin descuento: ", precio)
print("Descuento: ",round(descuento,2))
print("Precio final: ",round(precio_con_descuento,2))