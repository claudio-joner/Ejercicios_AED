espalda = 52*100 + 15
pecho = 62*100 + 75
mariposa = 59*100 + 80
crol = 48*100 + 15

total = espalda + pecho + mariposa + crol

minutos = total // 6000 # 1 min = 60seg  1seg= 100cent  1min = 6000cent
resto = total % 6000

segundos = resto // 100
centesimas = resto % 100

print('Total:', minutos, 'minutos', segundos, 'segundos y', centesimas, 'centesimas')