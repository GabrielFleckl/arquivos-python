from datetime import date
import time
print('='*32)
print('\033[34mCONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[m')
print('='*32)
anonasc = int(input('Qual seu \033[4mano\033[m de nascimento?:').strip())
print('\033[1;37mPROCESSANDO...\033[m')
time.sleep(1)
idade = date.today().year - anonasc
if idade <= 9:
    print('\033[1;34mCategoria:Mirim.\033[m')
elif idade <= 14:
    print('\033[1;34mCategoria:Infantil.\033[m')
elif idade <= 19:
    print('\033[1;34mCategoria:Junior.\033[m')
elif idade <= 25:
    print('\033[1;34mCategoria:Sênior.\033[m')
else:
    print('\033[1;34mCategoria:Master.\033[m')

