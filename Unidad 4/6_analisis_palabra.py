palabra = input("Ingrese una palabra: ")
contador_letras = 0
for letra in palabra:
    if letra not in "% &/()!#|°<>='?¿¡!{}[]´*¨":
        contador_letras += 1

    if letra in "aeiuoAEIOU":
        mensaje = "La palabra que tiene vocal."
    else:
        mensaje =""

print("La cantidad de letras son: ",contador_letras)
print(mensaje)


#Solucion con bandera

print('Analisis de Palabra')
print('=' * 80)

# Lectura de datos
palabra = input('Ingrese la palabra a analizar (en mayusculas): ')

# Proceso
largo = len(palabra)
ultima_letra = palabra[largo - 1]

termina_vocal = False
if ultima_letra == 'A' or ultima_letra == 'E' or ultima_letra == 'I' or \
        ultima_letra == 'O' or ultima_letra == 'U':
    termina_vocal = True

# Salida
print('La palabra ingresada tiene una longitud de ', largo, ' letras')
if termina_vocal:
    print('La palabra ingresada termina en vocal')