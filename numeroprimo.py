num = int(input('Digite um numero:'))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[33m', end=' ')
    print(c, end=' ')
print(f'\n O numero foi divisivel {tot} vezes',end=' ')
if tot ==2:
    print('e por isso ele é primo.')
else:
    print('e por isso ele nao é primo.')