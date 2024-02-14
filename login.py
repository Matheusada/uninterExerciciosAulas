while True:
    nome = input('Digite seu nome: ')
    if (nome != 'Matheus'):
        print('Nome inválido')
        continue
    senha = input ('Digite a senha: ')
    if(senha == 'ok'):
        break
print('Acesso concedido')

