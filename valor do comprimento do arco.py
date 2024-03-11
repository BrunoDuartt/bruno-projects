import math

pi = 3.14

def calcular_comprimento_arco(angulo, raio):
    
    angulo_radianos = math.radians(angulo)
    
    comprimento_arco = (angulo_radianos / 360) * (2 * pi * raio)
    
    return comprimento_arco

angulo1, raio1 = 30, 5
angulo2, raio2 = 45, 6
angulo3, raio3 = 60, 8

print(f"Para α = {angulo1}° e r = {raio1}: Comprimento do arco = {calcular_comprimento_arco(angulo1, raio1)}")
print(f"Para α = {angulo2}° e r = {raio2}: Comprimento do arco = {calcular_comprimento_arco(angulo2, raio2)}")
print(f"Para α = {angulo3}° e r = {raio3}: Comprimento do arco = {calcular_comprimento_arco(angulo3, raio3)}")