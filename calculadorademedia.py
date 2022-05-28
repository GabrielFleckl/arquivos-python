import time
print('='*28)
print('\033[32mSIMULADOR DE MEDIA SEMESTRAL\033[m')
print('='*28)
n1 = float(input('Digite a nota do seu \033[4;34mPrimeiro Semestre:\033[m'))
n2 = float(input('Digite a nota do seu \033[4;34mSegundo Semestre:\033[m'))
media = (n1+n2)/2
print('\033[1;37mPROCESSANDO...\033[m')
time.sleep(2)
if media<5.0:
    print('\033[31;1mStatus:REPROVADO.\033[m')
elif media == 5.0 or media < 6.9:
    print('\033[33;1mStatus:EM RECUPERAÇÃO.\033[m')
elif media > 7.0:
    print('\033[32;1mStatus:APROVADO!!!\033[m')










