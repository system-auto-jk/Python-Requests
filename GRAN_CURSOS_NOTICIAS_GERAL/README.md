# 📰 Web Scraper - Gran Cursos Online

Este projeto é um **web scraper em Python** que monitora o **blog Gran Cursos Online**, coletando notícias das principais editorias e exibindo novas informações assim que forem publicadas.

## 🚀 Funcionalidades
- Coleta títulos e links das notícias das seguintes editorias:
  - Polícia, Concurso Fiscal, Tribunais, Concurso Jurídico, Concurso Professor, Concurso Militar, Área Saúde, Área TI, Diplomata
- Detecta automaticamente **novas notícias** publicadas e exibe no terminal.
- Evita exibir notícias repetidas.
- Mantém o programa rodando em **loop infinito**, permitindo monitoramento contínuo.
- Pausa entre solicitações para evitar sobrecarga do site.

## 🛠️ Tecnologias utilizadas
- **Python 3**
- [Requests](https://pypi.org/project/requests/) → para realizar requisições HTTP.
- [BeautifulSoup (bs4)](https://pypi.org/project/beautifulsoup4/) → para processar e extrair dados do HTML.
- [Time](https://docs.python.org/3/library/time.html) → para controlar pausas e intervalos entre requisições.

## 📦 Como executar
1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/gran-cursos-scraper.git
   cd gran-cursos-scraper
````

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Execute o script:

   ```bash
   python main.py
   ```

   > ℹ️ O programa exibirá notícias antigas na primeira execução e continuará rodando, mostrando novas publicações assim que detectadas.

## 📌 Exemplo de saída

```
INFORMAÇÕES SOBRE - policia

Título da notícia antiga
https://blog.grancursosonline.com.br/...

Nova informação sobre - Policia
Título da notícia nova
https://blog.grancursosonline.com.br/...
```

## 📚 Aprendizados

* Aplicação de **web scraping contínuo** para monitoramento de notícias.
* Uso de listas para evitar repetição de informações.
* Implementação de **loop infinito** com pausas estratégicas para não sobrecarregar o servidor.
* Extração de títulos e links de forma organizada.

## 👨‍💻 Autor

Desenvolvido por **Erick Santos Silva**
🔗 [systemautojk.com.br](https://systemautojk.com.br)
📸 [@systemautojk](https://instagram.com/systemautojk)

---

⚠️ **Aviso:** Este projeto tem fins educativos. Estrutura do site pode mudar, o que pode afetar o funcionamento do scraper.

```

---

Se você quiser, Erick, posso **montar o `requirements.txt` + `.gitignore`** já formatados igual aos outros projetos, prontos pra GitHub.  

Quer que eu faça isso agora?
```
