idades = [[2, 4, 10, 12, 22, 68], [1, 5, 9, 31, 58, 41], [3, 6, 7, 8, 13, 15, 24, 32]]

for i in range(0, len(idades)):
    for j in range(0, len(idades[i])):
        if idades[i][j] < 18:
            print(f"Você tem {idades[i][j]} anos, você é MENOR de idade. Você está na lista {i} e posição {j}")
        else:
            print(f"Você tem {idades[i][j]} anos, você é MAIOR de idade. Você está na lista {i} e posição {j}")
