print('\n# Exemplo 1: Tratando exceções')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

try:
    print(n1/n2)
except:
    print('Não foi possível fazer a divisão')
finally:
    print('Fim do programa')
    
print('\n# Exemplo 2: Tratando exceções')
try:
    x = int(input('Digite um número: '))
    print(5/x)
except ZeroDivisionError:
    print('Não é possível dividir por zero')
except ValueError:
    print('Digite um integer')
finally:
    print('Fim do programa')
    
print('\n# Exemplo 3: Capturar e tratar exceções')
try:
    x = int(input('Digite um número: '))
    print(5/x)
except Exception as e:
    print(e)


