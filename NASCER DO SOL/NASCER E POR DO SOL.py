from bs4 import BeautifulSoup
import requests

# URL da página do Climatempo para a cidade de Lauro de Freitas - BA
URL = 'https://www.climatempo.com.br/previsao-do-tempo/cidade/3392/laurodefreitas-ba'

# Faz a requisição HTTP para obter o conteúdo da página
site = requests.get(URL)

# Verifica se a requisição foi bem-sucedida (status code 200 = OK)
if site.status_code == 200:
    # Cria o objeto BeautifulSoup para analisar o HTML da página
    conteudo = BeautifulSoup(site.content, 'html.parser')

    # Busca o parágrafo que contém a previsão principal
    texto = conteudo.find('p', attrs={'class': '-gray -line-height-24 _center'})

    # Se encontrou o texto, formata e exibe
    if texto:
        texto_formatado = ' '.join(texto.text.split())  # Remove espaços extras
        print(texto_formatado)
    else:
        print("Texto da previsão principal não encontrado.")

    # Busca a lista de variáveis climáticas (ex: Sol, chuva, vento, etc.)
    sol = conteudo.find('ul', attrs={'class': 'variables-list'})

    # Percorre cada item da lista de variáveis
    for i in sol:
        if 'Sol' in i.text:
            # Quebra o texto em partes
            partes = i.text.split()
            if len(partes) >= 3:
                nascer_sol = partes[1]  # horário de nascer do sol
                por_sol = partes[2]     # horário de pôr do sol
                print(f"Nascer do sol: {nascer_sol}")
                print(f"Pôr do sol: {por_sol}")
            else:
                # Caso o formato não seja o esperado
                sol_formatado = ' '.join(i.text.split())
                print(sol_formatado)
else:
    print(f"Falha ao acessar o site. Status code: {site.status_code}")

# Mantém a janela aberta até o usuário pressionar Enter
input("\nPressione Enter para finalizar o programa...")
