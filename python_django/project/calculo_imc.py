nome = input("Qual o seu nome?\n")
idade = input("Qual a sua idade?\n")
altura = input("Qual a sua altura?\n")
peso = input("Qual o seu peso?\n")

idade = int(idade)
altura = float(altura)
peso = float(peso)

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