from selenium import webdriver
import win32com.client as win32
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import pytz
from EnvEmail import enviar_email


class Automacao():

    @staticmethod
    def transformar_texto(texto):
        return int(texto.replace('R$', '').replace('.', '').replace(',', '.'))

    @staticmethod
    def _data_hora():

        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def iniciando(self):

        self.captura_produtos_especificos()
        self.salvar_dados_planilha()
        self.enviar_email()

    def configuracao(self):

        self.servico = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome()
        self.driver.set_window_position(-10000, 0)
        self.produtos = pd.read_excel(r'Produtos_2022.xlsx')
        self.produtos = self.produtos.fillna('-')

    def captura_produtos_especificos(self):
        desconto_min = 0.2

        for i, linha in self.produtos.iterrows():
            # AMAZON
            self.driver.get(linha['Amazon'])
            try:
                preco_amazon = self.driver.find_element(
                    By.CLASS_NAME, 'a-price-whole').text
                preco_amazon = self.transformar_texto(preco_amazon)
            except:
                print('Produto {} não disponivel na Amazon'.format(
                    linha['Link Produto']))
                preco_amazon = linha['Preço Original'] * 3

            # NETSHOES
            self.driver.get(linha['Netshoes'])
            preco_netshoes = self.driver.find_element(
                By.XPATH, '//*[@id="buy-box"]/div[2]/div[2]/div').text
            preco_netshoes = self.transformar_texto(preco_netshoes)

            # CENTAURO
            self.driver.get(linha['Centauro'])
            preco_centauro = self.driver.find_element(
                By.XPATH, '//*[@id="addToCart_pdp"]/div[1]/div/div[2]').text
            preco_centauro = self.transformar_texto(preco_centauro)

            preco_original = linha['Preço Original']

            lista_precos = [(preco_amazon, 'Amazon'), (preco_netshoes, 'Netshoes'),
                            (preco_centauro, 'Centauro'), (preco_original, 'Preço Original')]
            lista_precos.sort()
            self.produtos.loc[i, 'Preço Atual'] = lista_precos[0][0]
            self.produtos.loc[i, 'Local'] = lista_precos[0][1]

            if lista_precos[0][0] <= preco_original*(1-desconto_min):
                self.enviar_email = True
        return print()

    def salvar_dados_planilha(self):
        # salvar arquivo
        self.produtos.to_excel('Produtos.xlsx')


if __name__ == '__main__':
    objeto = Automacao()
    objeto.configuracao()
    objeto.iniciando()
    objeto.salvar_dados_planilha()
