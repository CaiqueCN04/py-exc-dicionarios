dados_alunos= {}

while len(dados_alunos):
    ra= int(input('informe seu RA: '))
    notas=[]
    for i in range(3):
        notas=float(input(f'nota {i+1}: '))
        notas.append(notas)
        dados_alunos[ra]=notas
print(dados_alunos)

for rm, lista in dados_alunos.items():
    media= sum(notas)/ len(notas)
    print(f'{ra} {round(media, 2)}')


