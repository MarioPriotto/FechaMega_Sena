# Elaborado pela primeira vez em 1988

cont = 0
for s1 in range(1, 55):
    for s2 in range(s1+1, 56):
        for s3 in range(s2+1, 57):
            for s4 in range(s3+1, 58):
                for s5 in range(s4+1, 59):
                    for s6 in range(s5+1, 60):
                        cont = cont + 1
                        print(cont, " - ", s1, s2, s3, s4, s5, s6)
