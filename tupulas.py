vendas = ('Lira','25/08/2020','15/02/1994',200,'Estagiário')
nome, data_contratacao, data_nascimento, salario, cargo = vendas
print(nome)
##################################################################
vendas = [
    ('20/08/2020', 'iphone x', 'azul', '128gb', 350, 4000),
    ('20/08/2020', 'iphone x', 'prata', '128gb', 1500, 4000),
    ('20/08/2020', 'ipad', 'prata', '256gb', 127, 6000),
    ('20/08/2020', 'ipad', 'azul', '128gb', 981, 5000),
    ('21/08/2020', 'iphone x', 'azul', '128gb', 397, 4000),
    ('21/08/2020', 'iphone x', 'prata', '128gb', 1017, 4000),
    ('21/08/2020', 'ipad', 'prata', '256gb', 50, 6000),
    ('21/08/2020', 'iphone x', 'azul', '128gb', 4000, 5000),      
]
faturamento = 0
produto_mais_vendido = ''
qtde_produto_mais_vendido = 0

for item in vendas:
    data,produto,cor,capacidade,unidades,valor_unitario = item
    if produto == 'iphone x' and data == '20/08/2020':
        faturamento += unidades * valor_unitario
    if data == '21/08/2020':
        if unidades > qtde_produto_mais_vendido:
            produto_mais_vendido = produto
            qtde_produto_mais_vendido = unidades
print(f'My product most sold was {produto_mais_vendido} with {qtde_produto_mais_vendido} unit')
print(f'R$ {faturamento:,}')