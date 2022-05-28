lista = 0
maioridadehomem = 0
nomemaisvelho = ''
totmulher20 = 0
for p in range(1, 3):
    nome = str(input('Digite seu nome:').capitalize())
    idade = int(input('Digite sua idade:'))
    sexo = str(input('Digite seu sexo (M ou F):').upper())
    lista += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20+= 0
print(f'A media de idade do grupo é de {lista/2:.0f} anos')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomemaisvelho}')
print(f'Ao todo sao {totmulher20} mulheres com menos de 20 anos')