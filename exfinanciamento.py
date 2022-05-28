valorcasa = float(input('Qual o valor da \033[4;34mcasa\033[m?:R$').strip())
salario = float(input('Qual é o seu \033[4;34msalario\033[m mensal?:R$').strip())
tempo = int(input('Em quantos \033[4;34manos\033[m você pretende pagar?:').strip())*12
valormes = valorcasa/tempo
if valormes >= salario*30/100:
    print(f'\033[31;4mPEDIDO NEGADO...\033[m \nSua parcela mensal de {valormes:.2f} excedeu 30% do seu salario ({salario*30/100:.2f})\nassim não podendo concluir seu pedido...')
else:
    print('PARABENS!!! Seu financiamento foi \033[4;32maprovado!\033[m ')
    print(f'Valor mensal a ser pago:R${float(valormes):.2f}')







