#Jokenpo
from time import sleep
from random import randint
print ('''bem vindo ao jogo de Jokenpo! Selecione sua opção para começar a jogar:
       
       [0] Finalizar jogo
       [1] Pedra
       [2] Papel
       [3] Tesoura''')
escolha = int(input('Escolha sua opção: '))
if escolha == 0:
    print ('Obrigado por jogar!')
    exit()
oponente = randint (1, 3)
print ('Jo')
sleep (1)
print ('Ken')
sleep (1)
print ('pô!')
sleep (1)
print ('=' * 20)

def pedra():
    if escolha == 1:
        print ('Empate! Também escolhi Pedra!')
    elif escolha == 2:
        print ('Parabens! você me venceu! Eu escolhi pedra!')
    else:
        print ('Você perdeu! Eu escolhi pedra!')

def papel():
    if escolha == 1:
        print ('Você perdeu! Eu escolhi papel!')
    elif escolha == 2:
        print ('Empate! Também escolhi papel!')
    else:
        print ('Parabens! Você me venceu! Eu escolhi papel!')

def tesoura():
    if escolha == 1:
        print ('Parabens! Você venceu! Eu escolhi tesoura!')
    elif escolha == 2:
        print ('Você perdeu! Eu escolhi tesoura!')
    else:
        print ('Empate! Também escolhi tesoura!')

def jogo():
    if oponente == 1:
        pedra()
    elif oponente == 2:
        papel()
    else:
        tesoura()

jogo()




    




