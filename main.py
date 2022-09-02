from PySide2.QtWidgets import (QApplication, QMainWindow, QWidget, QMessageBox)
from ui_login import Ui_Login
from ui_PrimeiraTela import Ui_PrimeiraTela
import sys
from database import DataBase



class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.tentativa = 0
        self.setupUi(self)
        self.setWindowTitle("Login do A2B")
        self.btn_login.clicked.connect(self.checkLogin)



 # Checagem da Senha e Usuário #

    def checkLogin(self):

        self.users = DataBase()
        self.users.conecta()
        authenticated = self.users.check_user(self.btn_user.text().upper(), self.btn_passaword.text())

        if authenticated == "Administrador" or authenticated == "user":
            self.w = PrimeiraTela(authenticated)
            self.w.show()
            self.close()

        else:

            if self.tentativa < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro ao acessar")
                msg.setText(f'Login ou Senha incorreto! \n \n tentativa: {self.tentativa + 1} de 3')
                msg.exec_()
                self.tentativa += 1

            if self.tentativa == 3:
                self.users.close_connection()
                sys.exit(0)

# Acesso a Primeira página do Sistema #
class PrimeiraTela (QMainWindow, Ui_PrimeiraTela):
    def __init__(self, user):
        super(PrimeiraTela, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de Gerenciamento A2B")

        if user == "user":
            self.bt_cadrastrar_usuario.setVisible(False)


        # Acesso paginas do Sistemas #
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_table.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_table))
        self.btn_contato.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_contato))
        self.btn_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_sobre))
        self.btn_import.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_import))
        self.bt_cadrastrar_usuario.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro))




        self.btn_cadastrar.clicked.connect(self.subscribe_user)


    def subscribe_user(self):

        if self.txt_senha.text() != self.txt_senha_2.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Senhas divergentes")
            msg.setText("As senhas não são iguais!")
            msg.exec_()
            return None

        nome = self.txt_nome.text()
        user = self.txt_usuario.text()
        password = self.txt_senha.text()
        access = self.cb_perfil.currentText()

        db = DataBase()
        db.conecta()
        db.insert_user(nome, user, password, access)
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Cadastro do usuário")
        msg.setText("Cadrastro realizado com sucesso!")
        msg.exec_()

        self.txt_nome.setText("")
        self.txt_usuario.setText("")
        self.txt_senha.setText("")
        self.txt_senha_2.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()
