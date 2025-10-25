# Importa a biblioteca json para manipulação de dados
import json 

NOME_ARQUIVO = 'contatos.json'

def carregar_dados():
    # Carrega os dados do arquivo JSON
    # Se o arquivo não existir, retorna uma lista vazia

    try:
        with open(NOME_ARQUIVO, 'r') as arquivo:
            return json.load(arquivo) # Lê o arquivo e retorna uma lista em um objeto Python
        
    except (FileNotFoundError, json.JSONDecodeError):
        return [] # Retorna uma lista vazia se o arquivo não existir ou estiver vazio
    
def salvar_dados(contatos):
    # Salva os dados no arquivo JSON
    
    with open(NOME_ARQUIVO, 'w') as arquivo:
        json.dump(contatos, arquivo, indent=4) # Escreve a lista de contatos no arquivo com indentação para melhor legibilidade