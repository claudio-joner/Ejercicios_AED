horario_partida = input("Ingrese el horario de partida con formato hh:MM  : ")
horario_llegada = input("Ingrese el horario de llegada con formato hh:MM : ")

hora_partida = horario_partida[0] + horario_partida[1]
min_partida = int(horario_partida[3] + horario_partida[4]) + (int(hora_partida)*60)

hora_llegada = horario_llegada[0] + horario_llegada[1]
min_llegada = int(horario_llegada[3] + horario_llegada[4]) + (int(hora_llegada)*60)

duracion_minutos = min_llegada - min_partida

hora_llegada_hotel = int((min_llegada+45)/60)
#hora_llegada_hotel = (int(min_llegada) + 45) // 60
minutos_llegada_hotel = (min_llegada+45)%60

print("Duracion del viaje en minutos: ",duracion_minutos)
print('Llega a las', (str(hora_llegada_hotel) + ':' + str(minutos_llegada_hotel)))