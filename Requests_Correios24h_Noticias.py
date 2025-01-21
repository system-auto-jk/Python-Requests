from time import sleep
from bs4 import BeautifulSoup
import requests


lista_noticias = list()

def Noticias():
    URL = requests.get('https://www.correio24horas.com.br/ultimas')

    conteudo = BeautifulSoup(URL.content, 'html.parser')

    todos_h1 = conteudo.find('div', attrs={'id':'resultList'})

    for h1 in todos_h1.find_all("a"):
        print(f'{h1.find("h1").text}\n{h1["href"]}\n')
        sleep(1)

Noticias()



            

