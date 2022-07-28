meta = 0.05
taxa = 0
rendimento = 0.10

if rendimento > meta:

    if rendimento > 0.20:
        taxa = 0.04
        print(f'A taxa foi de {taxa}')
    else:
        taxa = 0.02
        print(f'A taxa foi de {taxa}')

else:
    taxa = 0
    print(f'A taxa foi de {taxa}')

##########################################################

metas = 20000
vendas = 25000

if vendas < metas:
    print('Não ganhou bônus')

elif vendas > (metas * 2):
    bonus = 0.07 * vendas
    print(f'Ganhou {bonus} de bônus')
else:
    bonus = 0.03 * vendas
    print(f'Ganhou {bonus} de bônus')

#########################################################

faturamento_loja_1 = 2500
faturamento_loja_2 = 2200

print('Programa 1')

if faturamento_loja_1 == faturamento_loja_2:
    print('Os faturamentos sao iguais')
else:
    print('Os faturamentos são diferentes')

print('Programa 2')
email_usuario = input('Insira seu email: ')
if not '@' in email_usuario:
    print('Email invalido')

##########################################################

faturamento = input('Qual foi o faturamento da loja esse mês? ')
custo = input('Qual foi o custo da loja nesse mês? ')

if faturamento and custo:
    lucro = int(faturamento) - int(custo)
    print(f'O lucro da loja foi de {lucro} R$')

else:
    print('Preencha corretamente o campo')
