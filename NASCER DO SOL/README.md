# 🌦️ Web Scraper de Previsão do Tempo - Lauro de Freitas (BA)

Este projeto é um **web scraper em Python** que coleta informações de previsão do tempo diretamente do site [Climatempo](https://www.climatempo.com.br/), especificamente para a cidade de **Lauro de Freitas - BA**.

## 🚀 Funcionalidades
- Extrai o texto principal da previsão do tempo.
- Identifica e exibe informações sobre **nascer e pôr do sol** no dia.
- Remove espaços extras para melhorar a legibilidade das informações.
- Mantém o programa aberto após a execução, exibindo a mensagem *"Pressione Enter para finalizar o programa..."*.

## 🛠️ Tecnologias utilizadas
- **Python 3**
- [Requests](https://pypi.org/project/requests/) → para realizar a requisição HTTP.
- [BeautifulSoup (bs4)](https://pypi.org/project/beautifulsoup4/) → para processar e extrair dados do HTML.

## 📦 Como executar
1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/previsao-tempo-scraper.git
   cd previsao-tempo-scraper
````

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Execute o script:

   ```bash
   python main.py
   ```

   > ℹ️ O programa exibirá a previsão e só será finalizado após você pressionar **Enter**.

## 📌 Exemplo de saída

```
Hoje será parecido com ontem Sol com algumas nuvens. Chove rápido durante o dia e à noite.
Nascer do sol: 05:37:39h
Pôr do sol: 17:29:10h

Pressione Enter para finalizar o programa...
```

## 📚 Aprendizados

* Uso de **web scraping** para extrair informações de sites.
* Manipulação de HTML com **BeautifulSoup**.
* Tratamento de strings e remoção de espaços extras em Python.
* Formatação de saída para exibir dados mais claros.
* Implementação de pausa no terminal para evitar que a janela feche imediatamente.

## 👨‍💻 Autor

Desenvolvido por **Erick Santos Silva**
🔗 [systemautojk.com.br](https://systemautojk.com.br)
📸 [@systemautojk](https://instagram.com/systemautojk)
