#PRIMEIRA TENTATIVA RESOLUÇÃO EXERCÍCIO EM PYTHON DO TRIÂNGULO, AUSÊNCIA CLARA DO RACIOCÍNIO LÓGICO
print('Vamos verificar se os valores formam um triângulo e qual seria sua classificação: ')
lado1 = int(input('Digite o valor do primeiro lado: '))
lado2 = int(input('Digite o valor do segundo lado: '))
lado3 = int(input('Digite o valor do terceiro lado: '))
if (lado1 ==0 or lado2 ==0 or lado3 ==0):
    print('Isto não é um triângulo, meu pequeno gafanhoto')
elif (lado1 > lado2 + lado3 or lado2 > lado1 + lado3 or lado3 > lado2 + lado1):
    print('Isto não é um triângulo, meu pequeno gafanhoto')
elif(lado1 == lado2 and lado1== lado3 and lado2==lado3):
    print('Ora, temos três lados iguais, logo triângulo equilátero')
elif (lado1==lado2 and lado3 != lado2 or lado3==lado2 and lado1 != lado2 and lado1==lado3 and lado3 != lado2):
    print('Ora, ora... temos um triâgunlo isósceles')
elif (lado1 != lado2 and lado1 != lado3 and lado3 != lado2):
    print('Interessante... 3(três) lados DIFERENTES, temos um triângulo escaleno')


