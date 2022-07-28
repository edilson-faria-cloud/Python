print('')
print('Exercicio 01')
print('')
cpf = input('Insira seu CPF: ' )

#tratar o cpf
#tirar espaços no inicio e no final
cpf = cpf.strip()
#tirar os . (pontos)
cpf = cpf.replace('.', '')
#tirar ostraços (-)
cpf = cpf.replace('-', '')
if len(cpf) == 11 and cpf.isnumeric():
    print(cpf)
else:
    print('Digite seu CPF corretamente e digite apenas números')
    
print('')
print('-='*25)

################################################################
print('')
print('Exercicio 02')
print('')
nome = input('Digite seu nome: ')
email = input('Digite seu e-mail: ')

if nome and email:
    pos_a = email.find('@')
    servidor = email[pos_a:]
    if pos_a != -1 and '.' in servidor:
        print('Cadastro Concluido')
    else:
        print('Email Invalido')
else:
    print('Digite seu nome e e-mail corretamente')
    
print('')
print('-='*25)
