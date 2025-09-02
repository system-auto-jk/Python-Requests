import requests
from bs4 import BeautifulSoup
from time import sleep

# Lista de editorias que serão monitoradas no blog do Gran Cursos Online
lista_editoriais = (
    'policia', 'concurso-fiscal', 'tribunais', 'concurso-juridico',
    'concurso-professor', 'concurso-militar', 'area-saude', 'area-ti', 'diplomata'
)

# Lista para armazenar títulos já coletados, evitando repetições
lista_infor_tudo = []

# Primeira coleta inicial de informações
for edital in lista_editoriais:
    print(f'\nINFORMAÇÕES SOBRE - {edital}\n')

    URL_GRAN = requests.get(f'https://blog.grancursosonline.com.br/editorias/{edital}/')
    conteudo = BeautifulSoup(URL_GRAN.content, 'html.parser')

    # Coleta todos os blocos de postagens
    box_titulos = conteudo.find_all("div", attrs={'class': 'row list-post'})
    for i in box_titulos:
        # Extrai o título da notícia
        titulo = i.find("img")["alt"].strip()
        print(titulo)
        lista_infor_tudo.append(titulo)

        # Extrai o link da notícia
        link = i.find("a")["href"]
        print(link)
    
    # Pausa de 7 segundos entre editorias para não sobrecarregar o site
    sleep(7)

# Loop infinito para monitorar novas notícias
while True:
    for edital in lista_editoriais:
        print(f'\nINFORMAÇÕES SOBRE - {edital}\n')

        URL_GRAN = requests.get(f'https://blog.grancursosonline.com.br/editorias/{edital}/')
        conteudo = BeautifulSoup(URL_GRAN.content, 'html.parser')

        box_titulos = conteudo.find_all("div", attrs={'class': 'row list-post'})
        for i in box_titulos:
            titulo = i.find("img")["alt"].strip()
            link = i.find("a")["href"]

            # Só exibe se for uma notícia nova
            if titulo not in lista_infor_tudo:
                print(f'Nova informação sobre - {edital.capitalize()}')
                print(titulo)
                print(link)
                lista_infor_tudo.append(titulo)

        # Pausa de 10 segundos entre verificações
        sleep(10)

# Mantém a janela aberta até o usuário pressionar Enter (opcional, se rodar no Windows)
# input("\nPressione Enter para finalizar o programa...")
