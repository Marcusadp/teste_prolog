from pyswip import *
import random
import time

prolog = Prolog()

prolog.assertz('ganha(pedra, tesoura)')
prolog.assertz('ganha(papel, pedra)')
prolog.asserta('ganha(tesoura, papel)')
print('BEM VINDO JOGADOR!')
print('insira seu nome:')
nome = input()
print('pedra, papel ou tesoura?')
player_1 = input()
player_2 = random.sample(range(1,4), 1)
jogada = None
if player_2[0] == 1:
    jogada = 'pedra'
elif player_2[0] == 2:
    jogada = 'papel'
else:
    jogada = 'tesoura'

#time.sleep(3)
print('o bot jogou {}'.format(jogada))



if player_1 == jogada:
    print('Empatado')
else:
    resposta = bool(list(prolog.query('ganha( {} , {} )'.format(player_1, jogada))))
    if resposta:
        print('Parabens {}!'.format(nome))
        print('Você foi o ganhador!')
    else:
        print('é... voce ganhador')
