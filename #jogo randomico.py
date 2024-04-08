import random

print('=-=-=' * 45)

print('olá, esse jogo é bem simples você so tem que adivinhar qual o número que estou pensando :D')

print('=-=-=' * 45)

player = int(input('Qual valor que você acha que estou pensando? '))

N = random.randint(0, 10)

if player == N:
    print("parabéns você acertou")
else:
    print("você errou man")   
print('o número é :{}'.format(N))
