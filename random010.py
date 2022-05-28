import random
cont = 0
num = 0
com = random.randint(1, 11-1)
print(com)
while num != com:
    num = int(input('Escolha um numero de 0 a 10 que eu vou tentar adivinhar!:'))
    if num==com and cont > 0:
        print(f'Voce ganhou, parabens!!, e precisou de {cont} tentativas...', end=' ')
    if num != com:
        cont += 1
    if num == com and cont == 0:
        print(f'Voce ganhou, parabens!!')
    else:
        print(random.choice(['Tente denovo !', 'Esta perto!']))
        continue

