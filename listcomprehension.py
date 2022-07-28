precos_produtos = [100, 150, 300, 5500]
produtos = ['vinho', 'cafeiteira', 'microondas', 'iphone']

impostos = [preco * 0.3 for preco in precos_produtos]
print(impostos)
###############################################################################
vendas_produtos = [1500, 150, 2100, 1950]
produtos = ['vinho', 'cafeiteira', 'microondas', 'iphone']

lista_auxi = list(zip(vendas_produtos, produtos))
lista_auxi.sort(reverse=True)
produtos = [produto for vendas, produto in lista_auxi]
print(produtos)
###############################################################################

meta = 1000
vendas_produtos = [1500, 150, 2100, 1950]
produtos = ['vinho', 'cafeiteira', 'microondas', 'iphone']

produtos_acima_meta = []
for i, produto in enumerate(produtos):
    if vendas_produtos[i] > meta:
        produtos_acima_meta.append(produto)
print(produtos_acima_meta)

produtos_acima_meta = [produto for i, produto in enumerate(
    produtos) if vendas_produtos[i] > meta]
print(produtos_acima_meta)
###############################################################################

vendedores_dic = {'Maria': 1200, 'José': 300, 'Antonio': 800,
                  'João': 1500, 'Francisco': 1900, 'Ana': 2750, 'Luiz': 440}
meta = 1000
bonus = []

for item in vendedores_dic:
    if vendedores_dic[item] > meta:
        bonus.append(vendedores_dic[item] * 0.1)
    else:
        bonus.append(0)
print(bonus)

bonus = [vendedores_dic[item] * 0.1 if vendedores_dic[item]
         > meta else 0 for item in vendedores_dic]
