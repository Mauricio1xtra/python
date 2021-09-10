"""
print((type("Luiz")))
print("Hello World!")

print('Mauricio', type('Mauricio'))

print(37, type(37))

print(1.70, type(1.70))

print(37 > 18, type(37 > 18))

print('Multiplicação * ', 10 * 'Mauricio')
"""

nome = 'Luiz'
idade = 34
altura = 1.80
#e_maior = idade > 18
peso = 80
imc = peso / (altura **2)
ano_atual = 2021
ano_nasc = ano_atual - idade

print(f'{nome} tem {idade} anos, {altura} e pesa {peso}kg')
print(f'O IMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {ano_nasc}')

#print(nome, 'tem', idade, 'anos', 'de idade e seu imc é:', imc)
#print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
#print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
#print('{n} tem {i} anos de idade e seu imc é {im:.2f}'.format(n=nome, i=idade, im=imc))
"""
print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', e_maior)
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


#Programa de login
usuario = input('Nome de usuário: ')
senha = input('Digite sua senha: ')

usuario_bd = 'mauricio'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado!')
elif usuario_bd == usuario and senha_bd != senha:
    print('Senha inválida.')
elif usuario_bd != usuario and senha_bd == senha:
    print('Usuário inválido')
else:
    print('Usuário ou senha inválidos.')