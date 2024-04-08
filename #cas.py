#cas
import math
import random

N = input("nome: ")
I = input("idade: ")
P = input("peso: ")

N1 = N[0] + N[1]
I1 = I[1] + I[0]
P1 = str(P)
R = random.randint (0, 9)
P2 = P[1] + P[0]

print(N1, I1, P1, R, P2, sep='' )

