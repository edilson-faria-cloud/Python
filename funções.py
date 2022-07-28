# FUNÇÃO
from msilib.schema import ServiceControl


def cadastrar_produto():
    produto = input('Digite o nome do produto que deseja cadastrar: ')
    produto = produto.casefold()
    produto = produto.strip()
    return produto


produto = cadastrar_produto()
print(produto)
###############################################################################


def minha_soma(num1, num2, num3):
    return num1+num2+num3


soma = minha_soma(10, 20, 30)
print(soma)
print('')
###############################################################################


def eh_da_categoria(bebida, cod_categoria):
    bebida = bebida.upper()
    if cod_categoria in bebida:
        return True
    else:
        return False


produtos = ['beb46275', 'TFA23962', 'TFA64715', 'TFA69555', 'TFA56743', 'BSA45510', 'TFA44968', 'CAR75448', 'CAR23596', 'CAR13490', 'BEB21365', 'BEB31623', 'BSA62419', 'BEB73344', 'TFA20079', 'BEB80694', 'BSA11769', 'BEB19495', 'TFA14792',
            'TFA78043', 'BSA33484', 'BEB97471', 'BEB62362', 'TFA27311', 'TFA17715', 'BEB85146', 'BEB48898', 'BEB79496', 'CAR38417', 'TFA19947', 'TFA58799', 'CAR94811', 'BSA59251', 'BEB15385', 'BEB24213', 'BEB56262', 'BSA96915', 'CAR53454', 'BEB75073']
# percorrer toda a minha lista de produtos
# pra cada produto, verificar se ele e bebida alcoolica
# se for bebida alcoolica, exibir a mensagem enviar

for produto in produtos:
    if eh_da_categoria(cod_categoria='BEB', bebida=produto):
        print(f'Enviar {produto} para setor de bebidas alccolicas')
    elif eh_da_categoria(produto, 'BSA'):
        print(f'Enviar {produto} para setor de bebidas alccolicas')

###############################################################################
produtos = ['apple tv', 'mac', 'iphonex', 'ipad', 'airpods']
produtos.sort()
print(produtos)
produtos.sort(reverse=True)


def padronizar_codigos(lista_codigos, padrao='m'):
    for i, item in enumerate(lista_codigos):
        item = item.replace('  ', ' ')
        item = item.strip()
        if padrao == 'm':
            item = item.casefold()
        elif padrao == 'M':
            item = item.upper()
        lista_codigos[i] = item
    return lista_codigos


cod_produtos = ['  ABC12  ', 'abc123', 'AbC35']
print(padronizar_codigos(cod_produtos, 'm'))

###############################################################################
# Docstring e Annotations
# Docstring -> Diz o que a função faz, quais valores ela tem como argumento
# Annotation -> diz o que devem ser os argumentos


def minha_soma(num1, num2, num3):
    ''' Faz a soma de 3 numeros inteiros e devolve como resposta um inteiro
    Parametrs:
        num1 (int): Primeiro numero a ser somado
        num2 (int): Segundo numero a ser somado
        num3 (int): Terceiro numero a ser somado
    Returns:
        soma (int): O valor da soma dos 3 numeros dados com argumento    

    '''
    return num1 + num2 + num3


print(minha_soma(5, 6, 9))
print('')
###############################################################################
# Tratamento Try e Except


def descobrir_servidor(email):
    try:
        posicao_a = email.index('@')
        servidor = email[posicao_a]
        if 'gmail' in servidor:
            return 'gmail'
        elif 'hotmail' in servidor or 'outlook' in servidor or 'live' in servidor:
            return 'hotmail'
        elif 'yahoo' in servidor:
            return 'yahoo'
        elif 'uol' in servidor or 'bol' in servidor:
            return 'uol'
        else:
            return 'Não determinado'
    except:
        raise Exception('Email digitado nao tem @, digite novamente')


email = input('Qual o seu e-mail? ')
print(descobrir_servidor(email))
###############################################################################
print('')
# Args e Kwargs


def minha_soma(*numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma


print(minha_soma(10, 13, 1, 6, 6, 98))


def preco_final(preco, **adicionais):
    print(adicionais)
    if 'desconto' in adicionais:
        preco *= (1-adicionais['desconto'])
    if 'garantia_extra' in adicionais:
        preco += adicionais['garantia_extra']
    if 'imposto' in adicionais:
        preco *= (1+adicionais['imposto'])
    return preco
