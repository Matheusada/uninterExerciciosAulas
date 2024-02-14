mat1 = float(input('Digite a nota da primeira matéria: '))
mat2 = float(input('Digite a nota da segunda matéria: '))
mat3 = float(input('Digite a nota da terceira matéria: '))
mTotal = (mat1+mat2+mat3/3)
if (mTotal >= 7):
    print('Parabéns, foi aprovado!')
else:
    print('Estude mais, você não alncançou a média 7!')

# RESOLUÇÃO COM BASE NO PROFESSOR: A NOTA DE CADA MATÉRIA DEVE SER > 7
mat1 = float(input('Digite a nota da primeira matéria: '))
mat2 = float(input('Digite a nota da segunda matéria: '))
mat3 = float(input('Digite a nota da terceira matéria: '))
if (mat1 >= 7 and mat2 >= 7 and  mat3>=7):
    print('Parabéns, foi aprovado!')
else:
    print('Estude mais, você não alncançou a média 7!')






