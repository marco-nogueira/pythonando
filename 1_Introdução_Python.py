# Variáveis e tipos de dados

# -> Receber dados
# -> Armazenar dados
# -> Processar dados
# -> Mostrar dados processados

# -> Variáveis
# -> Tipos de dados
# -> int, float, bool, str, list, tuple, set, dict

# Use # para fazer comentários na mesma linha
# Use ''' texto ''' para fazer comentários em várias linhas

# int (inteiro)
'''idade = 21
# print(idade)'''

# float (real. Tem ponto flutuante, decimal)
'''altura = 1.82
print(altura)'''

# bool (booleano)
'''verdadeiro = True
falso = False'''

# str (string. Pode ser entre aspas simples ou duplas)
# Trabalhando com string na entrada e saída de dados.
'''nome = input('Qual o seu nome: ')
print(f"Olá, {nome}!")'''

'''idade = input('Qual é a sua idade: ')
print(f'Seu nome é {nome} e você tem {idade} anos.')'''

# Conversão de dados (Para funcionar deve tirar o comentário da variável idade)
'''tipo_de_dado = type(idade)
print(f'O tipo de dado original é {tipo_de_dado}')'''
# int to string
'''dado_transformado = str(idade)
print(f'O dado foi alterado para o tipo {type(dado_transformado)}')'''
# int to float
'''dado_transformado_novamente = float(idade)
print(f'O dado foi alterado novamente, agora para o tipo {type(dado_transformado_novamente)}')'''

# Conversão de dados direto no input
'''nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
print(media)'''

# Operadores aritméticos
# + - * / ** % //
'''resultado_da_soma = 2 + 2
print(resultado_da_soma)
resultado_da_subtracao = 2 - 2
print(resultado_da_subtracao)'''

# Ordem de precedência
# 1 - ()
# 2 - **
# 3 - * / // %
# 4 - + -

'''operacao_ordem_precedencia_por_parenteses = (5 + 5 - 2) * 3
print(f'O resultado usando parenteses para precedência de operador.\nTemos que para (5 + 5 - 2) * 3 o valor igual a {operacao_ordem_precedencia_por_parenteses}')'''

'''operacao_ordem_precedencia_sem_parenteses = 5 + 5 - 2 * 3
print(f'Então o resultado não utilizando parenteses como precedência de operador. Temos apenas operador *, - e +.\nTemos que para 5 + 5 - 2 * 3 o valor será igual a {operacao_ordem_precedencia_sem_parenteses}')'''

# Operador relacional
# 5 - < > <= >= == !=
# 6 - and or not

'''operador_relacional = 1 == 1
print(operador_relacional)'''

# Operadores de atribuição
# = += -= *= /= **= //= %=

# Operadores lógicos
# 'and' 'or' 'not'

operador_logico_and = True and True
print(operador_logico_and)

operador_logico_or = 5 == 5 or 5 == 6
print(operador_logico_or)

operador_logico_not = not True
print(operador_logico_not)

operadores_logicos = not((5 == 7 or 3 > 2) and (3 == 3 or 5 < 5))
print(operadores_logicos)


# Operadores de identidade
# is

# Operadores de associação
# in

# Operadores de repetição
# *
# **
# **
# 2 ** 3 = 8
# 2 * 2 * 2 = 8

# 2 * 2 * 2 * 2 = 16
# 2 ** 4 = 16