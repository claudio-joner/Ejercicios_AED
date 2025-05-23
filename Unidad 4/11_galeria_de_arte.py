print('GALERÍA DE ARTE')
cuadro1 = int(input('Ingrese año de creación del cuadro 1: '))
cuadro2 = int(input('Ingrese año de creación del cuadro 2: '))
cuadro3 = int(input('Ingrese año de creación del cuadro 3: '))

# Proceso
# Todos los cuadros son anteriores al siglo XX?
mensaje_sxx = ' son anteriores al siglo XX'
if cuadro1 < 1900 and cuadro2 <= 1900 and cuadro3 <= 1900:
    mensaje_sxx = 'TODOS' + mensaje_sxx
else:
    mensaje_sxx = 'NO TODOS' + mensaje_sxx

# Alguno fue creado en cierto año?
anio = int(input('\nIngrese año de creación a buscar: '))
mensaje_anio = ' hay cuadros correspondientes al año ' + str(anio)
if cuadro1 == anio or cuadro2 == anio or cuadro3 == anio:
    mensaje_anio = 'SÍ' + mensaje_anio
else:
    mensaje_anio = 'NO' + mensaje_anio

# Diferencia entre más nueva y más antigua
nueva = max(cuadro1, cuadro2, cuadro3)
antigua = min(cuadro1, cuadro2, cuadro3)
diferencia = nueva - antigua

nueva = 0
antigua = 0

#Version con IF anidados
if cuadro1 > cuadro2 and cuadro1> cuadro3:
    nueva = cuadro1
    if cuadro2 > cuadro3:
        antigua = cuadro3
    else:
        antigua = cuadro2
elif cuadro2 > cuadro1 and cuadro2> cuadro3:
    nueva = cuadro2
    if cuadro1 > cuadro3:
        antigua = cuadro3
    else:
        antigua = cuadro1
elif cuadro3 > cuadro2 and cuadro3> cuadro1:
    nueva = cuadro3
    if cuadro1 > cuadro2:
        antigua = cuadro1
    else:
        antigua = cuadro2

#Version IF y min y max
if cuadro1 >= cuadro2 and cuadro1 >= cuadro3:
    nueva = cuadro1
    antigua = min(cuadro2, cuadro3)
elif cuadro2 >= cuadro1 and cuadro2 >= cuadro3:
    nueva = cuadro2
    antigua = min(cuadro1, cuadro3)
else:
    nueva = cuadro3
    antigua = min(cuadro1, cuadro2)


# Resultados
print(mensaje_sxx)
print(mensaje_anio)
print('La diferencia entre la obra más nueva (', nueva, ') y la más antigua (', antigua, ') es', diferencia, 'años')