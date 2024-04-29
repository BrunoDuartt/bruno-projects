import random
a = random.randint(1, 999)

num = int(input("número inteiro: "))
num_bi = bin(num)
print(num_bi[2:])
print(a)