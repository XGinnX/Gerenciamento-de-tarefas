import sqlite3 as sql #pip install db-sqlite3
import datetime as dt

banco = sql.connect("gerenciamento.db")

cursor = banco.cursor()
# Criação da tabela de LOGS
try:
    cursor.execute('''CREATE TABLE Logs (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    log_data DATATIME,
    log_user_id INTEGER,
    log_title TEXT,
    log_description TEXT,
    )''')
    print("Tabela Criada com Sucesso!")
except:
    print("Erro: Tabela Já foi criada")

#cursor.execute("INSERT INTO usuarios (user_login, user_name, user_last_name, user_email, user_password) VALUES ('Jean_pai','Jean','Sales','jean.sls.snts@gmail.com','1234567')")

# Criação da tabela de Usuários
try:
    cursor.execute('''CREATE TABLE usuarios (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_login TEXT,
    user_name TEXT,
    user_last_name TEXT,
    user_email TEXT,
    user_password TEXT
    )''')
    print("Tabela Criada com Sucesso!")
except:
    print("Erro: Tabela Já foi criada")
    
def inserir_log(titulo, user_id, descricao):
    data = dt.datetime.now()
    cursor.execute("INSERT INTO Logs (log_data, log_user_id, log_title, log_description) VALUES (?,?,?,?)",(data,user_id,titulo,descricao))
    

def verificar_usuario(email):
    cursor.execute('SELECT * FROM usuarios WHERE user_email LIKE ?', ('%' + email + '%'))
    dados = cursor.fetchone()  # Usando fetchone para pegar apenas um resultado

    if dados:
        inserir_log("Logado com Sucesso", dados[0], "descricao teste")
        return True
    else:
        return False