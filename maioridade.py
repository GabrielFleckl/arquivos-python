from datetime import date
print('\033[33m-=-\033[m'*17)
print('\033[4:32mBEM-VINDO AO PRÉ-ALISTAMENTO DO EXERCITO BRASILEIRO\033[m ')
print('\033[33m-=-\033[m'*17)
anonasc = int(input('Qual seu ano de nascimento?:'))
idade = date.today().year - anonasc
print(f'Idade:{idade} anos')
if idade<17:
    print(f'Ainda faltam {18-idade} anos para seu alistamento, volte ao mais tardar...')
elif idade==17:
    print(f'Ainda falta 1 ano para seu alistamento, volte ao mais tardar...')
elif idade==18:
    print('''ESTA NA HORA DE CAPINAR E LAVAR A LOUÇA SOLDADO, 
    procure imediatamente uma junta militar mais proxima!!!'''.upper())
else:
    print(f'''Ja passou {idade-18} anos de se alistar, procure imediatamente uma junta militar mais proxima 
    para mais informações...''''')



