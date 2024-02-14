print('Seja bem-vindo(a) à empresa atacadista do Matheus Augusto de Azevedo') #Lembrete do Nome do aluno
valor_produto = float(input('Informe o preço unitário do produto : R$')) # Preço UNITÁRIO do produto que o usuário entra
qtd_produto = int(input('Informe a quantidade de produtos desejados: '))
if (qtd_produto < 200):  #O pção de vários prints para especificicação na mensagem da quantidade de produtos escolhidos
    valor_com_desconto = (valor_produto - (valor_produto * 0.00)) * qtd_produto
    print('Menos de 200 produtos, NÃO HÁ desconto, logo o preço fica R$ {:.2f}'.format(valor_com_desconto))
elif(qtd_produto >= 200 and qtd_produto <1000):#elif = else+if
    valor_com_desconto = (valor_produto - (valor_produto * 0.05)) * qtd_produto
    valor_sem_desconto = valor_produto * qtd_produto
    print('Entre 200 e abaixo de 1000 produtos, o preço COM desconto fica R$ {:.2f}'.format(valor_com_desconto))
    print('SEM DESCONTO ficaria R$ {:.2f}'. format (valor_sem_desconto))
elif(qtd_produto >= 1000 and qtd_produto <2000):
    valor_com_desconto = (valor_produto - (valor_produto * 0.10)) * qtd_produto
    valor_sem_desconto = valor_produto * qtd_produto
    print('Entre 1000 e abaixo de 2000 produtos, o preço COM desconto fica R$ {:.2f}'.format(valor_com_desconto))
    print('SEM DESCONTO ficaria R$ {:.2f}'. format (valor_sem_desconto))
else:
    valor_com_desconto = (valor_produto - (valor_produto * 0.15)) * qtd_produto
    valor_sem_desconto = valor_produto * qtd_produto
    print('Igual ou mais de 2000 produtos, o preço COM desconto fica R$ {:.2f}'.format(valor_com_desconto))
    print('SEM DESCONTO ficaria R$ {:.2f}'.format(valor_sem_desconto))
print('A empresa agradece a sua visita! Volte sempre!') #Atenção a indentação do print


