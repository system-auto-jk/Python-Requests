import requests
from bs4 import BeautifulSoup
from time import sleep

carreira = ('policia','concurso-fiscal','tribunais','concurso-juridico','concurso-professor','concurso-militar','area-saude','area-ti','diplomata')


def Infor_GRAN_TRIBUNAIS(carreira):

    URL_GRAN_TRIBUNAIS = requests.get(f'https://blog.grancursosonline.com.br/editorias/{carreira}/')

    conteudo_GRAN_Tribunais = BeautifulSoup(URL_GRAN_TRIBUNAIS.content, 'html.parser')

    box_titulos_GRAN_Tribunais = conteudo_GRAN_Tribunais.find_all("div", attrs={'class':'row list-post'})

    for titulo in box_titulos_GRAN_Tribunais:
        print(f'{titulo.find("img")["alt"].strip()}\n{titulo.find("a")["href"]}\n-')
        sleep(1)

#Infor_GRAN_TRIBUNAIS(carreira[0])
#ou
Infor_GRAN_TRIBUNAIS('policia')