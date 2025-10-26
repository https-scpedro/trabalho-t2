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

def main(): # Função principal, executa o loop do programa
    while True:
        opcao = exibir_menu() # Exibe o menu de opções

        if opcao == '1':
            adicionar_contato() # Chama a função para adicionar um contato
        elif opcao == '2':
            listar_contatos() # Chama a função para listar contatos
        elif opcao == '3':
            atualizar_contato() # Chama a função para atualizar um contato
        elif opcao == '4':
            deletar_contato() # Chama a função para deletar um contato
        elif opcao == '5':
            print("Saindo do programa.")
            break # Quebra o loop e encerra o programa
        else:
            print("Opção inválida. Por favor, tente novamente.")
