import textwrap

def menu():
    """Exibe o menu de opções e retorna a escolha do usuário."""
    menu = """\n
    =============== MENU ===============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [c]\tNova conta
    [u]\tNovo usuário
    [l]\tListar contas
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    """
    Realiza a operação de depósito.
    Argumentos são obrigatórios por POSIÇÃO.
    Retorna o novo saldo e o extrato atualizado.
    """
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n--- Operação falhou! O valor informado é inválido. ---")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Realiza a operação de saque.
    Argumentos são obrigatórios por NOME (keyword-only).
    Retorna o novo saldo e o extrato atualizado, ou o saldo e extrato originais.
    """
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n--- Operação falhou! Você não tem saldo suficiente. ---")

    elif excedeu_limite:
        print("\n--- Operação falhou! O valor do saque excede o limite. ---")

    elif excedeu_saques:
        print("\n--- Operação falhou! Número máximo de saques excedido. ---")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
        return saldo, extrato, numero_saques
    
    else:
        print("\n--- Operação falhou! O valor informado é inválido. ---")
    
    return saldo, extrato, numero_saques

def visualizar_historico(saldo, /, *, extrato):
    """
    Exibe o extrato da conta.
    O saldo é passado por POSIÇÃO e o extrato por NOME.
    """
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def filtrar_usuario(cpf, usuarios):
    """
    Filtra um usuário na lista pelo CPF.
    Retorna o objeto usuário se encontrado, ou None.
    """
    # Remove qualquer caractere não numérico do CPF
    cpf_limpo = "".join(filter(str.isdigit, cpf))
    
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf_limpo]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    """
    Cria um novo usuário e o adiciona à lista se o CPF for inédito.
    """
    cpf = input("Informe o CPF (somente números): ")
    
    # 1. Verifica se o usuário já existe
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n--- Operação falhou! Já existe usuário com este CPF! ---")
        return

    # 2. Coleta os demais dados
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    
    # Endereço no formato: logradouro, nro - bairro - cidade/sigla estado
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    # 3. Adiciona o novo usuário
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuário criado com sucesso! ===")

def criar_conta(agencia, proximo_numero_conta, usuarios):
    """
    Cria uma nova conta corrente e a vincula a um usuário existente.
    """
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        # Cria a conta e vincula o usuário (objeto/dicionário)
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": proximo_numero_conta, "usuario": usuario}
    
    print("\n--- Usuário não encontrado, fluxo de criação de conta encerrado! ---")
    return None

def listar_contas(contas):
    """
    Exibe todas as contas cadastradas.
    """
    if not contas:
        print("\n--- Não há contas cadastradas. ---")
        return
        
    print("\n============ LISTA DE CONTAS ============")
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            CPF:\t\t{conta['usuario']['cpf']}
        """
        print(textwrap.dedent(linha))
    print("==========================================")


def main():
    # Variáveis de Estado (Movidas para o main)
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    
    usuarios = []
    contas = []
    
    proximo_numero_conta = 1

    while True:
        opcao = menu()

        if opcao == "d":
            try:
                valor = float(input("Informe o valor do depósito: "))
            except ValueError:
                print("\n--- Operação falhou! Valor digitado inválido. ---")
                continue
            
            # Chamada da função DEPOSITAR (argumentos posicionais)
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            try:
                valor = float(input("Informe o valor do saque: "))
            except ValueError:
                print("\n--- Operação falhou! Valor digitado inválido. ---")
                continue
            
            # Chamada da função SACAR (argumentos nomeados)
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            # Chamada da função EXTRATO (posicional e nomeado)
            visualizar_historico(saldo, extrato=extrato)

        elif opcao == "u":
            # Chamada da função CRIAR USUÁRIO
            criar_usuario(usuarios)
            
        elif opcao == "c":
            # Chamada da função CRIAR CONTA CORRENTE
            nova_conta = criar_conta(AGENCIA, proximo_numero_conta, usuarios)
            if nova_conta:
                contas.append(nova_conta)
                proximo_numero_conta += 1
                
        elif opcao == "l":
            # Chamada da função LISTAR CONTAS
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("\n--- Operação inválida, por favor selecione novamente a operação desejada. ---")

if __name__ == "__main__":
    main()