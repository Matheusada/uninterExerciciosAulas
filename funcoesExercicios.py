'''def borda(s1):   #NENHUM PROGRAMA VAI EXECUTAR A PARTIR DE UMA FUNÇÃO => VAI SE EXECUTAR PELO PROGRAMA PRINCIPAL
    print('+','-'* len(s1),'+')
    print('|',s1,'|')
    print('+','-'* len(s1),'+')

borda('Testando')''' #AQUI COMEÇA A EXECUÇÃO DO PROGRAMA ! NO PROGRAMA PRINCIPAL

def borda(s1): # Cabeçalho da função
    #só imprime caso exista algum caractere
    tam = len(s1)
    if tam:
        print('+','-'* tam, '+')
        print('|', s1,'|')
        print('+','-'* tam, '+')
#Programa principal
borda('Olá, Mundo!')
borda('Lógica de Programação e Algoritmos')
