nome = input('Digite um nome: ')
idade = int(input('Digite uma idade: '))
if (nome == "Vinicius"):
    print("Vinicius")
elif (idade < 18):
    print('Você é menor de idade')
elif (idade > 100):
    print('Esta pessoa provavelmente não existe!')