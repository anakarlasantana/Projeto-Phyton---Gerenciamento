import sqlite3


# Criação do Banco de Dados - nome: system.bd


class DataBase():
    def __init__(self, name='system.bd') -> None:
        self.name = name

    def conecta(self):
        self.connection = sqlite3.connect(self.name)


    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass

    # Criar tabela #

    def create_table_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(""" 
            
                 CREATE TABLE IF NOT EXISTS users(
                 
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    user TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    access TEXT NOT NULL
                
                );
            """)

        except AttributeError:
            print('Faça a conexão com o banco!')

    # Método para inserir o usuários no banco de dados #

    def insert_user(self, name, user, password, access):

        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                
                INSERT INTO USERS(name, user, password, access) VALUES(?,?,?,?)
            
            """, (name, user, password, access))


            self.connection.commit()

        except AttributeError:
            print ('Faça a conexão!')

    # Método para fazer a checagem do usuário #

    def check_user(self, user, password) -> object:

        try:
            cursor = self.connection.cursor()
            cursor.execute("""
        
                 SELECT * FROM users;
        
                      """)

            for linha in cursor.fetchall():
               if linha[2].upper() == user.upper() and linha[3] == password and linha [4] == "Administrador":
                    return "Administrador"

               elif linha[2].upper() == user.upper() and linha[3] == password and linha [4] == "Usuário":
                    return "user"


               else:
                    continue

               return "Sem acesso"

        except:
            pass


    # Executar a classe #

if __name__ == "__main__":
    db = DataBase()
    db.conecta()
    db.create_table_users()
    db.close_connection()
