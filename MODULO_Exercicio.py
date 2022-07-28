from collections import Counter
import matplotlib.pyplot as plt


print('')
print('Exercicio 01')
vendas_tecnologia = {'notebook asus': 2450, 'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000,
                     'ps5': 14300, 'tablet': 1720, 'notebook dell': 17000, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000}

aux = Counter(vendas_tecnologia)
print(aux.most_common(3))
#############################################################################################################

print('')
print('Exercicio 02')
vendas_meses = [1500, 1727, 1350, 999, 1050,
                1027, 1022, 1500, 2000, 2362, 2100, 2762]
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun',
         'jul', 'ago', 'set', 'out', 'nov', 'dez']
plt.plot(meses, vendas_meses)
plt.ylabel('Vendas')
plt.xlabel('Meses')
plt.show()
