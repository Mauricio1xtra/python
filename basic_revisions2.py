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