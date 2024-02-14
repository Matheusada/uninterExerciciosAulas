#EXERCICIO 1 (contagem de 10 a 1000 utilizando o while)
'''x = 10
while (x <= 1000):
    print(x)
    x = x + 1'''

#lançamento foguete
'''x = 10
while (x >= 0 ):
    print(x)
    x = x - 1
print('FOGO!')'''

#Usuário escolhe intervalo (Pares)
'''v_inicial = int(input('Escolha o valor que deseja iniciar a contagem: '))
v_final = int(input('Escolha o valor que deseja finalizar a contagem: '))
x = v_inicial
while(x <= v_final):
    if (x % 2 == 0):
        print(x)
    x = x + 1'''
'''v_inicial = int(input('Escolha o valor que deseja iniciar a contagem: '))
v_final = int(input('Escolha o valor que deseja finalizar a contagem: '))
x = v_inicial
while(x <= v_final):
    if (x % 3 == 0):
        print(x)
    x = x + 1'''

#Exercicio de tabuada
'''valor = int(input('Escolha o número que deseja ver a TABUADA: '))
cont = 0
while (cont <= 10):
    print('{} x {} = {}' .format(valor, cont, valor * cont))
    cont += 1''' #TUDO DEPENDE DA ORDEM !!!!


#exercício soma 5 números escolhidos pelo usuário
'''soma = 0
cont = 1
while (cont <= 5):
    valor = int(input('Digite o {}º valor: '. format(cont)))
    cont += 1
    soma += valor #variável acumuladora
print ('O somatório dos números é: {} '. format(soma))'''

#Algoritmo que leia dois valores e imprima na tela o resultado da multiplicação de ambos (usando somente adição/subtração)
#Multiplicação como somatório sucessivo
'''v1 = int(input('Digite o 1º valor: '))
v2 = int(input('Digite o 2ºvalor: '))
cont = 1
mult = 0
while (cont <= v1):
    mult = mult + v2
    cont = cont + 1
print('Resultado  da multiplicação: {} x {} = {}'. format(v1, v2, mult))'''

#Valor inicial e final fornecido pelo usuário
#mostrar: a) qtd de números inteiros positivos b) qtd de nº pares c) ímpares d)a respectiva média de cada um dos itens
'''inicio = int(input('Digite o número que deseja iniciar o intervalo: '))
fim = int (input('Digite o número que deseja finalizar o intervalo: '))
cont = inicio
qtd_positivo = 0
qtd_pares = 0
qtd_impares = 0
soma_positivo = 0
soma_pares = 0
soma_impares = 0
if (inicio < fim):
    while (cont <= fim ):
        cont += 1
        if (cont > 0):
            qtd_positivo = qtd_positivo + 1
            soma_positivo = qtd_positivo + cont
        if (cont %3 == 0):
            qtd_impares = qtd_impares + 1
            soma_impares = qtd_impares + cont
        else:
            qtd_pares = qtd_pares + 1
            soma_pares = qtd_pares + cont
    print('A quantidade de números pares é de {} e a média deles é {}'. format(qtd_pares, soma_pares/qtd_pares))
    print('A quantidade de números ímpares é de {} e a média deles é {}'.format(qtd_impares, soma_impares/qtd_impares))
    print('A quantidade de números inteiros positivos é de {} e a média deles é {}'.format(qtd_positivo, soma_positivo/qtd_positivo))
else:
    print('Digite um valor válido para início')'''

'''cont = 0
soma = 0
valor = 0
while True:
    valor = int(input('Digite o valor:'))
    if (valor < 0) :
        continue
    if (not valor):
        break
    cont += 1
    soma += valor
print('DIGITOU 0')
print('E a média dos valores digitados é de: {}.' .format(soma/cont))'''

'''frase = 'Lógica de Programação e algoritmos'
for i in range(0, len(frase), 1):
    print(frase[i], end ='')'''

'''idade = int(input('Qual a sua idade?'))
while(idade > 0):
    sexo = input('Qual é o seu sexo ?(M OU F)')
    if (sexo == 'M') or (sexo == 'm'):
        print('Seja bem-vindo, senhor !')
    else:
        print('Seja bem-vinda, senhora')
    idade = int(input('Qual a sua idade?')) #PULO DO GATO AQUI, MESMA IDENTAÇÃO (HIERARQUIA DO IF/ELSE)
    # Se não coloca a idade aqui, vai parar no sexo e não idade !!!!!!'''
