from bs4 import BeautifulSoup
import requests

class Cotacao:
    def __init__(self):
        self.cotacao_agora = ""

    def Dolar_Euro(self, tipo):
        url = requests.get(f'https://www.remessaonline.com.br/cotacao/cotacao-{tipo.lower()}')
        conteudo = BeautifulSoup(url.content, 'html.parser')
        valor = conteudo.find('div', attrs={'class': 'style__Text-sc-1a6mtr6-2 ljisZu'})

        if valor:
            if tipo.upper() == 'DOLAR':
                simbolo = '💵'
            elif tipo.upper() == 'EURO':
                simbolo = '💶'

            self.cotacao_agora = f'{tipo.capitalize()}: 1{simbolo} = {valor.text}'
            print(self.cotacao_agora)
        else:
            print(f"Não foi possível obter a cotação para {tipo.capitalize()}.")

    def Bit_Coin(self):
        url = requests.get('https://www.infomoney.com.br/cotacoes/cripto/ativo/bitcoin-btc/')
        conteudo = BeautifulSoup(url.content, 'html.parser')
        box = conteudo.find('div', attrs={'class': 'line-info'})
        valores = box.find_all('p') if box else []

        if valores:
            print(f'BitCoin: 1🪙  = {valores[0].text} Reais')
        else:
            print("Não foi possível obter a cotação do Bitcoin.")


if __name__ == "__main__":
    cotacao = Cotacao()
    cotacao.Dolar_Euro('euro')
    cotacao.Dolar_Euro('dolar')
    cotacao.Bit_Coin()

