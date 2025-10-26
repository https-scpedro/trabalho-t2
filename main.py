# Importa as funções que o usuário pode executar
from funcoes_crud import adicionar_contato, listar_contatos, atualizar_contato, deletar_contato

def exibir_menu(): # Exibe o menu de opções
    print("\n ----- Menu de Contatos -----")
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Atualizar Contato")
    print("4. Excluir Contato")
    print("5. Sair")
    print("----------------------------")
    return input("Escolha uma opção: ")

