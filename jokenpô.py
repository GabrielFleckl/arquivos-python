from random import choice
m = ('pedra', 'tesoura', 'papel')
variavel = choice(m)
jogador = (input('Jogador, Vamos jogar jokenpô:'))
if variavel == 'pedra' and jogador == 'pedra':
    print('EMPATE')
elif variavel == 'pedra' and jogador == 'tesoura':
    print('VOCÊ PERDEU KK')
elif variavel == 'pedra' and jogador == 'papel':
    print('VOCÊ GANHOU KK')

if variavel == 'tesoura' and jogador == 'tesoura':
    print('EMPATE')
elif variavel == 'tesoura' and jogador == 'papel':
    print('VOCÊ PERDEU')
elif variavel == 'tesoura' and jogador == 'pedra':
    print('VOCÊ GANHOU')

if variavel == 'papel' and jogador == 'papel':
    print('EMPATE')
elif variavel == 'papel' and jogador == 'tesoura':
    print('VOCÊ GANHOU')
elif variavel == 'papel' and jogador == 'pedra':
    print('VOCÊ PERDEU')