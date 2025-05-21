votos_a_favor = int(input("Ingrese la cantidad de votos a favor: "))
votos_en_contra = int(input("Ingrese la cantidad de votos en contra: "))

total = votos_en_contra + votos_a_favor
porcentaje_a_favor = (votos_a_favor /total )*100
porcentaje_en_contra = (votos_en_contra /total )*100

print("Porcentaje a favor: ",round(porcentaje_a_favor,2))
print("Porcentaje en contra: ",round(porcentaje_en_contra,2))