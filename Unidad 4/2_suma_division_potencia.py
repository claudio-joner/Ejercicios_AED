num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
num3 = int(input("Numero 3: "))

suma = sum([num1,num2,num3])
resultado = 0
if suma> 10:
    resultado = int(suma/2)
else:
    resultado = suma ** 3

print("El resultado es: ",resultado)