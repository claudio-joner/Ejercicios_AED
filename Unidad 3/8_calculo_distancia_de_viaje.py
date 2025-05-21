from idlelib.rpc import RemoteObject

TOTAL_KM = 3641.3

m = float(input("Ingrese la cantidad de kilometros: "))

km = m // 1000
metros_restantes = m % 1000
porcentaje_recorrido = round((km / TOTAL_KM) * 100,2)

print("Total de km recorridos: ",km)
print("Total de metros recorridos: ",m)
print("Porcentaje: ",porcentaje_recorrido)

"""
8. Calculo Distancia de Viaje
8.1. Solucion
print('Conversion de metros a kilimetros de viaje recorridos')
print('=' * 80)
print('\n')

distancia = 3641.3 * 1000
metros = int(input('Ingrese la cantidad de metros recorridos: '))

kilometros = metros // 1000
metros_restantes = metros % 1000

porcentaje = (x * 100) / distancia

print('El viajero recorrio ', kilometrosm , ' kilometros con ', metros_restantes, ' metros')
print('Siginifica que el viajero recorrio solo un ', porcentaje, '% del total del viaje')
"""