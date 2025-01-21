from bs4 import BeautifulSoup
import requests
from time import sleep


lista_noticias_techmundo = list()
quantidade_noticias = 10
contador = 0

URL_TECH = requests.get('https://www.tecmundo.com.br/novidades')

conteudo_TECH = BeautifulSoup(URL_TECH.content, 'html.parser')

todos_h1_TECH = conteudo_TECH.find_all('h4')

for h1 in todos_h1_TECH:
    print(h1.text)
    print(h1.find("a")["href"])
    lista_noticias_techmundo.append(h1.text)
    sleep(0.3)



