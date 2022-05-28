n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))
digito = 0
while digito != 5:
    print('-=' * 20)
    print('O que quer fazer com esses numeros ?')
    print('-=' * 20)
    print(' ')
    print(''' [1] Somar \n [2] Multiplicar \n [3] Maior \n [4] Novos numeros \n [5] Sair do programa''')
    print(' ')
    digito = int(input('Digite a sua escolha:'))
    if digito == 1:
        print(f'A soma de {n1} e {n2} é =',n1 + n2)
    elif digito == 2:
        print(f'{n1} X {n2} = {n1*n2}')
    elif digito == 3:
        if n1 > n2:
            print(n1,'é o maior')
        else:
            print(n2,'é o maior')
    elif digito == 4:
        print(' ')
        n1 = int(input('Digite um numero:'))
        n2 = int(input('Digite outro numero:'))
    elif digito == 5:
        print('Fim Do Programa')
    else:
        print('Opção invalida!, Tente novamente...')