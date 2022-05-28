import random
from time import sleep
num = int(input('Escolha um numero de 0 a 5 que eu vou tentar adivinhar!:'))
com = random.randint(0 , 5)
print('PROCESSANDO...')
sleep(1.5)
if num==com:
    print('voce ganhou, parabens'.capitalize())
else:
    print(f'Você perdeu!, eu pensei no {com} e não no {num}')
print('--FIM--')



