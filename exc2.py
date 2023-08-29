produtos={}

while len(produtos)<5:
    nomep= input('coloque o nome do produto: ')
    preco= float(input('coloque o preço do produto: '))
    if preco<50:
        print('O preço deve ser superio a R$ 50.00')
    else:
        produtos[nomep]=preco
        
print(f'produtos adicionados {produtos}')