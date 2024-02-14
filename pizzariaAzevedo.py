print('BEM VINDO(A) À PIZZARIA DO MATHEUS AUGUSTO DE AZEVEDO')
print('-'*22 +'CARDÁPIO'+'-'*28)
print('|CÓDIGO |  DESCRIÇÃO  | PIZZA MÉDIA(M)|  PIZZA GRANDE(G) |')
print('|  21   | Napolitana  |    R$20,00    |     R$26,00      |')
print('|  22   | Margherita  |    R$20,00    |     R$26,00      |')
print('|  23   | Calabresa   |    R$25,00    |     R$32,50      |')
print('|  24   |  Toscana    |    R$30,00    |     R$39,00      |')
print('|  25   | Portuguesa  |    R$30,00    |     R$39,00      |')
print('-'*58)
acumulador = 0
while True:
    tamanho = input('Entre com o tamanho de pizza desejado (M/G): ')
    if (tamanho !='M') and (tamanho !='m') and (tamanho !='g') and (tamanho !='G'): #Em vez de colocar as duas opções, no inicio posso colocar tamanho = tamanho.upper()
        print('Opção inválida ! Digite um valor válido no tamanho!')
        continue #Se o usuário digitar algo inválido, volta paara o começo do While
    codigo = input ('Entre com o código do sabor desejado (21/22/23/24/25): ')

    if (codigo!= '21') and (codigo != '22') and (codigo != '23') and (codigo != '24') and (codigo != '25'):
        print('Opção inválida ! Digite um código válido!')
        continue #Se o usuário digitar algo inválido, volta paara o começo do While
        #PIZZA NAPOLITANA
    if (codigo == '21') and (tamanho == 'm'or tamanho == 'M'):
        print('Você escolheu a pizza Napolitana tamanho M')
        acumulador = acumulador + 20 #pegue o valor do acumulador e some com 20
    elif (codigo == '21') and (tamanho == 'g' or tamanho == 'G'):
        print('Você escolheu a pizza Napolitana tamanho G')
        acumulador = acumulador + 26
        #PIZZA MARGHERITA
    elif (codigo == '22') and (tamanho == 'm' or tamanho == 'M'):
         print('Você escolheu a pizza Margherita tamanho M')
         acumulador = acumulador + 20  # pegue o valor do acumulador e some com 20
    elif (codigo == '22') and (tamanho == 'g' or tamanho == 'G'):
         print('Você escolheu a pizza Margherita tamanho G')
         acumulador = acumulador + 26
        #PIZZA CALABRESA
    elif (codigo == '23') and (tamanho == 'm'or tamanho == 'M'):
        print('Você escolheu a pizza Calabresa tamanho M')
        acumulador = acumulador + 25 #pegue o valor do acumulador e some com 20
    elif (codigo == '23') and (tamanho == 'g' or tamanho == 'G'):
        print('Você escolheu a pizza Calabresa tamanho G')
        acumulador = acumulador + 32
        #TOSCANA
    elif (codigo == '24') and (tamanho == 'm' or tamanho == 'M'):
        print('Você escolheu a pizza Toscana tamanho M')
        acumulador = acumulador + 30  # pegue o valor do acumulador e some com 20
    elif (codigo == '24') and (tamanho == 'g' or tamanho == 'G'):
        print('Você escolheu a pizza Toscana tamanho G')
        acumulador = acumulador + 39
        #Portuguesa
    elif(codigo == '25') and (tamanho == 'm' or tamanho == 'M'):
        print('Você escolheu a pizza Portuguesa tamanho M')
        acumulador = acumulador + 30  # pegue o valor do acumulador e some com 20
    elif (codigo == '25') and (tamanho == 'g' or tamanho == 'G'):
        print('Você escolheu a pizza Prtuguesa tamanho G')
        acumulador = acumulador + 39
    pedir_mais = input('Deseja fazer mais algum pedido?(S/N):  ') #PODE-SE USAR O pedir_mais.upper()
    if(pedir_mais =='S' or pedir_mais =='s'):
        continue
    else:
        print('O valor total a ser pago é de: R${:.2f}'. format(acumulador))
        break



