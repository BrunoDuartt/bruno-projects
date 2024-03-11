import math

def graus_para_radianos(graus):
    radianos = graus * math.pi / 180
    return radianos

graus_valores = [30, 60, 90, 180]

for graus in graus_valores:
    radianos = graus_para_radianos(graus)
    print(f"{graus} graus é igual a {radianos:.4f} radianos.")