mais_vendidos = {
    'tecnologia': 'iphone',
    'refrigeração': 'ar consul 1200 btu',
    'livros': 'o alquimista',
    'eletrodomestico': 'microondas',
}
vendas_tecnologia = {
    'Iphone': 15000,
    'Samsung Galaxy': 12000,
    'TV Samsung': 10000,
    'PS5': 14300,  
}
qtde_iphone = vendas_tecnologia['Iphone']
print(qtde_iphone)
print(mais_vendidos['livros'])
#respondendo com o metodo get
print(vendas_tecnologia.get('TV Samsung'))
if vendas_tecnologia.get('TVS') == None:
    print('TVS não está na lista!')
else:
    print(vendas_tecnologia.get('TVS'))
print('')
#####################################################################################
lucro_1tri = {'janeiro': 10000, 'fevereiro': 120000, 'janeiro': 90000}
lucro_2tri = {'abril': 88000, 'maior': 89000, 'junho': 120000}

lucro_1tri['abril'] = 88000
print(lucro_1tri)
#Adicionando varios itens
lucro_1tri.update(lucro_2tri)
#Adicionando um item já existente
lucro_1tri['janeiro'] = 75000
print(lucro_1tri)
#removendo o mes de junho
del lucro_1tri['junho']
print(lucro_1tri)
print('')
################################################################################
total_ps5 = 0
for chave in vendas_tecnologia:
    #if 'PS5' in chave:
     #   total_ps5 += vendas_tecnologia[chave]
    print(f'{chave}: {vendas_tecnologia[chave]} unidades')
print('')
###############################################################################
# METODOS UTEIS items()
vendas_tecnologia = {'notebook asus': 2450, 'iphone': 1500, 'samsung galaxy': 12000, 'tv samsung': 10000}

#forma 1 -> Usando apenas o dicionario e as chaves
for chave in vendas_tecnologia:
    if vendas_tecnologia[chave] > 5000:
        print(f'{chave}: {vendas_tecnologia} unidades')
print('-'*25)
#Forma 2 -> usando o dicionario.items()
for produto, qtde in vendas_tecnologia.items():
    if qtde > 5000:
        print(f'{chave}: {vendas_tecnologia} unidades')
print('')
print('-='*30)
################################################################################
#Keys() e values()
chaves = vendas_tecnologia.keys()
valores = vendas_tecnologia.values()
print(chaves)
print(valores)
print(list(chaves))
print(list(valores))

for chave in vendas_tecnologia:
    print(f'{chave} {vendas_tecnologia[chave]}')
print('*'*40)
#organizando esse dicionario em ordem
lista_chaves = list(chaves)
lista_chaves.sort()

for chave in lista_chaves:
    print(f'{chave}: {vendas_tecnologia[chave]} unidades')
print('')
###############################################################################
produtos = ['iphone', 'samsung galaxy', 'tv samsung','ps5', 'tablet','ipad','tv philco','notebook hp','notebook dell']
vendas = [1500,1200,10000,1430,1720,1000,17000,2450,3250]

lista_tuplas = zip(produtos, vendas) # junta a lista
dicionario_vendas = dict(lista_tuplas)
print(dicionario_vendas)