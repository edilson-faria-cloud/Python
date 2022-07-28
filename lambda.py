import enum


def padronizar_texto(texto):
    texto = texto.casefold()
    texto = texto.replace("  ", " ")
    texto = texto.strip()
    return texto


produtos = [' ABC12 ', 'abc34', 'AbC37', 'beb12', ' BSA151']
for i, produto in enumerate(produtos):
    produtos[i] = padronizar_texto(produto)
print(produtos)

produtos = list(map(padronizar_texto, produtos))
print(produtos)


vendas_produtos = {'vinho': 100, 'cafeiteira': 150,
                   'microondas': 300, 'iphone': 5500}

################################################################################


def segundo_item(tupla):
    return tupla[1]


lista_vendas = list(vendas_produtos.items())
lista_vendas.sort(key=segundo_item, reverse=True)
print(lista_vendas)
################################################################################
# Lambda Expressions são funções anonimas que tem 1 linha e sao atribuidas a uma variavel, como se a variavel virasse uma função
preco_tecnologia = {'notebook asus': 2450, 'iphone': 4500, 'samsung galaxy': 3000, 'tv samsung': 1000,
                    'ps5': 3000, 'tablet': 1000, 'notebook dell': 3000, 'ipad': 3000, 'tv philco': 800, 'notebook hp': 1700}


def calcular_preco(preco):
    return preco * 1.3


preco_com_imposto = list(map(calcular_preco, preco_tecnologia.values()))
print(preco_com_imposto)

# fazendo com lambda
preco_imposto_2 = list(
    map(lambda preco: preco * 1.3, preco_tecnologia.values()))
print(preco_imposto_2)
###############################################################################


def calcular_imposto(imposto):
    return lambda preco: preco * imposto


calcular_preco_produto = calcular_imposto(0, 1)
