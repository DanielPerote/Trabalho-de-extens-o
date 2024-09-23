import pandas as pd  
from datetime import datetime

# Inicializar DataFrame para armazenar as transações
columns = ['data', 'descricao', 'tipo', 'valor']
transacoes = pd.DataFrame(columns=columns)

# Função para adicionar uma transação
def adicionar_transacao(descricao, tipo, valor):
    global transacoes
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nova_transacao = pd.DataFrame([[data, descricao, tipo, valor]], columns=columns)
    transacoes = pd.concat([transacoes, nova_transacao], ignore_index=True)
    print(f"Transação adicionada: {descricao}, {tipo}, {valor}")

# Função para adicionar entrada de caixa
def adicionar_entrada(descricao, valor):
    adicionar_transacao(descricao, 'entrada', valor)

# Função para adicionar saída de caixa
def adicionar_saida(descricao, valor):
    adicionar_transacao(descricao, 'saída', valor)

# Função para encerrar o caixa e gerar relatório
def encerrar_caixa():
    global transacoes
    total_entradas = transacoes[transacoes['tipo'] == 'entrada']['valor'].sum()
    total_saidas = transacoes[transacoes['tipo'] == 'saída']['valor'].sum()
    saldo_final = total_entradas - total_saidas

    print("\nRelatório de Encerramento de Caixa")
    print("---------------------------------")
    print(f"Total de Entradas: R$ {total_entradas:.2f}")
    print(f"Total de Saídas:   R$ {total_saidas:.2f}")
    print(f"Saldo Final:       R$ {saldo_final:.2f}")

    # Salvar relatório em arquivo CSV
    transacoes.to_csv('relatorio_caixa.csv', index=False)
    print("\nRelatório salvo em 'relatorio_caixa.csv'")

    # Resetar o DataFrame para o próximo dia
    transacoes = pd.DataFrame(columns=columns)

# Exemplo de uso
if __name__ == "_main_":
    adicionar_entrada("Venda de produto X", 150.00)
    adicionar_entrada("Venda de produto Y", 200.00)
    adicionar_saida("Compra de materiais", 100.00)
    adicionar_saida("Pagamento de contas", 50.00)

    encerrar_caixa()