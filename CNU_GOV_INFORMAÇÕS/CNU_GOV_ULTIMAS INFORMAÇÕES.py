# Programa que pega as últimas 3 notícias sobre o CNU no site do GOV
import requests
from bs4 import BeautifulSoup
from time import sleep

def InforCNU():
    print('- BUSCANDO INFORMAÇÕES SOBRE O CNU -\n')

    listainfocnu = []  # Lista para armazenar as notícias coletadas

    # Requisição para acessar a página de notícias sobre o CNU
    req = requests.get('https://www.gov.br/gestao/pt-br/concursonacional/noticias')
    sleep(2)  # Pausa para simular processamento / evitar sobrecarga no site

    # Faz o parsing do HTML com BeautifulSoup
    site = BeautifulSoup(req.content, 'html.parser')

    # Busca todos os elementos <a> com a classe que contém os títulos das notícias
    titulos = site.find_all('a', attrs={'class': 'summary url'})

    cont = 0
    for i in titulos:
        # Exibe título e link da notícia
        print(f'Título: {i.text}\nLink: {i["href"]}\n')

        # Adiciona título e link à lista
        listainfocnu.append(f'Título: {i.text}\nLink: {i["href"]}\n')

        cont += 1
        if cont == 3:  # Limita a 3 notícias
            break

# Executa a função principal
InforCNU()

# Mantém a janela aberta até o usuário pressionar Enter
input("\nPressione Enter para finalizar o programa...")
