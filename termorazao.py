termo = int(input('Primeiro termo:'))
r = int(input('Razao:'))
d = termo + (10-1) * r
for c in range (termo,d, r):
    print(f'{c}', end= ' > ')
print('Acabou')


