#CONDICIONAL COMPOSTA, LÊ UM VALOR INTEIRO E VERIFICA SE ELE É PAR OU ÍMPAR
x = int(input('Digite um valor inteiro:'))
#Cuidado com a comparação lógica que é feita pelo sinal de "=="
if (x % 2 == 0):
    print('Este número é par')
else:
     print('Este número é ímpar')