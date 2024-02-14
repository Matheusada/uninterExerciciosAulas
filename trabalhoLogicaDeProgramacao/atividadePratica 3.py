#início da Função cachorro_peso()
def cachorro_peso():
    while True:
        try:
            peso = int(input('Entre com o peso do cachorro (KG): '))
            if (peso < 3):
                return + 40
            elif (peso >= 3) and (peso < 10):
                return + 50
            elif (peso >= 10) and (peso < 30):
                return + 60
            elif (peso >= 30) and (peso < 50):
                return + 70
            else:
                print('Pare de digitar valores inválidos para peso!')
        except ValueError: #ACASO O USUÁRIO INCAUTO UTILIZAR-SE DE UMA LETRA OU UM NÚMERO DECIMAL
            print('Pare de digitar valores não inteiros ou que são letras!')
#fim da Função cachorro_peso()

#início da Função cachorro_pelo()
def cachorro_pelo():
    while True:
        opcao_pelo = input('Qual das opções de pelo tem seu Pet?\n' +
                           'C- CURTO\n'+
                           'M- MÉDIO\n'+
                           'L-LONGO\n'+ '>>')
        opcao_pelo = opcao_pelo.upper()
        opcao_pelo = opcao_pelo.strip()
        if opcao_pelo == 'C':
            return 1.00
        elif opcao_pelo == 'M':
            return 1.5
        elif opcao_pelo == 'L':
            return 2.0
        else:
            print('Pare de digitar opções diferentes de C, M ou L')
            continue #RETORNA PARA A PERGUNTA/INÍCIO DO LAÇO
#fim da Função cachorro_pelo()

#início da Função cachorro_extra()
def cachorro_extra():
    acumulador = 0
    while True:
        extra = input('Deseja qual serviço extra?\n' +
                        '0- Não desejo nenhum ou mais nenhum extra (ENCERRAR SERVIÇO)\n' +
                        '1- Cortar as unhas do cachorro - R$ 10,00\n' +
                        '2- Escovar os dentes do cachorro - R$ 12,00\n' +
                        '3- Limpar as orelhas do cachorro - R$ 15,00\n'+
                        '>>')
        if extra == '0':
            return acumulador
        elif extra =='1':
            acumulador += 10
            continue #Volta para o início do While
        elif extra =='2':
            acumulador += 12
            continue  # Volta para o início do While
        elif extra =='3':
            acumulador += 15
            continue  # Volta para o início do While
        else:
            print('Pare de digitar opções diferentes de 0,1,2 e 3!')
#fim da Função cachorro_extra()

#INÍCIO DO MAIN (PRINCIPAL)
print('SEJA BEM-VINDO(A) AO PET SHOP DO MATHEUS AUGUSTO DE AZEVEDO')
peso = cachorro_peso()
print('OBA !!!! Recebemos o peso do seu cachorro, o valor base do serviço é de R${}'. format(peso))
pelo = cachorro_pelo()
extra = cachorro_extra()
total = peso * pelo + extra
print('O valor total ficou em : R$ {:.2f}, sendo que:\n >> Pelo peso (KG) do cachorro: R$ {:.2f}\n >> Tipo de pelo: R$ {:.2f}\n >> Serviços extras : R$ {:.2f}'.format(total, peso, pelo, extra))