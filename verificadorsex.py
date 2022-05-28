sexo = 1
while sexo != 'M' or 'F':
    sexo = (input('Digite seu sexo: [M/F]')).upper().strip()[0]
    if sexo == 'M':
        print('Sexo valido')
        break
    elif sexo == 'F':
        print('Sexo valido')
        break
    else:
        print('Por favor, Digite novamente!')