#Números primos 2 até 99 ( colocando na tela todos eles)
#utilizando while (como são de quantidade definida mais fácil seria o for)

'''n = int(input('Digite um número inteiro: '))
count = int(0)
i = int(0)

while (i <= n or count < 2):
  i += 1
  x = n % i
  if (x == 0):
    count += 1

if (count <= 2):
  print('É primo')
else:
  print('Não é primo')'''
'''for i in range(3,13,1):
  print(i)'''
'''x = 3
while (x < 13):
    print(x)
    x += 1'''
'''for i in range(0,9,2):
    print(i)'''
'''i = 0
while(i < 9):
    print(i)
    i += 2'''

'''print('VIRTUAL CAIXA ELETRÔNICO')
valor = int(input('Digite o valor que deseja sacar em R$: '))
while True:
    if (valor > 100):
        cedulas100 = valor//100
        valor = valor - (cedulas100 *100)
        print('Serão {} cédulas de R$100'.format(cedulas100))
        if not valor:
            break
    if (valor >= 50):
        cedulas50 = valor//50
        valor = valor - (cedulas50 *50)
        print('Serão {} cédulas de R$100'.format(cedulas50))
        if not valor:
            break
    if (valor >=20):
        cedulas20 = valor//20
        valor = valor - (cedulas20 *20)
        print('Serão {} cédulas de R$20'.format(cedulas20))
        if not valor:
            break
    if (valor >= 10):
        cedulas10 = valor//10
        valor = valor - (cedulas10 *10)
        print('Serão {} cédulas de R$10'.format(cedulas10))
        if not valor:
            break
    if (valor >= 5):
        cedulas5 = valor//5
        valor = valor - (cedulas5 *5)
        print('Serão {} cédulas de R$100'.format(cedulas5))
        if not valor:
            break
    if valor:
        print('Serão {} cédulas de R$1'.format(valor))
        break'''

#<3 gratuito
#>=3 e <= 12 15
#>12 30

'''idade = int (input ('Qual a sua idade ? \nPara sair digite "0"'))
while (idade != 0):
    if (idade < 3):
        print('O ingresso é gratuito!')
        ingresso3 = input('Deseja ganhar o ingresso?(S/N): \nPara sair digite "sair": ')
        if (ingresso3 =='S') or (ingresso3 =='s'):
            qtd_3 = int(input('Quantos ingressos gratuitos?: '))
            print('Parabéns, você adquiriu {} ingressos gratuitos'. format(qtd_3))
            break
        else:
            print('Agradecemos sua visita!')
            break
    if (idade >= 3) and (idade <= 12):
        print('O ingresso custa R$ 15,00!')
        ingresso10 = input('Deseja comprar o ingresso?(S/N): \nPara sair digite "sair": ')
        if (ingresso10 =='S') or (ingresso10 =='s'):
            qtd_10 = int(input('Quantos ingressos de R$ 15,00: '))
            print('Parabéns, você adquiriu {} ingressos no valor de R$15,00, totalizando R${:.2f}'.format(qtd_10, (qtd_10 * 15)))
        else:
            print('Agradecemos sua visita!')
            break
    if(idade >12):
        print('O ingresso custa R$ 30,00!')
        ingresso30 = input('Deseja comprar o ingresso?(S/N): \nPara sair digite "sair": ')
        if (ingresso30 =='S') or (ingresso30 =='s'):
            qtd_30 = int(input('Quantos ingressos de R$ 30,00: '))
            print('Parabéns, você adquiriu {} ingressos no valor de R$30,00, totalizando R${:.2f}'.format(qtd_30, (
                        qtd_30 * 30)))
            break

print('Agradecemos sua visita !')'''
total = 0 #tem que ser antes do laço, pois ela deve ser 0
dinheiro = 0

while True:
    idade = input('Qual a sua idade? ') #Aqui nao se usa o int, pois estamos com o 'sair' de break
    if idade == 'sair':
        break
    idade = int(idade)
    total += 1
    if (idade < 3):
        ingresso = 0
    else:
        if(idade >12):
            ingresso = 30
        else:
            ingresso = 15
    dinheiro += ingresso
media= dinheiro/total
print ('Total de pessoas: {}'. format(total))
print ('Total arrecadado {}'. format(dinheiro))
print ('media arrecada: {}'. format(media))
















