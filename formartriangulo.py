r1 = int(input('Reta um:'))
r2 = int(input('Reta dois:'))
r3 = int(input('Reta três:'))
p = r1+r2>r3, r1+r3>r2, r2+r3>r1
print(p)
if p == (True, True, True):
    print("é possivel")
else:
    print('Não é possivel')






