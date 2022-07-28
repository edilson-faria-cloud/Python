print('')
print('Exercicio 01')
print('')
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set','out','nov','dez']
vendas_1sem = [25000, 29000, 22200, 17750,15870,19990]
vendas_2sem = [19850,20120,17450,15555,495012,9650]

vendas_1sem.extend(vendas_2sem)
maior_valor = max(vendas_1sem)
menor_valor = min(vendas_1sem)
print(maior_valor)
print(menor_valor)

i_maior_valor = vendas_1sem.index(maior_valor)
i_menor_valor = vendas_1sem.index(menor_valor)

print(f'O melhor mês do ano foi {meses[i_maior_valor]} com {maior_valor} vendas')

fat_total = sum(vendas_1sem)
print(f'Faturamento total: R${fat_total:,}')

percentual = maior_valor / fat_total
print(f'O melhor mês representou {percentual:.1%} das vendas do ano todo')

top3 = []
maior_valor = max(vendas_1sem)
top3.append(maior_valor)
vendas_1sem.remove(maior_valor)
print(vendas_1sem)
maior_valor = max(vendas_1sem)
top3.append(maior_valor)
vendas_1sem.remove(maior_valor)
print(vendas_1sem)
print(top3)
print('-='*25)
print('')
###############################################################
print('Exercicio 02')
print('Mudança Carga Tributária')
print('')
produtos = ['computador', 'livro', 'tablet', 'celular', 'tv', 'ar condicionado', 'alexa', 'máquina de café', 'kindle']
produtos_ecommerce = [
    [10000, 2500],
    [50000, 40],
    [7000, 1200],
    [20000, 1500],
    [5800, 1300],
    [7200, 2500],
    [200, 800],
    [3300, 700],
    [1900, 400],
]


if 'livro' in produtos:
    i_livro = produtos.index('livro')
    total_antigo = produtos_ecommerce[i_livro][0] * produtos_ecommerce[i_livro][1]
    produtos_ecommerce[i_livro][1] *= 1.1
    novo_total = produtos_ecommerce[i_livro][0] * produtos_ecommerce[i_livro][1]
    print(f'Vamos pagar de imposto a mais: R${novo_total - total_antigo:,}') 