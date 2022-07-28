vendas_funcionario1 = 1000
vendas_funcionario2 = 770
vendas_funcionario3 = 2700
print('')
print('Exercicio 01')
print('')
if vendas_funcionario1 >= 1000:

    if vendas_funcionario1 >= 2000:
        bonus = 0.15 * vendas_funcionario1
    else:
        bonus = 0.1 * vendas_funcionario1
else:
    bonus = 0
    print(f'O funcionario 1 ganhou {bonus} de bonus')


if vendas_funcionario2 >= 2000:
    bonus = vendas_funcionario2 * 0.15
elif vendas_funcionario2 >= 1000:
    bonus = 0.1 * vendas_funcionario2
else:
    bonus = 0
print(f'O funcionario 2 ganhou {bonus} bônus.')


if vendas_funcionario3 >= 1000:
    bonus = vendas_funcionario3 * 0.1
else:
    bonus = 0
print(f'O funcionario 3 ganhou {bonus} bônus.')

print('-='*25)

################################################################
print('')
print('Exercicio 02')

produto = input('Qual o produto? ')
categoria = input('Qual a categoria do produto? ')
qtd = int(input('Qual a quantidade atual do produto? '))

if produto and categoria and qtd:
    qtd = int(qtd)
    if categoria == 'bebidas':
        if qtd < 75:
            print(
                f'Solicitar {produto} à equipe de compras, temos apenas {qtd} unidades em estoque')
        elif categoria == 'limpeza':
            if qtd < 30:
                print(
                    f'Solicitar {produto} à equipe de compras, temos apenas {qtd} unidades em estoque')
        else:
            if qtd < 50:
                print(
                    f'Solicitar {produto} à equipe de compras, temos apenas {qtd} unidades em estoque')

else:
    print('Preencha todas as informações')
