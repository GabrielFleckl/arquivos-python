maiortempo=0
menortempo=99999
maratonistas = int(input("Digite o numero de maratonistas:"))
for c in range(maratonistas):
    tempomaratonista = int(input(f"Quanto tempo (em minutos) o maratonista {c+1} terminou a maratona?:"))
    if c == maratonistas:
        maiortempo = c
        menortempo = c
    else:
        if tempomaratonista < menortempo:
            menortempo = tempomaratonista

print(f"O menor tempo de maratona foi de {menortempo/60:.2f} horas.")

