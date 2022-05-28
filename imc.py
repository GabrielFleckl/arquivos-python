peso = float(input('Quanto você pesa?:'))
altura = float(input('Quanto você tem de altura?:'))
imc = peso/(altura*altura)
if imc < 18.5:
    (print('Abaixo do peso'))
elif imc <= 18.5 or imc < 24.9:
    print('Peso ideal')
elif imc < 24.9 or imc < 29.9:
    print('Sobrepeso')
elif imc < 29.9 or imc < 39.9:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade morbida')
print(imc)
