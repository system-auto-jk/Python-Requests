# Python-Requests: Informações sobre Concursos Públicos

Este projeto em Python foi desenvolvido para buscar e exibir informações sobre concursos públicos em diferentes estados do Brasil. Utilizando as bibliotecas `requests` e `BeautifulSoup`, o programa acessa um site específico e extrai dados de interesse.

## Estrutura do Projeto

- **[Informações_Concursos](https://github.com/system-auto-jk/Python-Requests/tree/main/Informa%C3%A7%C3%B5es_Concursos)**: Diretório que contém o código principal do projeto, responsável pela coleta e exibição das informações sobre concursos públicos.

## Funcionalidades

- **Buscar Concurso por Estado**: Permite buscar por um concurso específico em um estado escolhido.
- **Todos os Concursos por Estado**: Lista todos os concursos públicos abertos em um estado.
- **Concursos de Prefeituras**: Exibe as últimas informações sobre concursos municipais.
- **Destaques por Estado**: Mostra os concursos em destaque em um estado selecionado.

## Pré-requisitos

Certifique-se de ter as seguintes bibliotecas instaladas:

```bash
pip install requests
pip install beautifulsoup4
```

## Como Usar

1. **Clone o Repositório**:

   ```bash
   git clone https://github.com/system-auto-jk/Python-Requests.git
   cd Python-Requests/Informações_Concursos
   ```

2. **Execute o Programa**:

   Dentro do diretório `Informações_Concursos`, execute o script Python:

   ```bash
   python ConcursoBrasil.py
   ```

3. **Navegue pelas Opções**:

   O programa apresenta um menu interativo onde você pode escolher as opções disponíveis para a busca de concursos.

## Exemplo de Uso

- **Buscar um Concurso por Estado**:

  ```bash
  Escolha a Opção: 1
  Concurso: PROFESSOR
  Estado: bahia
  ```

- **Listar Todos os Concursos em um Estado**:

  ```bash
  Escolha a Opção: 2
  Estado: bahia
  ```

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou relatar problemas.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
