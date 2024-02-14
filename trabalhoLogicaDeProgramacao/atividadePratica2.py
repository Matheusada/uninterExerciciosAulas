print('BEM VINDO(A) À SORVETERIA DO MATHEUS AUGUSTO DE AZEVEDO')
print('-'*25 +'CARDÁPIO'+'-'*31)
print('| Nº BOLAS |  TRADICIONAL(TR)|   PREMIUM (PR)  |  ESPECIAL(ES) |')
print('|    1     |     R$ 6,00     |     R$7,00      |    R$8,00     |')
print('|    2     |     R$ 11,00    |     R$13,00     |    R$15,00    |')
print('|    3     |     R$ 15,00    |     R$18,00     |    R$21,00    |')

print('-'*64)
acumulador = 0
while True:
    sabor = input('Entre com o sabor de sorvete desejado (TR/PR/ES) : ')
    sabor = sabor.upper() #ACASO O USUÁRIO INCAUTO UTILIZAR-SE DE LETRAS MINÚSCULAS
    if (sabor !='TR') and (sabor !='PR') and (sabor !='ES'): #Em vez de colocar as duas opções, no inicio posso colocar sabor = sabor.upper()
        print('Opção inválida ! Por favor, digite um sabor válido!')
        continue #Se o usuário digitar algo inválido, volta paara o começo do While
    n_bolas = input ('Entre com o Nº de bola(s) desejada(s)(1/2/3): ')

    if (n_bolas != '1') and (n_bolas != '2') and (n_bolas != '3'):
        print('Quantidade de Bolas de Sorvete Inválida ! Digite um número válido!')
        continue #Se o usuário digitar algo inválido, volta paara o começo do While

        #SABOR TRADICIONAL
    if (sabor == 'TR') and (n_bolas == '1'):
        print('Você escolheu o sabor Tradicional com 1(uma)bola')
        acumulador = acumulador + 6 #pegue o valor do acumulador e some com 20
    elif (sabor == 'TR') and (n_bolas == '2'):
        print('Você escolheu o sabor Tradicional com 2(duas)bolas')
        acumulador = acumulador + 11
    elif (sabor == 'TR') and (n_bolas == '3'):
        print('Você escolheu o sabor Tradicional com 3(três)bolas')
        acumulador = acumulador + 15

        #SABOR PREMIUM
    if (sabor == 'PR') and (n_bolas == '1'):
        print('Você escolheu o sabor Premium com 1(uma)bola')
        acumulador = acumulador + 7 #pegue o valor do acumulador e some com 20
    elif (sabor == 'PR') and (n_bolas == '2'):
        print('Você escolheu o sabor Premium com 2(duas)bolas')
        acumulador = acumulador + 13
    elif (sabor == 'PR') and (n_bolas == '3'):
        print('Você escolheu o sabor Premium com 3(três)bolas')
        acumulador = acumulador + 18

        #SABOR ESPECIAL
    if (sabor == 'ES') and (n_bolas == '1'):
        print('Você escolheu o sabor Especial com 1(uma)bola')
        acumulador = acumulador + 8  # pegue o valor do acumulador e some com 20
    elif (sabor == 'ES') and (n_bolas == '2'):
        print('Você escolheu o sabor Especial com 2(duas)bolas')
        acumulador = acumulador + 15
    elif (sabor == 'ES') and (n_bolas == '3'):
        print('Você escolheu o sabor Especial com 3(três)bolas')
        acumulador = acumulador + 21

    pedir_mais = input('Deseja fazer mais algum pedido?(S/N):  ') #PODE-SE USAR O pedir_mais.upper()
    pedir_mais = pedir_mais.upper()
    if(pedir_mais =='S'):
        continue
    else:
        print('O valor total a ser pago é de: R${:.2f}'. format(acumulador))
        break



