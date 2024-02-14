import re

import pandas as pd
#dataFrame
df = pd.read_csv('https://raw.githubusercontent.com/leonhgomes/Pandas/main/pokemon_data.csv')
#print(df.columns) # Acesso às colunas
#print(df.head(3)) # head = cabeça (início da tabela)
#print(df.tail(2))# tail = cauda (fim da tabela)
#Acessar Colunas individuais
#print(df['Tipo 1'])
#print(df.iloc[:4])>> i de índice loc de localizar
#print(df.loc[df['Tipo 1'] == 'Fogo'])>> Busca por nomes
'''for indice, linha in df.iterrows():
    print(indice, linha['Nome'])
    if linha ['#'] == 150:
        break'''

#novo_df = df.loc[df['Nome'].str.contains('pi$', flags=re.I,regex=True)]
#print(novo_df)

#df.loc[df['Tipo 1'] == 'Fogo','Tipo 1'] = 'Fogueteiro'
#print(df)

print(df.groupby(['Tipo 1']).mean())






