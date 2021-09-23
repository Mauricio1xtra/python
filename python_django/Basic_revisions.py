
"""
print((type("Luiz")))
print("Hello World!")

print('Mauricio', type('Mauricio'))

print(37, type(37))

print(1.70, type(1.70))

print(37 > 18, type(37 > 18))

print('Multiplicação * ', 10 * 'Mauricio')
"""


#Operadores relacionais + IF ELIF ELSE
"""
== igualdade
>= maior que ou igual a
< menor que
<= menor que ou igual a
!= diferente

"""
nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

idade = int(idade)

#Limite para pegar empréstimo
#idade_limite = 18
idade_menor = 20 #Muito jovem
idade_maior = 30 #Passou da idade

#if idade > idade_limite:
if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} NÃO pode pegar o empréstimo.')

#OPERADORES LÓGICOS
# and, not, or
# in e not in

"""
AND - Verdadeiro E verdadeiro = verdadeiro
OR - verdadeiro OU verdadeiro = verdadeiro
NOT - inversão de valores - ex: if not b > a: print('B é maior do que A.) 
else: print('A é menor do que B')
ou seja vai ser impresso A É MAIOR QUE B, mesmo não sendo.

IN - existem dentro - retorno falso o verdadeiro conforme expressão
ex: nome = "Mauricio" if "M" in nome: print("Existe") Else: print("Não Existe.")
NOT IN - não existe no texto
"""

a = 2
b = 2
c = 3

print(a == b and b < c)
print(a == b or b < c)
print(not a == b and not b < c)





#DOCUMENTAÇÃO E FUNÇÕES BUILT-IN ÚTEIS
import re

def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False

def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False

def is_number(val):
    return is_int(val) or is_float(val)

num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")

if is_number(num1) and is_number(num2):
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
else:
    print("ERROR")

#PASS E ELLIPSIS COMO PLACEHOLDER
valor = False

if valor:
    ... #ou podemos utilizar o pass,
else:
    print("Tchau")