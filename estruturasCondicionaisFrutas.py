print('Escolha o que deseja comprar: ')
print('1- Banana')
print('2- Maça')
print('3- Laranja')
produto= int(input('Qual dessas frutas deseja ? Digite o nº: '))
quantidade= int(input('Qual a quantidade desejada ?'))
if (produto == 1):
    total = quantidade * 1.85
    print('Você comprou {} bananas, totalizando : R${:.2f}'. format(quantidade, total))
else:
    if (produto == 2):
        total = quantidade * 2.30
        print('Você compru {} maças, totalizando: R${:.2f}'. format(quantidade, total))
    else:
        if (produto ==3):
            total= quantidade * 3.60
            print('Você compri {} laranjas, totalizando: R${:.2f}'. format(quantidade,total))
        else:
            print('Produto inexistente!')



