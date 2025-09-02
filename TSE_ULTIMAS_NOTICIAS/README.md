# 📰 Web Scraper - Notícias TSE

Este projeto é um **web scraper em Python** que coleta as últimas notícias do site oficial do **Tribunal Superior Eleitoral (TSE)**.

## 🚀 Funcionalidades
- Acessa automaticamente a página de notícias do TSE.
- Extrai os **títulos** e **links** das notícias.
- Exibe as informações no terminal de forma organizada.
- Pausa entre cada notícia para não sobrecarregar o site.
- Mantém o programa aberto até o usuário pressionar **Enter** para finalizar.

## 🛠️ Tecnologias utilizadas
- **Python 3**
- [Requests](https://pypi.org/project/requests/) → para realizar requisições HTTP.
- [BeautifulSoup (bs4)](https://pypi.org/project/beautifulsoup4/) → para processar e extrair dados do HTML.
- [Time](https://docs.python.org/3/library/time.html) → para controlar pausas entre exibição de notícias.

## 📦 Como executar
1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/tse-news-scraper.git
   cd tse-news-scraper
````

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Execute o script:

   ```bash
   python main.py
   ```

   > ℹ️ O programa exibirá os títulos e links das notícias do TSE e só será finalizado após você pressionar **Enter**.

## 📌 Exemplo de saída

```
Título da notícia 1
https://www.tse.jus.br/comunicacao/noticias/noticia1

Título da notícia 2
https://www.tse.jus.br/comunicacao/noticias/noticia2

Título da notícia 3
https://www.tse.jus.br/comunicacao/noticias/noticia3

Pressione Enter para finalizar o programa...
```

## 📚 Aprendizados

* Uso de **web scraping** para coletar notícias de órgãos oficiais.
* Manipulação de HTML com **BeautifulSoup**.
* Implementação de pausas entre requisições para evitar sobrecarga do servidor.
* Formatação de saída clara e organizada no terminal.

## 👨‍💻 Autor

Desenvolvido por **Erick Santos Silva**
🔗 [systemautojk.com.br](https://systemautojk.com.br)
📸 [@systemautojk](https://instagram.com/systemautojk)
