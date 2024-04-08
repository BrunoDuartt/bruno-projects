from colorama import Fore, Style
import math

Tv = (f"{Fore.GREEN}esse programa tem como função de converter |KM| em |RPM| e o contrario também{Style.RESET_ALL}")# o txt vai ficar verde 

print(Tv)
print('-=-' * 50)

velocidade = input('qual a marcação você deseja usar (Km) ou (Mph)? ')

if velocidade in ["Km", "km"]:
    k = int(input("qual o valor em Km/h? "))
    vl = (k / 1.609344)
    print('A velocidade do veiculo em Mph é {:.0f} Mph'.format(vl))    

if velocidade in ["Mph", "mph"]:
    M = int(input("Qual o valor em Mph? "))
    vlm = (M * 1.609344)
    print('A velocidade em Km/h é {:.0f} Km/h'.format(vlm))

print('-=-' * 50)
tt = (f"{Fore.RED}Obrigado por usar esse programa, até mais!{Style.RESET_ALL}")# O TEXTO FICA VERMELHO
print(tt)