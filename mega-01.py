# Primeira versão de 1988 (acho que ainda era em BASIC)
# E o jogo possivelmente era a LOTO
# A lógica segue a mesma
# Combinações apuradas: 50.063.860

mostrar = input("Mostrar, demoradamente, dados individuais (S-N): ")

cont = 0
for s1 in range(1, 56):
    for s2 in range(s1+1, 57):
        for s3 in range(s2+1, 58):
            for s4 in range(s3+1, 59):
                for s5 in range(s4+1, 60):
                    for s6 in range(s5+1, 61):
                        cont = cont + 1
                        if mostrar == "S" or mostrar == "s":
                            print(cont, " - ", s1, s2, s3, s4, s5, s6)
print("Número total de combinações: ", cont)
