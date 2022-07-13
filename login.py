from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QMessageBox, QWidget, QApplication
import mysql.connector


class Ui_Login(QWidget):

    # Sinal emitido para retornar ao menu
    loginToMenuSignal = pyqtSignal(name = "loginToMenuSignal")
    loginToEditMenuSignal = pyqtSignal(name = "loginToEditMenuSignal")

    def switchToMenu(self):
        self.loginToMenuSignal.emit()

    def switchToEditMenu(self):
        self.loginToEditMenuSignal.emit()





    # Função que checa os dados do Login    
    def login(self):
        email = self.emailTB.text()
        senha = self.senhaTB.text()

        if(self.emailTB.text() == ''):
            self.emailVazioMSG()


        elif(self.senhaTB.text() == ''):
            self.senhaVazioMSG()

        else:
            # Conecta ao banco de dados
            mydb = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "35c4p3fromh3ll",
                database = "trabalhopoo"
            )
            mycursor = mydb.cursor()

            checaEmail = "SELECT email FROM funcionarios WHERE email = %s"
            data = (email,)
            mycursor.execute(checaEmail, data)
            
            listaEmail = mycursor.fetchall()



            if(listaEmail == []):
                self.usuarioInexistenteMSG()
            else:
                checaSenha = "SELECT email, senha FROM funcionarios WHERE email = %s"
                data = (email,)
                mycursor.execute(checaSenha, data)
                
                listaLogin = mycursor.fetchall()

                if(str(listaLogin[0][1]) != str(senha)):
                    self.senhaInvalidaMSG()
                else:
                    checaSenha = "SELECT nome FROM funcionarios WHERE email = %s"
                    data = (email,)
                    mycursor.execute(checaSenha, data)
                
                    nome = mycursor.fetchall()
                    self.loginSucedidoMSG(nome)
                    self.switchToEditMenu()

                    # Encerra a conexão com o banco
                    mycursor.close()
                    mydb.close()
                    
        





    def setupUi(self, Login):


        Login.setObjectName("Login")
        Login.resize(300, 250)
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")



# Labels

        self.emailLabel = QtWidgets.QLabel(self.centralwidget)
        self.emailLabel.setGeometry(QtCore.QRect(50, 30, 50, 30))
        self.emailLabel.setObjectName("emailLabel")



        self.senhaLabel = QtWidgets.QLabel(self.centralwidget)
        self.senhaLabel.setGeometry(QtCore.QRect(50, 90, 50, 30))
        self.senhaLabel.setObjectName("senhaLabel")



# Text Boxes

        self.emailTB = QtWidgets.QLineEdit(self.centralwidget)
        self.emailTB.setGeometry(QtCore.QRect(100, 30, 120, 30))
        self.emailTB.setObjectName("emailTB")



        self.senhaTB = QtWidgets.QLineEdit(self.centralwidget)
        self.senhaTB.setGeometry(QtCore.QRect(100, 90, 120, 30))
        self.senhaTB.setObjectName("senhaTB")

        # Transformando os caracteres do campo de senha
        self.senhaTB.setEchoMode(QtWidgets.QLineEdit.Password)



# Buttons

        self.loginBTN = QtWidgets.QPushButton(self.centralwidget)
        self.loginBTN.setGeometry(QtCore.QRect(160, 150, 100, 30))
        self.loginBTN.setObjectName("loginBTN")

        # Entra na tela de edição do cardápio
        self.loginBTN.clicked.connect(self.login)



        self.voltarBTN = QtWidgets.QPushButton(self.centralwidget)
        self.voltarBTN.setGeometry(QtCore.QRect(40, 150, 100, 30))
        self.voltarBTN.setObjectName("voltarBTN")

        # Volta para o menu
        self.voltarBTN.clicked.connect(self.switchToMenu)



        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.emailLabel.setText(_translate("Login", "Email:"))
        self.senhaLabel.setText(_translate("Login", "Senha:"))
        self.loginBTN.setText(_translate("Login", "Login"))
        self.voltarBTN.setText(_translate("Login", "Voltar"))





# Mensagens de tratamento de dados do login

    def emailVazioMSG(self):
        msg = QMessageBox()
        msg.setWindowTitle("Email vazio!")
        msg.setText("Por favor, entre com o email!")

        msg.exec_()



    def senhaVazioMSG(self):
        msg = QMessageBox()
        msg.setWindowTitle("Senha vazia!")
        msg.setText("Por favor, entre com a senha!")

        msg.exec_()



    def senhaInvalidaMSG(self):
        msg = QMessageBox()
        msg.setWindowTitle("Senha inválida!")
        msg.setText("A senha inserida está incorreta!")

        msg.exec_()
    


    def usuarioInexistenteMSG(self):
        msg = QMessageBox()
        msg.setWindowTitle("Email inválido!")
        msg.setText("O email não está cadastrado!")

        msg.exec_()



# Menagens de ações bem sucedidas

    def loginSucedidoMSG(self, nome):
        msg = QMessageBox()
        msg.setWindowTitle("Login realizado!")
        msg.setText("Seu login foi efetuado com sucesso! Bem vindo " + str(nome[0][0]) + "!")

        msg.exec_()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
