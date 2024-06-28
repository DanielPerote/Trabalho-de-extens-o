import sqlite3
from sqlite3 import Error

def ConexaoBanco():
    caminho="C:\\Users\\usuario\\Desktop\\Sqlite\\Banco\\extensão.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon=ConexaoBanco()

class Gestao:
    def __init__(self, banco):
        self.conn = sqlite3.connect(banco)
        self.criar_tabela_estoque()

    def criar_tabela_estoque(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS estoque (
                id INTEGER PRIMARY KEY,
                produto TEXT,
                quantidade INTEGER
            )
        ''')
        self.conn.commit()

    def criarTabela(conexao, sql):
        try:
            c=conexao.cursor()
            c.execute(sql)
            print("TAbela criada")
        except Error as ex:
            print(ex)
    vcon.close()  

    def adicionar_produto(self, produto, quantidade):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO estoque (produto, quantidade) VALUES (?, ?)", (produto, quantidade)
        )
        self.conn.commit()
    def remover_produto(self, produto, quantidade):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT quantidade FROM estoque WHERE produtos?", (produto,)
        )
        resultado = cursor.fetchone()
        if resultado:
            estoque_atual = resultado[0]
            if estoque_atual >= quantidade:
                cursor.execute("UPDATE estoque SET quantidade=? WHERE produto=?", (estoque_atual - quantidade, produto))
                self.conn.commit()
            else:
                print(f"Quantidade insuficiente de {produto} em estoque.")
        else:
            print(f"{produto} não encontrado em estoque.")

    def consultar_estoque(self, produto):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT quantidade FROM estoque WHERE produto=?", (produto,)
        )
        resultado = cursor.fetchone()
        if resultado:
            return resultado[0]
        else:
            return 0
        
    def listar_produtos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT produto FROM estoque")
        produto = cursor.fetchall()
        return [produto[0] for produto in produto]
    
sistema = Gestao("estoque.db")

sistema.adicionar_produto("Pao Arabe",25)
sistema.adicionar_produto("Pao Bola",20)
sistema.adicionar_produto("Pao de Forma",3)

estoque_Pao_Arabe = sistema.consultar_estoque("Pao_Arabe")
print(f"Quantidade de Pao em estoque:{estoque_Pao_Arabe}")

produtos_em_estoque = sistema.listar_produtos()
print(f"Produtos em estoque: {produtos_em_estoque}")