
palabra = input('Ingrese palabra a enmascarar: ')


n = len(palabra)
asteriscos = "*" * (n-2)
enmascarada = palabra[0] + asteriscos + palabra[n-1]

# Resultados
print('\nLa palabra enmascarada es:', enmascarada)