s1 = "Matheus Augusto de Azevedo"
tamanho = len(s1)
resultado = tamanho <=15
print(resultado)

print(s1[0:-3])
nota = 10.56
disciplina = "python"

print('Parabéns, você tirou {:.1f} em {}'.format(nota, disciplina))
print(f'Parabéns, você tirou {nota:.1f}')

favoriteFood = "Macarrão"
dateOfBirth= 1992
birthAge = 1992/30

print('Olá, sou Matheus, minha comida favorita é o {}, nasci em {}, e m eu ano de nascimento dividido por minha idade resulta em {}'. format(favoriteFood, dateOfBirth,birthAge))