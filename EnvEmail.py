import win32com.client as win32


def enviar_email(self):
    self.enviar_email = False
    outlook = win32.Dispatch('outlook.application')

    if self.enviar_email:
        # enviar email
        mail = outlook.CreateItem(0)
        mail.To = 'semchefe41@gmail.com'
        mail.Subject = f'Lista de produtos com {self.desconto_min:.0%} de Desconto'
        mail.Body = 'Texto do Email'

        # filtrar produtos

        tabela_filtrada = self.produtos.loc[self.produtos['Preço Atual']
                                            <= self.produtos['Preço Original']*(1-self.desconto_min), :]

        # Texto do Email
        mail.HTMLBody = f'<p>Esses são os produtos com mais de {self.desconto_min:.0%} desconto</p> {tabela_filtrada.to_html}'
        mail.Send()
