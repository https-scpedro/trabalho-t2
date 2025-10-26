# Importa as funções de persistência de dados e formatação de telefone
from src.persistencia import salvar_dados, carregar_dados
from src.utils import formatar_telefone_salvar, formatar_telefone_exibicao

# Função para adicionar um novo contato
def adicionar_contato():
    print ("\n --- Adicionar Contato ---")
    nome = input("Digite o nome: ")
    email = input("Digite o email: ")
    telefone = input("Digite o telefone: ")

    contatos = carregar_dados() # Carrega a lista de contatos existente

    # Verifica se o email já existe
    for contato in contatos:
        if contato['email'] == email:
            print("\nErro: Já existe um contato com este email.")
            return
        
    # Padroniza o telefone para salvar
    telefone_formatado = formatar_telefone_salvar(telefone)
        
    # Cria um dicionário para o novo contato
    novo_contato = {
        'nome': nome,
        'email': email,
        'telefone': telefone_formatado
    }

    # Adiciona o novo contato à lista
    contatos.append(novo_contato)

    # Salva a lista atualizada de contatos
    salvar_dados(contatos)

    print(f"\nContato {nome} adicionado com sucesso.")


# Função para listar todos os contatos
def listar_contatos():
    print("\n --- Lista de Contatos ---")
    contatos = carregar_dados() # Carrega a lista de contatos

    # Verifica se a lista está vazia
    if not contatos:
        print("Nenhum contato encontrado.")
        return
    

    # Percorre a lista e exibe cada contato
    for i, contato in enumerate(contatos, start=1):
        # Pega o telefone salvo (só dígitos) e formata para exibição
        telefone_exibicao = formatar_telefone_exibicao(contato['telefone'])

        print(f"\n {i}. Nome: {contato['nome']}")
        print(f"Email: {contato['email']}")
        print(f"Telefone: {telefone_exibicao}")


# Função para atualizar um contato
def atualizar_contato():
    print("\n --- Atualizar Contato ---")
    email_search = input("Digite o email do contato a ser atualizado: ")

    contatos = carregar_dados() # Carrega a lista de contatos

    contato_encontrado = None

    # Procura o contato na lista pelo email
    for contato in contatos:
        if contato['email'] == email_search:
            contato_encontrado = contato
            break # Sai do loop se encontrar o contato

    if contato_encontrado:
        print("Contato encontrado. Deixe em branco para não alterar.")

        # Formata o telefone para exibição
        telefone_atual_exibicao = formatar_telefone_exibicao(contato_encontrado['telefone'])

        novo_nome = input(f"Novo nome ({contato_encontrado['nome']}): ")
        novo_telefone = input(f"Novo telefone ({telefone_atual_exibicao}): ")

        # Atualiza os dados do contato se novos valores forem fornecidos
        if novo_nome:
            contato_encontrado['nome'] = novo_nome
        if novo_telefone:
            contato_encontrado['telefone'] = formatar_telefone_salvar(novo_telefone)

        # Salva a lista atualizada de contatos
        salvar_dados(contatos)
        print("\nContato atualizado com sucesso.")
    else:
        print("\nContato não encontrado.")

# Função para deletar um contato
def deletar_contato(): 
    print("\n --- Excluir Contato ---")
    email_delete = input("Digite o email do contato a ser excluído: ")

    contatos = carregar_dados() # Carrega a lista de contatos

    contato_remove = None

    # Procura o contato na lista pelo email
    for contato in contatos:
        if contato['email'] == email_delete:
            contato_remove = contato
            break # Sai do loop se encontrar o contato

    if contato_remove: 
        contatos.remove(contato_remove) # Remove o contato da lista

        # Salva a lista atualizada de contatos
        salvar_dados(contatos)
        print("\nContato excluído com sucesso.")
    else:
        print("\nContato não encontrado.")
