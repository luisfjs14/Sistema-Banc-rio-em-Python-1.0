# 🏦 Sistema Bancário Simples (v1.0 - Modularizado)

Este projeto é uma refatoração e expansão de um sistema bancário simples, implementado em Python, com o objetivo de demonstrar boas práticas de modularização, uso de funções com regras específicas de passagem de argumentos (positional-only e keyword-only), e gerenciamento de usuários e contas.

## 🚀 Funcionalidades

O sistema oferece as seguintes operações:

| Opção | Comando | Descrição |
| :---: | :---: | :--- |
| **D** | `Depositar` | Realiza um depósito na conta. |
| **S** | `Sacar` | Realiza um saque, respeitando o limite diário (`R$ 500,00`) e a quantidade de saques (`3`). |
| **E** | `Extrato` | Exibe o histórico de movimentações e o saldo atual. |
| **U** | `Novo usuário` | Cadastra um novo cliente (pessoa física) no sistema, verificando a duplicidade de CPF. |
| **C** | `Nova conta` | Cria uma nova conta corrente e a vincula a um usuário existente. |
| **L** | `Listar contas` | Exibe todas as contas correntes cadastradas. |
| **Q** | `Sair` | Encerra o programa. |

---

## 💻 Requisitos de Implementação (Desafio)

O código foi reestruturado para atender aos seguintes requisitos de modularização e boas práticas:

### 1. Separação em Funções

Todas as operações principais foram encapsuladas em funções distintas para melhorar a legibilidade e manutenção.

### 2. Regras de Passagem de Argumentos

| Função | Regra de Argumentos | Argumentos Recebidos |
| :---: | :---: | :--- |
| **`depositar`** | Argumentos **Apenas por Posição** (`/`) | `(saldo, valor, extrato, /)` |
| **`sacar`** | Argumentos **Apenas por Nome** (`*`) | `(*, saldo, valor, extrato, limite, numero_saques, limite_saques)` |
| **`visualizar_historico`** | Posição e Nome (misto) | `(saldo, /, *, extrato)` |

### 3. Gerenciamento de Usuários (Clientes)

* Os usuários são armazenados em uma lista de dicionários.
* Um usuário é composto por: **Nome**, **Data de Nascimento**, **CPF** (somente números) e **Endereço**.
* É implementada a validação para impedir o cadastro de 2 usuários com o mesmo CPF.

### 4. Gerenciamento de Contas Correntes

* As contas são armazenadas em uma lista de dicionários.
* Uma conta é composta por: **Agência**, **Número da Conta** e **Usuário** (vinculado).
* **Agência Fixa:** `"0001"`.
* **Número da Conta:** Sequencial, iniciando em 1.
* Um usuário pode ter múltiplas contas, mas cada conta pertence a um único usuário. O vínculo é realizado buscando o usuário pelo CPF.

---

## 🛠️ Como Executar

1.  **Copie o Código:** Salve todo o código-fonte Python em um arquivo no seu computador (sugestão: `banco.py`).

2.  **Execute o script no terminal:**
    Abra seu terminal ou prompt de comando, navegue até o diretório onde você salvou o arquivo e execute:
    ```bash
    python banco.py
    ```

### Exemplo de Uso:

Ao iniciar o programa, você verá o menu:

=============== MENU =============== 
[d] Depositar 
[s] Sacar 
[e] Extrato 
[c] Nova conta 
[u] Novo usuário 
[l] Listar contas 
[q] Sair 

Você deve começar cadastrando um usuário (`u`) e, em seguida, uma conta (`c`) para poder realizar as operações de depósito e saque.

---

## ✒️ Autor

* **Luís** ([@luisfjs14](https://github.com/luisfjs14))
