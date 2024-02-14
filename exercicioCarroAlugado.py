kmPercorrido = int(input('Quantos Kilômetros foram percorridos com o veículo?'))
quantDias = int(input('Por quantos dias o carro foi alugado?'))
precoTotal= 0.15 * kmPercorrido + 60 * quantDias
print('O total a pagar é: %.2f' % (precoTotal))