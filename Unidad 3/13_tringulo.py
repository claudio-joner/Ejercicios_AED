cateto1 = int(input('Ingrese uno de los catetos: '))
cateto2 = int(input('Ingrese el otro cateto: '))


suma = pow(cateto1, 2) + pow(cateto2, 2)
hipotenusa = round(pow(suma, 0.5), 2)

print('\nLa hipotenusa es', hipotenusa)
print('El lado mayor es', max(cateto1, cateto2))
print('El lado menor es', min(cateto1, cateto2))