print('Exercicio 01')
print('')
meta = 10000
vendas = [
    ('João', 15000),
    ('Julia', 27000),
    ('Marcus', 9900),
    ('Maria', 3750),
    ('Ana', 7870),
]

for vendedor, qtde in vendas:
    if qtde >= meta:
        print(f'{vendedor} bateu a meta, vendeu {qtde} unidades')

print('-='*25)
print('')
#######################################################################
print('Exercicio 02')
print('')
vendas_produtos = [
    ('Iphone', 558147,951642),
    ('Galaxy', 712305,244295),
    ('Ipad', 573823,26964),
    ('TV', 60523,405252),
]
for produto, vendas2019, vendas2020 in vendas_produtos:
    if vendas2020 > vendas2019:
        crescimento = vendas2020 / vendas2019 - 1
        print(f'{produto} teve {vendas2019} vendas em 2019, {vendas2020} vendas em 2020. Crescimento de {crescimento:.1%}')