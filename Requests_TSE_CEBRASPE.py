from bs4 import BeautifulSoup
import requests
from time import sleep


URL_TSE = requests.get('https://www.tse.jus.br/comunicacao/noticias')
conteudo_TSE = BeautifulSoup(URL_TSE.content,'html.parser')
box_TSE = conteudo_TSE.find_all('h3', attrs={'class':'news-list-title'})

for titulo in box_TSE:
    print(titulo.text.strip())
    print(titulo.find("a")["href"]+'\n')
    sleep(1)
