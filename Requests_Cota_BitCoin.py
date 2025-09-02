from bs4 import BeautifulSoup
import requests

class Cotacao:
    def __init__(self):
        self.cotacao_agora = ""

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
    cotacao.Bit_Coin()

