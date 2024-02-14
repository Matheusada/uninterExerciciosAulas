'''mochila = ['Machado','Camisa', 'Bacon', 'Abacte']
for item in mochila:
    for letra in item:
        print(letra, end='')
    print()'''

mochila = ['Machado','Camisa', 'Bacon', 'Abacate']
for i in range(0,len(mochila),1):
    for j in range(0,len(mochila[i]),1):
        print(mochila[i][j],end='')
    print()
