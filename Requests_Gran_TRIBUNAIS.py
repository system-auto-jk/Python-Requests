import requests
from bs4 import BeautifulSoup
from time import sleep

def Infor_GRAN_TRIBUNAIS():

    URL_GRAN_TRIBUNAIS = requests.get('https://blog.grancursosonline.com.br/editorias/tribunais/')

    conteudo_GRAN_Tribunais = BeautifulSoup(URL_GRAN_TRIBUNAIS.content, 'html.parser')

    box_titulos_GRAN_Tribunais = conteudo_GRAN_Tribunais.find_all("div", attrs={'class':'row list-post'})

    for titulo in box_titulos_GRAN_Tribunais:
        print('CONCURSOS - TRI / JUR (GRAN)',f'{titulo.find("img")["alt"].strip()}\n{titulo.find("a")["href"]}\n-')
        sleep(1)

Infor_GRAN_TRIBUNAIS()