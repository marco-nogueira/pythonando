# Receba 4 notas de um aluno e exiba se ele foi aprovado (nota maior ou igual a 6)
# Se ele ficou de recuperação (nota maior ou igual a 4) e menor que 6
# Se ele foi reprovado (nota menor que 4)

nota1 = float(input('Digite a nota 1: ')) 
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))
nota4 = float(input('Digite a nota 4: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

# if media >= 6:
#     print(f'Aprovado, sua média foi ${media}.')
# elif media >= 4:
#     print('Recuperação, sua média foi ${media}.')
# else:
#     print('Reprovado, sua média foi ${media}.') 

if media <= 2:
    print(f'Reprovado, sua média foi ${media}.')
elif media >= 30:
    print(f'média muito alta, sua média foi ${media}.')
elif media >= 22:
    print(f'média muito alta, sua média foi ${media}.')
else:
    print(f'nothing, sua média foi ${media}')