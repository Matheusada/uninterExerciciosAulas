#Conceito de Escopo de variável: é a propriedade que determina onde uma variável pode ser utilizada dentro de um programa. LEMBRAR QUE O PROGRAMA SEMRRE VAI DAR PRIORIDADE PARA A VARIÁVEL QUE ESTIVER NAQUELE ESCOPO!
#Cada escopo local tem suas próprias variáveis, às vezes dois escopos locais com o nome de variáveis iguais, sem problemas !
#IMPORTANTE: INSTRUÇÃO GLOBAL => A ÚNICA MANEIRA PARA SE ALTERAR UMA VARIÁVEL GLOBAL -SEM CRIAR UMA NOVA VARIÁVEL LOCAL, É UTILIZAR A INSTRUÇÃO GLOBAL ANTES DISSO !
# veja:
'''def comida():
    ovos = 12
    print(ovos)

def mexido ():
    ovos = 24
    print(ovos)

comida()''' #Puxa o 12 de comida, mesmo tendo duas variáveis com o nome "ovos"

