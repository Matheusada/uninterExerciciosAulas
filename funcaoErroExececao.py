#No erro de exceção a SINTAXE está correta, o problema ocorre durante a execução do programa, normalmente devido a um dado digitado de maneira inválida e não tratado durante o programa;
#TRATANDO UMA EXCEÇÃO
'''while True: #AQUI NEM FOI CRIADA FUNÇÃO
    try:
        x = int(input('Por favor digite um número: '))
        break
    except ValueError:
        print('Oops! Número inválido. Tente novamente...')'''

def div():
    try:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite um número: '))
        res = num1/num2
    except ZeroDivisionError:
        print('Oops! Erro de divisão por zero...')
    except:
        print('Algo de errado aconteceu...')
    else:
        return res
    finally:
        print('Executará sempre!')
print(div())