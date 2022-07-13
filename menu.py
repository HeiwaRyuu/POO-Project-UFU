from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QMessageBox, QWidget, QApplication




class Ui_Menu(QWidget):


    # Sinais emitidos para a troca de janelas

    menuToClientesSignal = pyqtSignal(name = "menuToClientesSignal")
    menuToFuncionariosSignal = pyqtSignal(name = "menuToFuncionariosSignal")
    menuToLoginSignal = pyqtSignal(name = "menuToLoginSignal")

    def switchToClientes(self):
        self.menuToClientesSignal.emit()

    def switchToFuncionarios(self):
        self.menuToFuncionariosSignal.emit()

    def switchToLogin(self):
        self.menuToLoginSignal.emit()




    def setupUi(self, Menu):


        Menu.setObjectName("Menu")
        Menu.resize(300, 250)
        self.centralwidget = QtWidgets.QWidget(Menu)
        self.centralwidget.setObjectName("centralwidget")



        self.CClienteBTN = QtWidgets.QPushButton(self.centralwidget)
        self.CClienteBTN.setGeometry(QtCore.QRect(90, 20, 120, 30))
        self.CClienteBTN.setObjectName("CClienteBTN")

        # Abre a janela Clientes
        self.CClienteBTN.clicked.connect(self.switchToClientes)



        self.CFuncionarioBTN = QtWidgets.QPushButton(self.centralwidget)
        self.CFuncionarioBTN.setGeometry(QtCore.QRect(90, 60, 120, 30))
        self.CFuncionarioBTN.setObjectName("CFuncionarioBTN")

        # Abre a janela Funcionários
        self.CFuncionarioBTN.clicked.connect(self.switchToFuncionarios)



        self.editMenuBTN = QtWidgets.QPushButton(self.centralwidget)
        self.editMenuBTN.setGeometry(QtCore.QRect(90, 100, 120, 30))
        self.editMenuBTN.setObjectName("editMenuBTN")

        # Abre a tela de login
        self.editMenuBTN.clicked.connect(self.switchToLogin)



        self.sairBTN = QtWidgets.QPushButton(self.centralwidget)
        self.sairBTN.setGeometry(QtCore.QRect(90, 150, 120, 30))
        self.sairBTN.setObjectName("sairBTN")

        # Sai da aplicação
        self.sairBTN.clicked.connect(Menu.close)





        Menu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Menu)
        self.statusbar.setObjectName("statusbar")
        Menu.setStatusBar(self.statusbar)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Menu"))
        self.CClienteBTN.setText(_translate("Menu", "Cadastrar Cliente"))
        self.sairBTN.setText(_translate("Menu", "Sair"))
        self.CFuncionarioBTN.setText(_translate("Menu", "Cadastrar Funcionário"))
        self.editMenuBTN.setText(_translate("Menu", "Editar Cardápio"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu = QtWidgets.QMainWindow()
    ui = Ui_Menu()
    ui.setupUi(Menu)
    Menu.show()
    sys.exit(app.exec_())
