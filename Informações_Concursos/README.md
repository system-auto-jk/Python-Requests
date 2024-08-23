# Buscador de Concursos Públicos

Este projeto em Python permite a busca e visualização de informações sobre concursos públicos em diferentes estados do Brasil. Utilizando as bibliotecas `requests` e `BeautifulSoup`, o programa extrai dados de um site específico e exibe os concursos disponíveis em um formato amigável para o usuário.

## Funcionalidades

- **Buscar Concurso por Estado**: Permite ao usuário buscar um concurso específico em um estado escolhido.
- **Todos os Concursos por Estado**: Exibe todos os concursos públicos abertos em um estado.
- **Concursos de Prefeituras**: Mostra as últimas informações sobre concursos municipais.
- **Destaques por Estado**: Exibe os concursos em destaque em um estado selecionado.

## Pré-requisitos

Certifique-se de ter as seguintes bibliotecas instaladas:

```bash
pip install requests
pip install beautifulsoup4
```

## Como Usar

1. **Clone o Repositório**:

   ```bash
   git clone https://github.com/SeuUsuario/NomeDoRepositorio.git
   cd NomeDoRepositorio
   ```

2. **Execute o Programa**:

   Execute o script Python:

   ```bash
   python nome_do_arquivo.py
   ```

3. **Navegue pelas Opções**:

   Ao iniciar, o programa exibe um menu com as seguintes opções:

   - `[1] BUSCAR CONCURSO POR ESTADO`
   - `[2] TODOS OS CONCURSOS POR ESTADO`
   - `[3] ULTIMAS INFORMAÇÕES SOBRE CONCURSOS`
   - `[4] DESTAQUES POR ESTADO`
   - `[5] SAIR`

   Escolha a opção desejada e siga as instruções na tela.

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

Se você deseja contribuir com este projeto, sinta-se à vontade para enviar pull requests ou relatar problemas.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
