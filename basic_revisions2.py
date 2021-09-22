"""
Formatando valores com modificadores - AUlA 5

:s - Texto (strings)
:d - Inteiro (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

"""
num_1 = 1
print(f"{num_1:0>10}")

num_2 = 2 
print(f"{num_2:0^10}")
print(f"{num_2:0>10.2f}")

nome = "Mauricio"
sobrenome = "Ferreira"
print(f'{nome:#^50}') #Add cerquinha 
print((50-len(nome)) / 2) #subtrai 50 - qtde de caracteres da função nome e divide por 2
#Na primeira situação estamos passando o indice do sobrenome(1)
nome_formatado = "{1:+^50}".format(nome, sobrenome) #{:*^50}".format(nome) ou "{n:0>20}".format(n=nome)
print(nome_formatado)
"""

#MINIPULANDO STRINGS - AULA 6
"""
*String indices
*Fatiamento de strings [inicio:fim:passo]
*Funções Built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.
"""

#Positivos [012345678]
texto = "Python s2"
#Negativos -[987654321]

nova_string = texto[2:6] #[0::2] pega o caractere do inicio ao fim, pulando 2 casas
print(nova_string)


"""
While em Python = AULA 7
Utilizando para realizar ações enquanto
uma condição for verdadeira

requisitos: Entender condições e operadores
"""
"""
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue #ou break para o loop quando a condição é verdadeira

    print(x)
    x = x + 1

print("Acabou!")
"""

"""
x = 0
while x < 10:
    y = 0
        print(f"({x}, {
    while y < 5:
        print(f"({x},{y})")
        y += 1

    x += 1 # x = x + 1

print("Acabou!")
"""

#Calculadora
while True:
    print()
    num_1 = input("Digite um número: ")
    num_2 = input("Digite outro número: ")
    operador = input("Digite um operador: ")
    sair = input("Deseja sair? [s]im ou [n]ão: ")

    if sair == "s":
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print("Você precisa digitar um número.")
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    # + - / *
    if operador == "+":
        print(num_1 + num_2)
    elif operador == "-":
        print(num_1 - num_2)
    elif operador == "/":
        print(num_1 / num_2)
    elif operador == "*":
        print(num_1 * num_2)
    else:
        print("Operador invalido!")

"""WHILE / ELSE - AULA 8
Contadores
Acumuladores
"""
#!CONTADOR
contador = 0 #pode começar a partir de qualquer número, ex: contador = 50

# while contador <= 100:
#     print(contador)
#     contador += 1

#!ACUMULADOR
contador_1 = 1
acumulador = 1

while contador_1 <= 10:
    print(contador_1, acumulador)
    
    if contador_1 > 5:
        break #TODO: quando colocamos o BREAK o ELSE não será executado, ele sai do bloco de código

    acumulador = acumulador + contador_1
    contador_1 += 1
else:
    print("Cheguei no else.")
print("Isso será executado!")

