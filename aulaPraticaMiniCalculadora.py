v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))
print('Digite 1 para operação de adição (+)')
print('Digite 2 para operação de subtração (-)')
print('Digite 3 para operação de multiplicação (x)')
print('Digite 4 para operação de divisão (/)')
print('Pressione qualquer outro número para sair')
op = int(input('Agora escolha qual operação deseja fazer:'))
if (op == 1):
    ad = v1 + v2
    print('O valor da adição entre os números é: {}'. format(ad))
elif(op == 2):
     sub = v1 -v2
     print('O valor da subtração entre os números é: {}'. format(sub))
elif(op==3):
    mult = v1 * v2
    print('O valor da multiplicação entre os números é: {}'. format(mult))
elif(op==4):
    div = v1/v2
    print('O valor da divisão entre os números é: {}'. format(div))
else:
    print('Operação inválida!')
print('Encerrando o programa...')


