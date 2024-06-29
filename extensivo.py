import sqlite3

# Função para conectar ao banco de dados
def connect_db():
    return sqlite3.connect('simple_inventory.db')

# Função para adicionar um novo item ao estoque
def add_item(name, quantity):
    conn = connect_db()
    c = conn.cursor()
    c.execute("INSERT INTO inventory (name, quantity) VALUES (?, ?)", (name, quantity))
    conn.commit()
    conn.close()
    print(f"Item '{name}' adicionado com quantidade {quantity}.")

# Função para remover um item do estoque
def remove_item(name, quantity):
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT quantity FROM inventory WHERE name=?", (name,))
    result = c.fetchone()
    if result:
        current_quantity = result[0]
        if current_quantity >= quantity:
            new_quantity = current_quantity - quantity
            c.execute("UPDATE inventory SET quantity=? WHERE name=?", (new_quantity, name))
            conn.commit()
            print(f"Item '{name}' removido com quantidade {quantity}.")
        else:
            print(f"Quantidade insuficiente no estoque para remover {quantity} unidades de '{name}'.")
    else:
        print(f"Item '{name}' não encontrado no estoque.")
    conn.close()

# Função para visualizar todos os itens no estoque
def view_inventory():
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT * FROM inventory")
    items = c.fetchall()
    conn.close()
    print("Estoque Atual:")
    for item in items:
        print(f"ID: {item[0]}, Nome: {item[1]}, Quantidade: {item[2]}")

# Função principal para exibir o menu e gerenciar as operações
def main():
    while True:
        print("\nControle de Estoque")
        print("1. Adicionar Item")
        print("2. Remover Item")
        print("3. Visualizar Estoque")
        print("4. Sair")
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            name = input("Nome do item: ")
            quantity = int(input("Quantidade: "))
            add_item(name, quantity)
        elif choice == '2':
            name = input("Nome do item: ")
            quantity = int(input("Quantidade a remover: "))
            remove_item(name, quantity)
        elif choice == '3':
            view_inventory()
        elif choice == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "_main_":
    main()
add_item(name="goiabada", quantity=3)