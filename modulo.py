import webbrowser as wb
import time
import keyboard

wb.open_new_tab('https://www.jornaldacidadeonline.com.br/')
segundos_hoje = time.time()
print(segundos_hoje)
data_hoje = time.ctime()
print(data_hoje)
tempo_inicial = time.time()
for i in range(100000000):
    pass
tempo_final = time.time()
duracao = tempo_final - tempo_inicial
print(f'O programa levou {duracao} segundos para rodar')

data_atual = time.gmtime()
print(data_atual)
