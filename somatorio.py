n = 0
soma = 1
cont = -1
while n != 999:
    n = int(input('Digite um número [999 para parar]:'))
    soma += n
    cont += 1
    total = soma - 1000
print(f'Você digitou {cont} números e a soma entre eles é {total}')
