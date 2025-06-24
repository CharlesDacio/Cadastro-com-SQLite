import sqlite3

def conectar():
    return sqlite3.connect("usuarios.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def cadastrar_usuario():
    nome = input("Nome: ")
    email = input("E-mail: ")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
    conn.commit()
    conn.close()
    print("Usuário cadastrado com sucesso!\n")

def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    if not usuarios:
        print("Nenhum usuário encontrado.\n")
        return
    for usuario in usuarios:
        print(f"ID: {usuario[0]}, Nome: {usuario[1]}, E-mail: {usuario[2]}")
    print()

def editar_usuario():
    listar_usuarios()
    try:
        user_id = int(input("Digite o ID do usuário para editar: "))
        nome = input("Novo nome: ")
        email = input("Novo e-mail: ")
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE usuarios SET nome = ?, email = ? WHERE id = ?", (nome, email, user_id))
        conn.commit()
        conn.close()
        print("Usuário atualizado com sucesso!\n")
    except:
        print("Erro ao editar. Verifique o ID.\n")

def excluir_usuario():
    listar_usuarios()
    try:
        user_id = int(input("Digite o ID do usuário para excluir: "))
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (user_id,))
        conn.commit()
        conn.close()
        print("Usuário excluído com sucesso!\n")
    except:
        print("Erro ao excluir. Verifique o ID.\n")

def menu():
    criar_tabela()
    while True:
        print("1. Cadastrar usuário")
        print("2. Listar usuários")
        print("3. Editar usuário")
        print("4. Excluir usuário")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            editar_usuario()
        elif opcao == "4":
            excluir_usuario()
        elif opcao == "5":
            break
        else:
            print("Opção inválida.\n")

if __name__ == "__main__":
    menu()