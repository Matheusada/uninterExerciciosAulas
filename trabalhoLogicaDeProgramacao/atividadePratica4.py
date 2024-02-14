#--------------------------Início das Variáveis Globais--------------------------
lista_colaborador = []
id_global = 0
#--------------------------FIM das Variáveis Globais-----------------------------

#--------------------------Início de cadastrar_colaborador(id)-------------------
def cadastrar_colaborador(id):
    print('Bem-vindo ao menu de Cadastro do Colaborador')
    print('Código do Colaborador: {}.'.format(id))
    nome = input('Entre com o nome do colaborador: ')
    setor = input('Entre com o setor do colaborador: ')
    pagamento = float(input('Entre com o pagamento do colaborador: '))
    dicionario_colaborador = {'id':            id,
                              'nome':          nome,
                              'setor':         setor,
                              'pagamento(R$)': pagamento}
    lista_colaborador.append(dicionario_colaborador.copy())
#--------------------------FIM de cadastrar_colaborador(id)----------------------

#--------------------------Início de consultar_colaborador()---------------------
def consultar_colaborador():
    print('Bem-vindo ao menu de Consulta do Colaborador')
    while True:
        opcao_consultar = input('\nEscolha a opção desejada:\n' +
                                '1-Consultar todos Colaboradores\n' +
                                '2-Consultar por ID\n' +
                                '3-Consultar por Setor\n' +
                                '4-Retornar ao Menu  \n' +
                                '>>>>')
        if opcao_consultar == '1':  # MELHOR FAZER O TRATAMENTO COM STRING PARA FACILITAR/ com inteiros, precisaria colocar exceções
            print('Você escolheu a opção consultar TODOS os colaboradores')
            for colaborador in lista_colaborador:#Colaborador vai varrer a lista toda de colaboradores
                print('-'*20)
                for key, value in colaborador.items(): #Varrer todos os conjuntos chave e valor do dicionário colaborador
                    print('{}: {}'. format(key,value))
                print('-' * 20)
        elif opcao_consultar == '2':
            print('Você escolheu a opção consultar por ID')
            id_desejado= int(input('Entre com o ID desejado: '))
            for colaborador in lista_colaborador:
                if colaborador['id'] == id_desejado: #O valor do campo código(dicionário) = valor desejado?
                    print('-' * 20)
                    for key, value in colaborador.items():  # Varrer todos os conjuntos chave e valor do dicionário colaborador
                        print('{}: {}'.format(key, value))
                    print('-' * 20)
        elif opcao_consultar == '3':
            print('Você escolheu a opção consultar por SETOR')
            id_desejado = input('Entre com o SETOR desejado: ')
            for colaborador in lista_colaborador:
                if colaborador['setor'] == id_desejado:  # O valor do campo código(dicionário) = valor desejado?
                    print('-' * 20)
                    for key, value in colaborador.items():  # Varrer todos os conjuntos chave e valor do dicionário colaborador
                        print('{}: {}'.format(key, value))
                    print('-' * 20)
        elif opcao_consultar == '4':
            return  # OPÇÃO MAIS ELEGANTE, SAI DA FUNÇÃO CONSULTAR e volta para o MAIN
        else:
            print('Opção inválida! Tente novamente, por favor!')
            continue  # Volta para o início do laço
#--------------------------FIM de consultar_colaborador()------------------------

#--------------------------Início do remover_colaborador()-----------------------
def remover_colaborador():
    print('Bem-vindo ao menu de Remoção de Colaborador')
    id_desejado = int(input('Entre com o ID do colaborador que deseja remover: '))
    for colaborador in lista_colaborador:
        if colaborador['id'] == id_desejado:  # O valor do campo código(dicionário) = valor desejado?
            lista_colaborador.remove(colaborador)
            print('\nColaborador Removido com SUCESSO!')
#--------------------------FIM remover_colaborador()-----------------------------

#--------------------------Início do MAIN-------------------
print('Seja bem-vindo(a) ao programa de gerenciamento de pessoas do Matheus Augusto de Azevedo')
while True:
    opcao_principal = input('\nEscolha a opção desejada:\n' +
                           '1-Cadastrar Colaborador\n' +
                           '2-Consultar Colaborador\n' +
                           '3-Remover Colaborador(es)\n' +
                           '4-Sair \n' +
                           '>>>>')
    if opcao_principal == '1': #MELHOR FAZER O TRATAMENTO COM STRING PARA FACILITAR/ com inteiros, precisaria colocar exceções
        id_global += 1
        cadastrar_colaborador(id_global)
    elif opcao_principal =='2':
        consultar_colaborador()
    elif opcao_principal =='3':
        remover_colaborador()
    elif opcao_principal =='4':
        break #Encerra o laço principal, acabando o programa
    else:
        print('Opção inválida! Tente novamente, por favor!')
        continue #Volta para o início do laço

#--------------------------FIM do MAIN----------------------