ano_nascimento = int(input('digite seu ano de nascimento: '))
ano_atual = int(input('Digite o ano em que se encontra: '))
idade = (ano_atual - ano_nascimento)
print('Sua idade no ano atual de {} é de: {} anos'.format(ano_atual, idade))
if (idade >= 18):
    print('Parabéns, já pode ter carteira!')
else:
    print('Infelizmente ainda não pode tirar carteira')



