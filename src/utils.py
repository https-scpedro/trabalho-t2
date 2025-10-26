import re

def formatar_telefone_salvar(telefone):
    # Remove os caracteres não numéricos de uma string de telefone.
    # Exemplo: "(11) 98888-8888" vira "11988888888"

    # re.sub() substitui padrões.
    # r'\D' é um regex que significa "qualquer caractere que NÃO seja um dígito".
    # '' é pelo que queremos substituir (ou seja, nada).
    return re.sub(r'\D', '', telefone)

def formatar_telefone_exibicao(telefone):
    # Formata uma string de dígitos de telefone para um padrão legível.
    # Exemplo: "11988888888" vira "(11) 98888-8888"

    # Limpa o telefone primeiro, caso ele venha de uma fonte não tratada
    telefone_limpo = formatar_telefone_salvar(telefone)
    
    # Formata para celular (11 dígitos: DD + 9 + XXXX-XXXX)
    if len(telefone_limpo) == 11:
        # Ex: (11) 98765-4321
        return f"({telefone_limpo[:2]}) {telefone_limpo[2:7]}-{telefone_limpo[7:]}"
    
    # Formata para fixo (10 dígitos: DD + XXXX-XXXX)
    elif len(telefone_limpo) == 10:
        # Ex: (11) 4444-5555
        return f"({telefone_limpo[:2]}) {telefone_limpo[2:6]}-{telefone_limpo[6:]}"
    
    # Se não for um formato padrão, apenas retorna o número limpo
    else:
        return telefone_limpo