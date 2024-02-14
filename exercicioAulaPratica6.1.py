import random

#Função valida inteiro
def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x<min) or (x> max)):
        x = int(input(pergunta))
    return x
#Função para verificar quem ganhou
def vencedor (jogador1, jogador2):
    global empate, v1, v2
    if jogador1 == 1: #Pedra
        if jogador2 == 1: #pedra
            empate += 1
        elif jogador2 == 2:#papel
            v2 += 1
        elif jogador2 == 3: #tesoura
            v1 += 1
    elif jogador1 == 2: #Papel
        if jogador2 == 1:  # pedra
            v1 += 1
        elif jogador2 == 2:  # papel
            empate += 1
        elif jogador2 == 3:  # tesoura
            v2 =+1
    elif jogador1 == 3: #Tesoura
        if jogador2 == 1:  # pedra
            v2 += 1
        elif jogador2 == 2:  # papel
            v1 += 1
        elif jogador2 == 3:  # tesoura
            empate += 1
    resultados = [v1,v2,empate]
    return resultados

#Programa Principal
print('JOKENPÔ')
print('1-PEDRA')
print('2-PAPEL')
print('3-TESOURA')

resultados = []
jogadas = []
v1 = 0 #Números de vitórias do jogador 1
v2 = 0 #Números de vitórias do jogador 2
empate = 0

while True:
        j1 = valida_int('Escolha sua jogada: ', 0,3)
        if j1 == 0: # mais arrojado seria 'if not j1'
            break
        j2 = random.randint(1,3)
        jogadas.append([j1,j2])
        resultados = vencedor(j1, j2)
        #print(vencedor(j1,j2))

        for jogada in jogadas:
            for dado in jogada:
                print(dado, end=' ')
            print()

print('Número de vitórias do j1: {}'. format(resultados[0]))
print('Número de vitórias do j2: {}'. format(resultados[1]))
print('Número de empates: {}'. format(resultados[2]))