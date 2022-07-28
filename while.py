produto = input('Registre um produto. Para cancelar o registro de um novo produto: ')
vendas = []

while produto != '':
    vendas.append(produto)
    produto = input('Registre um produto. Para cancelar o registro de um novo produto: ')

print(f'Registro Finalizado Os produtos cadastrado foram {vendas}')
print('')
############################################################################################
vendas = []
while True:
   
    produto = input('Qual o produto? ')
    if not produto:
        break
    qtde = int(input('Qual quantidade? '))
    vendas.append([produto,qtde])

print(vendas)