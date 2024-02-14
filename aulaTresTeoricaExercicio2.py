tempo_trab = int(input('Qual o seu tempo de trabalho em anos: ?'))
sal = float(input('Qual o seu salário ?'))
if(tempo_trab >10):
    bonus = sal + (sal * 0.3)
    print('Trabalhador, você possui mais de 10 anos, logo seu novo salário será de R${}'.format(bonus))
else:
    if (tempo_trab >5):
        bonus = sal + (sal * 0.2)
        print('Trabalhador, você possui mais de 5 anos, logo seu novo salário será de R${}'.format (bonus))
    else:
        bonus = sal + (sal * 0.1)
        print('Trabalhador, você possui menos de 5 anos, logo seu novo salário será de R${}'.format(bonus))
