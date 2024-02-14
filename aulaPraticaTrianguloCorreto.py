A = int(input('Digite o 1º lado do triângulo: '))
B = int(input('Digite o 2º lado do triângulo: '))
C = int(input('Digite o 3º lado do triângulo: '))

if (A> 0 and B>0 and C>0):
    if(A < B+C) and (B < C+A) and (C < A+B):
        if(A==B) and (A==C) and (B==C):
             print('Ora, temos um triâgulo equilátero')
        else:
            if(A != B and B!=C and C !=A):
                print('Ora, eis aqui um triângulo escaleno!')
            else:
                print('Ora, temos um triângulo isósceles')
    else:
        print('Isto não é um triângulo, pois um lado é maior ou igual que a soma dos outros dois!')
else:
    print('Isto não é um triãngulo, pois um dos lados é igual 0')