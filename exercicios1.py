
#AULA 28
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro,
informe que não é um número inteiro.
"""
num_inteiro = input("Digite um número inteiro: ")

if not num_inteiro.isdigit():
    print("Isso não é um número inteiro, digite novamente.")
else:
    num_inteiro = int(num_inteiro)
    if not num_inteiro % 2 == 0:
        print(f"{num_inteiro} é ímpar!")
    else:
        print(f"{num_inteiro} é par!")


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação
apropriada. Ex. Bom dia 0-11, Boa tarde 12:17 e Boa noite 18-23.
"""
horario = input("Digite a hora: ")
minuto = input("Digite o minuto: ")

if horario.isdigit():
    horario = int(horario)
    minuto = int(minuto)

    if horario < 0 or horario > 23:
        print("Horario deve estar entre 0 e 23h")
    else:
        if horario <= 11 and minuto <= 59:
            print(f"{horario}:{minuto} - Bom dia!")
        elif horario <=17 and minuto <= 59:
            print(f"{horario}:{minuto} - Boa tarde")
        else:
            print(f"{horario}:{minuto} - Boa noite!")
else:
    print("Por favor, digite um horario entre 0 e 23h.")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos, escreva " Seu nome é curto!" se tiver entre 5 e 6 letras, escreva
"Seu nome é normal!"; maior que 6 escreva "Seu nome é muito grande!".
"""
nome = input("Digite o seu nome: ")
tamanho = len(nome)

if tamanho <= 4:
    print(f"{nome}, seu nome é curto!")
elif tamanho <= 6:
    print(f"{nome}, seu nome é normal!")
else:
    print(f"{nome}, seu nome é muito grande!")