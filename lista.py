#TRABALHANDO COM INDEX
print('')
vendas = [1000,5120,350,900]
produtos = ['tv', 'celular', 'mouse', 'teclado']
#vendas[2] = 200 #Modifica
print(f'Vendas do produto {produtos[1]} foram de {vendas[2]} unidades')

i = produtos.index('mouse')
qtd_estoque = vendas[i]

print(f'Quantidade em estoque do mouse e de: {qtd_estoque}')
print(produtos[i])

produto = input('Insira o nome do produto em letra miniscula ')
if produto in produtos:
    io = produtos.index(produto)
    qtd_estoque = vendas[i]
    print(f'Temos {qtd_estoque} unidades de {produto} no estoque')
else:
    print(f'{produto} Não existe no estoque')
print('')
#######################################################################

apple = ['apple tv', 'mac', 'iphone x', 'Ipad', 'apple watch', 'macbook', 'airpods']
tamanho = len(apple) #Conta o tamanho da lista
vendas2 = [1000,1500,270,900,100,1200]
mais_vendido = max(vendas2)
menos_vendido = min(vendas2)

print(apple)
#adiciona o iphone 12
apple.append('Iphone 12')
print(apple)
#remover o iphone x
produto_remover = 'iphonex'

if produto_remover in apple:
    apple.remove('iphonex')
else:
    print(f'{produto_remover} não existe na lista de produtos') 
    
print(f'Temos {tamanho} produtos')
print(f'O produto mais vendido teve {mais_vendido} unidades vendidas e o menos vendido teve {menos_vendido} unidades vendidas')

i = vendas2.index(mais_vendido)
produto_mais_vendido = apple[i]

print(produto_mais_vendido)

i = vendas2.index(menos_vendido)
produto_menos_vendido = apple[i]

print(produto_menos_vendido)
print('')
#######################################################################

produtos3 = ['S1', 'S11', 'A50', 'A30', 'S12']
novos_produtos = ['Iphone 12', 'Iphone 13']
vendas3 = [200, 10000, 3500, 800, 15000]

produtos3.extend(novos_produtos)
print(produtos3)
produtos3.sort() #ordena uma lista
print(produtos3)
vendas3.sort(reverse=True) #Ordena do menos para o maior
print(vendas3)
print(' ; '.join(produtos3))

#####################################################################
lista = ['ipad', 'iphone x', 'apple tv']
lista2 = lista.copy() #Copia uma lista

lista[1] = 'iphone 12'
print(lista)
print(lista2)
print('')
#####################################################################

vendedores = ['Lira', 'João', 'Diego', 'Alon']
produtos = ['ipad', 'iphone']
vendas = [
    [100,200],
    [300,500],
    [50,1000],
    [900,10],   
]
vendas_ipad_joao = vendas[1][0]
print(f'Lista de venda do {vendedores[1]} é {vendas_ipad_joao} unidades')
vendas_iphone = vendas[0][1] + vendas[1][1] + vendas[2][1] + vendas[3][1]
print(f'Vendas total de Iphone {vendas_iphone}')