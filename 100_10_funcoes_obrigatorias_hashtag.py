#https://youtu.be/NB9pdUDNAJ4?si=WcQidprTB-Ny_2eB
# Hashtag
# 00:00 Introdução
# 00:44 Função Print (+ parâmetros)
# 04:18 Função Help (ajuda)
# 07:14 Função Range (intervalo)
# 11:17 Função Map (+ lambda)
# 16:05 Função Filter (filtro)
# 17:48 Função Sum (soma)
# 18:59 Função Sorted (ordenação)
# 23:00 Função Enumerate (índice do item)
# 25:34 Função Zip (juntar listas)
# 28:18 Função Open/With Open (escrever/ler arquivo)
# 34:36 Conclusão

import time

# FUNÇÃO 1 - temporizador regressivo
# print("Contagem")
# for i in range(5):
#     print(5 - i, end="\r")
#     # print(5 - i, end="\n")
#     time.sleep(1)
# print("Acabou!")

# ou usando range:
# for i in range(5, 0, -1):
#     print(i, end="\r")
#     time.sleep(1)

# FUNÇÃO 2 -  help    
# help(print)

# def calcular_imposto(faturamento, taxa):
#     """
#     faturamento (floar): o faturamento da empresa que vamos calcular o imposto
#     taxa (flota): a taxa percentual de imposto sobre o faturamento (ex: 0.2)
    
#     returns: imposto, faturamento_liquido
#     imposto (float): valor total do imposto calculado sobre o faturamento
#     faturamento_liquido (float): quanto sobrou do faturamento depois de descontao o imposto
#     """
#     imposto = faturamento * taxa
#     return imposto, faturamento - imposto

# help(calcular_imposto)

# FUNÇÃO 3 - ramge
# lista = list(range(5))
# lista = list(range(1, 6))
# lista = list(range(1, 10, 2))
# lista = list(range(5, 0, -1))
# print(lista)

# FUNÇÃO 4 - map - Executar uma função sobre cada um dos valores da lista:
# salarios = [1000, 2000, 750, 850, 1100]

# def aumentar_salario(salario):
#     if salario > 1000:
#         novo_salario = salario * 1.1
#     else:
#         novo_salario = salario * 1.2
#     return novo_salario

# # usando uma função map
# novos_salarios = list(map(aumentar_salario, salarios))
# print(novos_salarios)

# # usando uma função lambda
# novos_salarios = list(map(lambda salario: salario * 1.1, salarios))
# print(novos_salarios)

# FUNÇÃO 5 - função filter
# salarios = [1000, 2000, 750, 850, 1100]

# salarios_altos = list(filter(lambda x: x > 1000, salarios))
# print(salarios_altos)

# FUNÇÃO 6 - função soma
custos = [600, 5000, 350, 4000]

# custo_total = sum(custos)
# custo_total = sum(custos, start=1000)
# print(custo_total)

# FUNÇÃO 7 - função sorted
# exemplo 1
# salarios = [1000, 5000, 7000, 850]
# salarios_ordenados = sorted(salarios)
# print(salarios_ordenados)
# salarios_ordenados = sorted(salarios, reverse=True)
# print(salarios_ordenados)

# exemplo 2
# salarios_mais_bonus = [
#     (1000, 500, 180),
#     (5000, 40, 200),
#     (7000, 0, 0),
#     (850, 4000, 150)
#     ]
# # usando o sort, ordena pelo primeiro item
# funcionarios_ordenados = sorted(salarios_mais_bonus, reverse=True)
# print(funcionarios_ordenados)
# # usando o sort com o parametro key, fazendo o sort pela soma dos valores
# funcionarios_ordenados = sorted(salarios_mais_bonus, reverse=True, key=lambda x: sum(x))
# print(funcionarios_ordenados)

# FUNÇÃO 8 - função enumerate
# salarios = [1000, 5000, 7000, 850]
# funcionarios = ["lira", "alon", "amanda", "marcus"]

# for salario in salarios:
#     print(salario)
    
# for i, salario in enumerate(salarios):
#     funcionario = funcionarios[i]
#     print(f"Funcionário: {funcionario}, Salário: {salario}")

# FUNÇÃO 9 - função zip
# salarios = [1000, 5000, 7000, 850]
# funcionarios = ["lira", "alon", "amanda", "marcus"]

# for funcionario, salario in zip(funcionarios, salarios):
#     print("O novo salário do ",funcionario," é ",salario * 1.1)
    
# dict_salarios = dict(zip(funcionarios, salarios))
# print(dict_salarios)

# FUNÇÃO 10 - função open
salarios = [1000, 5000, 7000, 850]
funcionarios = ["lira", "alon", "amanda", "marcus"]

# arquivo = open("salario_funcionarios.txt", "w", encoding="utf-8")

# for funcionario, salario in zip(funcionarios, salarios):
#     arquivo.write(f"Novo salário do {funcionario} é {salario * 1.1}\n")
# arquivo.close()

# arquivo = open("salario_funcionarios.txt", "r", encoding="utf-8")
# texto = arquivo.read()
# print("Texto do arquivo: ")
# print(texto)
# arquivo.close()

# recomendado
# with open("salario_funcionarios.txt", "r", encoding="utf-8") as arquivo:
#     texto = arquivo.read()
# print("Texto do arquivo: ")
# print(texto)    

# append
# recomendado
with open("salario_funcionarios.txt", "a", encoding="utf-8") as arquivo:
    texto = arquivo.read()
print("Texto do arquivo: ")
print(texto)    