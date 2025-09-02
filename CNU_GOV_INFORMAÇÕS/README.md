# 📰 Web Scraper - Últimas Notícias sobre o CNU (Concurso Nacional Unificado)

Este projeto é um **web scraper em Python** que coleta as **3 notícias mais recentes** sobre o **CNU (Concurso Nacional Unificado)** diretamente do portal oficial do Governo Federal.

## 🚀 Funcionalidades
- Acessa automaticamente o site do Governo Federal.
- Extrai os **títulos** e **links** das 3 últimas notícias do CNU.
- Exibe as informações no terminal de forma organizada.
- Mantém o programa aberto até o usuário pressionar **Enter** para finalizar.

## 🛠️ Tecnologias utilizadas
- **Python 3**
- [Requests](https://pypi.org/project/requests/) → para realizar a requisição HTTP.
- [BeautifulSoup (bs4)](https://pypi.org/project/beautifulsoup4/) → para processar e extrair dados do HTML.
- [Time](https://docs.python.org/3/library/time.html) → para adicionar pausas no processamento.

## 📦 Como executar
1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/cnu-news-scraper.git
   cd cnu-news-scraper
````

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Execute o script:

   ```bash
   python main.py
   ```

   > ℹ️ O programa exibirá as últimas 3 notícias sobre o CNU e só será finalizado após você pressionar **Enter**.

## 📌 Exemplo de saída

```
- BUSCANDO INFORMAÇÕES SOBRE O CNU -

Título: Inscrições do Concurso Nacional Unificado são prorrogadas
Link: https://www.gov.br/gestao/pt-br/concursonacional/noticias/inscricoes-prorrogadas

Título: Governo Federal divulga locais de prova do CNU
Link: https://www.gov.br/gestao/pt-br/concursonacional/noticias/locais-de-prova

Título: Publicado edital complementar do CNU
Link: https://www.gov.br/gestao/pt-br/concursonacional/noticias/edital-complementar

- PROGRAMA INFORMAÇÕES SOBRE O CNU FINALIZADO - 

Pressione Enter para finalizar o programa...
```

## 📚 Aprendizados

* Aplicação de **web scraping** para coletar notícias em sites governamentais.
* Uso de **BeautifulSoup** para navegar no HTML.
* Extração seletiva de informações específicas (últimos 3 títulos e links).
* Pausa no terminal para evitar fechamento automático.

## 👨‍💻 Autor

Desenvolvido por **Erick Santos Silva**
🔗 [systemautojk.com.br](https://systemautojk.com.br)
📸 [@systemautojk](https://instagram.com/systemautojk)
