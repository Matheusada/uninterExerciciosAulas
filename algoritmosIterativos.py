inicial = int(input('Digite o valor que deseja iniciar a contagem: '))
final = int(input('Digite o valor que deseja finalizar a contagem: '))
x = inicial

while (x <= final):
    if(x %2 == 0):
        print(x)
    x = (x+1)