num = p = cont = soma = maior = menor = 0
while p != 'N':
    num = int(input('Digite um número:'))
    cont += 1
    soma += num
    p = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'Você digitou {cont} numeros e a média entre eles é {soma/cont}')
print(f'O maior é {maior} e o menor é {menor}')

