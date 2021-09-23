#PROGRAMA DE LOGIN
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

#Len - Quantidade de caracteres
qtd_caracteres = len(usuario)
print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('Você precisa digitar pelo menos 6 caracteres.')
else:
    print('Você foi cadastrado no sistema!')