print('Digite uma mensagem que irei repeti-la para você!')
print('Para sair, basta digitar "sair"')
while True:
    texto = input('')
    print(texto)
    if texto == 'sair':
        break
print('Encerrando o programa...')