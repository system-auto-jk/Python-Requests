from time import sleep
from bs4 import BeautifulSoup
import requests


def ConcursoPrefeituras():
    req = requests.get('https://concursosnobrasil.com/concursos/novos/')
    sleep(2)
    if req.status_code ==200:
        site = BeautifulSoup(req.content, 'html.parser')
        box = site.find_all('tr')
        for concurso in box:
            try:
                primeiro = concurso.find_all("td")
                print(f'{concurso.find("td").text.strip()}\n{concurso.find("a")["href"]}\nEstado: {primeiro[1].text.strip()}\nVagas: {primeiro[2].text}')
                print()
            except:
                print('')

ConcursoPrefeituras()



