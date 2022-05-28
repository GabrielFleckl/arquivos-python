a=int(input("Digite um número inteiro para transforma-lo em binário: "))
#Pede o número decimal 
#string vazia para armazenar o número.
binario=""
while a!=0:
    binario= binario+str(a%2)#define se o número vai ser 0 ou 1. Depois de seu cálculo armazena o número em forma de string na variável binario fora do while 
    a= a//2#faz a divisão inteira do número solicitado até ele chegar a 0.
print(binario[::-1])#Ao final informei o número em binário(coloquei ele de trás para frente, pois ele normal indica outro número mas não o certo).