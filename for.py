produtos = ['coca', 'pepsi','guarana', 'sprite', 'fanta']
producao = [15000,12000,13000,5000,250]
texto = 'lira@gmail.com'

for produto in produtos:
    print(f'O produto é {produto}')

################################################################################################
vendas = [1200,300,800,1500,2750,400,20,23,70,90,80,110,999,900,80,870,50,1111,120,800]
meta = 1000
qtd_bateu_meta = 0

for venda in vendas:
    if venda >= meta:
        qtd_bateu_meta += 1

qtd_funcionarios = len(vendas)

print(f'O percentual de pessoas que bateram a meta foi de {qtd_bateu_meta/qtd_funcionarios:.0%}')
print('')

###################################################################################################

estoque = [1200,300,800,1500,1900,2750,400,20,23,70,90]
produtos = ['coca','pepsi','guarana','skol','brahma','agua','del valle','dolly','redbull','cachaça','vinho tinto']
nivel_minimo = 50

for i, qtd in enumerate(estoque):
    if qtd < nivel_minimo:
        print(f'{produtos[i]} está abaixo do nivel minimo. Tempos apenas {qtd} unidades')    
        
##################################################################################################

estoque = [
    [294,125,269,208,2],
    [300,992,501,223,16],
    [429,397,198,60,80],
]

fabricas = ['Lira Manufacturing', 'Fabrica Hashtag','Produções e Cia']
nivel_minimo = 50

for i, lista in enumerate(estoque):
    for qtd in lista:
        if qtd < nivel_minimo:
            print(fabricas[i])

vendas = [100,150,2000,120]
meta = 110
for venda in vendas:
    if venda < meta:
        print('A loja nao ganha bonus')
        continue
    print(venda)