print('Exercicio 01')
print('')

quarto = [
    ['João', 'cpf:00000000000'],
    ['João', 'cpf:11111111111'],
    ['João', 'cpf:22222222222'],
    ['João', 'cpf:33333333333'],
]

qtd_pessoas = int(input('Quantas pessoas terão no quarto? '))
quarto = []

for i in range(qtd_pessoas):
    nome = input('Qual o nome? ')
    cpf = input('Qual cpf? ')
    hospede = [nome,f'cpf: {cpf}']
    quarto.append(hospede)

print(quarto)
print('')    
##########################################################
print('Exercicio 02')
meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

for venda in vendas:
    if venda[1] >= meta:
        print(f'Vendedor {venda[0]} bateu a meta. Fez {venda[1]} vendas')

print('')
##############################################################################
print('Exercicio 03')
produtos = ['iphone','galaxy','ipada','tv','maquina de café','kindle','geladeira']
vendas2020 = [558147,71456,98765,892292,15478,587413,456987]
vendas2021 = [951642,2448295,787604,867660,646016,694913,539704]

for i, produto in enumerate(produtos):
    if vendas2020[i] > vendas2021[i]:
        crescimento = vendas2020[i] / vendas2021[i] - 1
        print(f'{produto} vendeu R${vendas2020[i]:,} no ano de 2020 e vendeu R${vendas2021[i]:,} no ano de 2021 e teve {crescimento:.1%} de crescimento')
###############################################################################
print('')
print('Exercicio 04')


estoque = [
    [294,125,269,208,2,33],
    [300,992,501,223,16,89],
    [429,397,198,60,80,75],
]

fabricas = ['Lira Manufacturing', 'Fabrica Hashtag','Produções e Cia']
nivel_minimo = 50
fabricas_abaixo_nivel=[]

for i, lista in enumerate(estoque):
    for qtd in lista:
        if qtd < nivel_minimo:
            if fabricas[i] in fabricas_abaixo_nivel:
                pass
            else:
                fabricas_abaixo_nivel.append(fabricas[i])
print('')
###############################################################################
print('Exercicio 05')
print('')
meta = 10000
melhor_vendedor = ''
maior_vendas = 0
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Ana', 10330],
    ['Alon', 7870],
]

acima_meta = []
for venda in vendas:
    
    if venda[1] >= meta and venda[1] > maior_vendas:
        acima_meta.append(venda)
        maior_vendas = venda[1]
        melhor_vendedor = venda[0]
        
calculo = len(acima_meta) / len(vendas)

print(acima_meta)
print(f'{calculo:.1%} dos vendedores bateram a meta')
print(f'O melhor vendedor foi {melhor_vendedor} com {maior_vendas} vendas')
    