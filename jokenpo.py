'''Criando um programa que joga jokenpô com o usuário'''

#Importando a biblioteca random e time
from random import randint
from time import sleep

#definindo os itens
itens = ('Pedra', 'Papel', 'Tesoura')

#jogada do Computador
computador = randint(0,2)

#apresentando as opções
print('''Suas opções:
        [0] Pedra
        [1] Papel
        [2] Tesoura''')

#jogador escolhe a opção
jogador = int(input("Qual é sua jogada? "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ")
sleep(2)

print("-=" * 11)

#mostrando o que cada um jogou
print(f'Computador jogou: {itens[computador]}')

#Lógica do jogo - irá apresentar os resultados
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print("EMPATE!")
    elif jogador == 1:
        print("JOGADOR VENCEU!")
    elif jogador ==2:
        print("COMPUTADOR VENCEU!")
    else:
        print("JOGADA INVÁLIDA!")
elif computador == 1: #computador jogou papel
    if jogador == 0:
        print("COMPUTADOR VENCEU!")
    elif jogador == 1:
        print("EMPATE!")
    elif jogador == 2:
        print("JOGADOR VENCEU!")
    else:
        print("JOGADA INVÁLIDA!")
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print("JOGADOR VENCEU!")
    elif jogador == 1:
        print("COMPUTADOR VENCEU!")
    elif jogador == 2:
        print("EMPATE!")
    else:
        print("JOGADA INVÁLIDA!")