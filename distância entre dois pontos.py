#distância entre dois pontos

import math


def calcular_distancia(ponto1, ponto2):
    x1, y1 = ponto1
    x2, y2 = ponto2
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia


ponto1 = (1, 1)
ponto2 = (3, 4)
print(f"Distância entre {ponto1} e {ponto2}: {calcular_distancia(ponto1, ponto2)}")

ponto1 = (0, 0)
ponto2 = (10, 10)
print(f"Distância entre {ponto1} e {ponto2}: {calcular_distancia(ponto1, ponto2)}")

ponto1 = (2, 7)
ponto2 = (20, 30)
print(f"Distância entre {ponto1} e {ponto2}: {calcular_distancia(ponto1, ponto2)}")