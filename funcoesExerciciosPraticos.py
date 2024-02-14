'''def cont (v_final, v_inicial = 0, passo = 1):
    for i in range(v_inicial, v_final, passo):
        print('{} '. format (i), end='')
    print('\n')

cont(20,10,2)'''
'''def ordem (v1 = 0,v2 = 0,v3 = 0):
    if (v1 and v2 and v3):
        if((v1>v2) and (v1>v3)):
            if(v2>v3):
                print('A ordem crescente dos números fornecidos é : {}, {}, {}'. format(v3,v2,v1), end='')
            else:
                print('A ordem crescente dos números fornecidos é : {}, {}, {}'. format(v2,v3,v1), end='')
        elif ((v2>v1) and (v2>v3)):
            if(v1>v3):
                print('A ordem crescente dos números fornecidos é : {}, {}, {}'. format(v3,v1,v2), end='')
            else:
                print('A ordem crescente dos números fornecidos é : {}, {}, {}'. format(v1,v3,v2), end='')
        elif ((v3>v1) and v3>v2):
            if (v1> v2):
                print('A ordem crescente dos números fornecidos é : {}, {}, {}'. format(v2,v1,v3), end='')
            else:
                print('A ordem crescente dos números fornecidos é : {}, {}, {}'.format(v1, v2, v3), end='')


x = int(input('Digite o 1º número: '))
y = int(input('Digite o 2º número: '))
z = int(input('Digite o 3º número: '))

ordem(x,y,z)'''

#Validação de String
def valida (pergunta, min, max):
    s1 = input(pergunta)
    tam = len(s1)
    while ((tam < min) or (tam >max)):
        s1 = input(pergunta)
        tam = len(s1)
    return s1
x = valida('Digite uma string: ', 10,30)
print('Você digitou a string {}.\nDado válido. ENCERRANDO O PROGRAMA ...'. format(x))



