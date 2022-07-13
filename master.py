import sys, math
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QMessageBox, QWidget, QApplication

# Local Imports
from menu import Ui_Menu
from clientes import Ui_Clientes
from funcionarios import Ui_Funcionarios
from editarmenu import Ui_EditarMenu
from login import Ui_Login
from edithamburguer import Ui_Hamburguers



class Controller(object):

    def __init__(self):
        self.WindowConfig = QtWidgets.QMainWindow()

    def MenuWindow(self):
        self.Menu = Ui_Menu()
        self.Menu.setupUi(self.WindowConfig)
        self.Menu.menuToClientesSignal.connect(self.ClientesWindow)
        self.Menu.menuToFuncionariosSignal.connect(self.FuncionariosWindow)
        self.Menu.menuToLoginSignal.connect(self.LoginWindow)
        self.WindowConfig.show()

    def LoginWindow(self):
        self.login = Ui_Login()
        self.login.setupUi(self.WindowConfig)
        self.login.loginToMenuSignal.connect(self.MenuWindow)
        self.login.loginToEditMenuSignal.connect(self.EditarMenuWindow)
        self.WindowConfig.show()

    def EditarMenuWindow(self):
        self.editMenu = Ui_EditarMenu()
        self.editMenu.setupUi(self.WindowConfig)
        self.editMenu.editarMenuToHamburguerSignal.connect(self.EditHamburguerWindow)
        #self.editMenu.editarMenuToPizzaSignal.connect(self.EditPizzaWindow)
        self.editMenu.editarMenuToMenuSignal.connect(self.MenuWindow)
        self.WindowConfig.show()

    def EditHamburguerWindow(self):
        self.clientes = Ui_Hamburguers()
        self.clientes.setupUi(self.WindowConfig)
        self.clientes.preencheTabela()
        self.clientes.hamburguersToEditMenuSignal.connect(self.EditarMenuWindow)
        self.WindowConfig.show()

    #def EditPizzaWindow(self):
    #    self.clientes = Ui_Clientes()
    #    self.clientes.setupUi(self.WindowConfig)
    #    self.clientes.preencheTabela()
    #    self.clientes.clientesToMenuSignal.connect(self.MenuWindow)
    #    self.WindowConfig.show()

    def ClientesWindow(self):
        self.clientes = Ui_Clientes()
        self.clientes.setupUi(self.WindowConfig)
        self.clientes.preencheTabela()
        self.clientes.clientesToMenuSignal.connect(self.MenuWindow)
        self.WindowConfig.show()

    def FuncionariosWindow(self):
        self.funcionarios = Ui_Funcionarios()
        self.funcionarios.setupUi(self.WindowConfig)
        self.funcionarios.preencheTabela()
        self.funcionarios.funcionariosToMenuSignal.connect(self.MenuWindow)
        self.WindowConfig.show()
    

def main():
    app = QApplication(sys.argv)
    controller = Controller()
    controller.MenuWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()