from bs4 import BeautifulSoup
import requests

quantidade_noticias = 5
lista_noticias = list()
contador = 0
URL = requests.get('https://noticias.stf.jus.br/')

conteudo = BeautifulSoup(URL.content, 'html.parser')

todos_h1 = conteudo.find_all('div', attrs={'class':'card-lt-md card-xs noticia m-0 m-b-24'})

print(len(todos_h1))
for h1 in todos_h1:
    print(h1.find("a").text.strip())
    print(h1.find("a")['href'])
    print()
    