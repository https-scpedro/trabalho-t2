# Trabalho T2: Agenda de Contatos em Python (CRUD)

Este projeto é um sistema de gerenciamento de contatos desenvolvido em Python como parte da avaliação do Trabalho T2 da disciplina de `Programação para Ciência de Dados`.

O programa implementa as quatro operações fundamentais de persistência de dados (CRUD) e utiliza um arquivo JSON como banco de dados.


## 1. Critérios de Avaliação

Os principais critérios de avaliação abordados foram:
* **Estruturação e organização do código (15 pts):** O projeto utiliza uma abordagem estruturada, separando responsabilidades em diferentes módulos (menu, lógica de negócio, persistência, utilitários) dentro de um pacote `src`.
* **Funcionalidades (CRUD completo - 20 pts):** O sistema permite Criar, Ler, Atualizar e Deletar contatos.
* **Persistência em arquivos (5 pts):** Os dados são persistidos em um arquivo `contatos.json`, permitindo que os registros sobrevivam ao fechamento do programa.
* **Clareza e legibilidade do código (5 pts):** O uso de nomes claros para funções e variáveis.
* **Comentários explicativos (5 pts):** O código é comentado para explicar a lógica e o funcionamento das partes essenciais.


## 2. Funcionalidades Principais

O sistema é controlado via um menu interativo no terminal e possui as seguintes funções:

* **1. Adicionar Contato:** Cria um novo registro de contato (nome, email, telefone).
* **2. Listar Contatos:** Exibe todos os contatos cadastrados de forma formatada.
* **3. Atualizar Contato:** Permite alterar o nome e/ou o telefone de um contato existente, buscando-o pelo seu email (usado como identificador único).
* **4. Excluir Contato:** Remove um contato da agenda, também buscando-o pelo email.


## 3. Estrutura do Projeto

O código foi organizado da seguinte maneira para garantir a separação de responsabilidades:

* **`main.py`**: Ponto de entrada do programa. Controla o menu e o loop principal.
* **`contatos.json`**: É o banco de dados, o arquivo onde os contatos são salvos.
* **`.gitignore`**: Arquivo que diz ao Git pastas para serem ignoradas (como pycache).
* **`README.md`**: Este arquivo de explicação.
* **`src/` (Pasta):** Esta pasta contém toda a lógica do programa.
    * **`__init__.py`**: Arquivo vazio que define a pasta `src` como um "pacote" Python.
    * **`funcoes_crud.py`**: Contém as funções principais (Adicionar, Listar, Atualizar, Deletar).
    * **`persistencia.py`**: Contém as funções que leem e salvam os dados no `contatos.json`.
    * **`utils.py`**: Funções auxiliares (formatar os números de telefone).


## 4. Como Executar

O projeto não requer a instalação de nenhuma biblioteca externa (além das que já vêm com o Python).

1.  Clone este repositório:
    ```bash
    git clone (https://github.com/https-scpedro/trabalho-t2.git)
    ```

2.  Navegue até a pasta do projeto:
    ```bash
    cd trabalho-t2
    ```

3.  Execute o programa:
    ```bash
    python main.py
    ```

