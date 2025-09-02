from bs4 import BeautifulSoup
import requests
from time import sleep

# URL da página de notícias do TSE
URL_TSE = requests.get('https://www.tse.jus.br/comunicacao/noticias')

# Faz o parsing do HTML com BeautifulSoup
conteudo_TSE = BeautifulSoup(URL_TSE.content, 'html.parser')

# Seleciona todos os títulos de notícias (tag <h3> com classe específica)
box_TSE = conteudo_TSE.find_all('h3', attrs={'class': 'news-list-title'})

# Percorre cada título encontrado
for titulo in box_TSE:
    # Exibe o texto do título, removendo espaços extras
    print(titulo.text.strip())

    # Exibe o link da notícia
    print(titulo.find("a")["href"] + '\n')

    # Pausa de 1 segundo entre notícias para não sobrecarregar o site
    sleep(1)

# Mantém a janela aberta até o usuário pressionar Enter (opcional para Windows)
input("\nPressione Enter para finalizar o programa...")
