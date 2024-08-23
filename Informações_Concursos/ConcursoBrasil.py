import requests
from bs4 import BeautifulSoup
from time import sleep

def BuscadorEstado(buscador, estado):
    site = requests.get(f'https://concursosnobrasil.com/concursos/{estado}/')

    if site.status_code ==200:

        try:
            conteudo = BeautifulSoup(site.content, 'html.parser')
            print('\nDestaques - Concursos Públicos Abertos Bahia\n')
            table =conteudo.find('table')
            seção = table.find_all('a')
            cont = 0
            
            for i in seção:
                nome = str(i.text).upper()
                if buscador in nome:
                    print(nome)
                    print(i["href"])
                    print('')
                    cont +=1
                    sleep(0.2)
            print(f'Informações encontradas sobre {buscador.upper()}: {cont} em ({estado.upper()})')
            segresp = input('Fazer outra busca?: ')
            if segresp =='s':
                BuscadorEstado(buscador=input('Concurso: ').upper(),estado=input('Estado: '))
            else:
                pass
        except:
            print(' Erro ao buscar informações ')
    else:
        print('Erro ao  buscar estado')

def TodosEstado(estado):
    try:

        site = requests.get(f'https://concursosnobrasil.com/concursos/{estado}')
    except:
        print('Erro de conexão')

    if site.status_code ==200:
        try:
            conteudo = BeautifulSoup(site.content, 'html.parser')
            cont = 0
            print('\nConcursos Públicos Abertos Bahia\n')
            seção = conteudo.find('table')
            titulos = seção.find_all('a')
            
            for i in titulos:
                print(i.text)
                print(i["href"])
                print()
                cont +=1
                sleep(0.1)
            print(f'{cont} Concursos em ({estado.upper()})')
            segresp = input('Fazer outra busca?: ')
            if segresp =='s':
                TodosEstado(estado=input('Estado: '))
            else:
                pass
        except:
            print(' Erro ao buscar informações ')
    else:
        print('Erro de conexão ao buscar estado')
        TodosEstado(estado=input('Estado: '))
        
def BemVindo():

    print('BEM VINDO(A) - BUSQUE MAIS INFORMAÇÕES SOBRE CONCURSOS PUBLICOS')

    print('''
    [1] BUSCAR CONCURSO POR ESTADO
    [2] TODOS OS CONCURSOS POR ESTADO
    [3] ULTIMAS INFORMAÇÕES SOBRE CONCURSOS
    [4] DESTAQUES POR ESTADO
    [5] SAIR
        ''')

def ConcursoPrefeituras():
    req = requests.get('https://concursosnobrasil.com/')
    sleep(2)
    if req.status_code ==200:
        site = BeautifulSoup(req.content, 'html.parser')
        box = site.find('div',attrs={'class':'secao-2-first'})
        titulos = box.find_all('a')
        for i in titulos:
            print(f'Titulo: {i.text}\nLink: {i["href"]}\n')
            sleep(0.1)
        segresp = input('Fazer nova busca?: ')
        if segresp =='s':
            ConcursoPrefeituras()


def Destaques(estado):
    lista= list()
    site = requests.get(f'https://concursosnobrasil.com/concursos/{estado}/')

    conteudo = BeautifulSoup(site.content, 'html.parser')
    print('\nDestaques - Concursos Públicos Abertos Bahia\n')
    tabela = conteudo.find('table')
    seção = tabela.find_all('tr',attrs={'class':'destaque'})

    cont = 0
    for i in seção:
        link = i.find('a')["href"]
        print(f'{i.text}\n{link}\n')
        cont+=1
        lista.append(f'{i.text}\n{link}\n')
    print(f'({cont}) Concursos em Destaque')
    segresp = input('Fazer outra busca?: ')

    if segresp =='s':
        Destaques(estado=input('Estado: '))
    else:
        pass

while True:
    BemVindo()

    resposta = int(input('Escolha a Opção: '))

    if resposta == 1:
        BuscadorEstado(buscador=input('Concurso: ').upper(),estado=input('Estado: '))
        
    elif resposta == 2:
        TodosEstado(estado=input('Estado: '))
    
    elif resposta == 3:
        ConcursoPrefeituras()

    elif resposta == 4:
        Destaques(estado=input('Estado: '))

    elif resposta == 5:
        print('FIM DO PROGRAMA!')
        break
    elif str(resposta) == '':
        print(f'RESPOSTA INCORRETA - VOCÊ DIGITOU ({resposta})')

    else:
        print(f'RESPOSTA INCORRETA - VOCÊ DIGITOU ({resposta})')





