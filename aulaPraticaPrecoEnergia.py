print('Cálculo do preço de energia elétrica')
kwh = float(input('Qual a quantidade de kWh consumida?'))
tipInst = input('1-r (para residências) \n2-i (para indústrias)) \n3-c (para comércios) \n Selecione o tipo de instalação: ')
if (tipInst == 'r'):
    if (kwh <= 500):
        valor = kwh * 0.40
        print('O valor total a pagar para residencial será de R${:.2f}'. format(valor))
    else:
        valor = kwh * 0.65
        print('O valor total a pagar para residencial será de R${:.2f}'.format(valor))
elif(tipInst == 'c'):
        if (kwh <=100):
            valor = kwh * 0.55
            print('O valor total a pagar para comercial será de R${:.2f}'. format(valor))
        else:
            valor = kwh * 0.60
            print('O valor total a pagar para comercialserá de R${:.2f}'.format(valor))
elif(tipInst == 'i'):
        if(kwh <=5000):
            valor = kwh * 0.55
            print('O valor total a pagar para industrial será de R${:.2f}'.format(valor))
        else:
            valor = kwh * 0.60
            print('O valor total a pagar para industrial será de R${:.2f}'.format(valor))
else:
    print('Selecione uma opção válida!')
