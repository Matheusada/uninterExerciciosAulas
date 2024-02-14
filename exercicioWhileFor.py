#algoritmo que calcule a média dos núemros pares de 1 até 100 (1 e 100 inclusos)
#1º usando for
'''soma = 0
qtd = 0
for i in range(1,101,1): #o passo, 3º parâmetro é opcional, já que o 1 é padrão
    if(i % 2 == 0):
        soma += i
        qtd += 1
media = soma/qtd
print('A média dos pares de 1 até 100 é: {}'. format(media))'''

#2º utilizando while

'''cont = 0
soma = 0
qtd = 0

while (cont <100):
    cont = cont + 1
    if (cont % 2 == 0):
        soma = soma + cont
        qtd = qtd + 1
print('A média dos pares de 1 até 100 é : {}'. format (soma/qtd))'''
'''i = 100
while (i <= 999):
   print(i)
   i += 10'''
'''def div2 (num , den):
   res = num / den
   print(res)

div2(3,10)'''
numeros = (10, 15, 20, 25, 30)
for numero in numeros:
   print(numero)



