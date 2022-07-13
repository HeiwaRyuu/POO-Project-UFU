from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QMessageBox, QWidget, QApplication
import mysql.connector



class Ui_EditarMenu(QWidget):



    # Sinal emitido para retornar ao menu
    editarMenuToMenuSignal = pyqtSignal(name = "editarMenuToMenuSignal")
    editarMenuToHamburguerSignal = pyqtSignal(name = "editarMenuToHamburguerSignal")
    editarMenuToPizzaSignal = pyqtSignal(name = "editarMenuToPizzaSignal")

    def switchToMenu(self):
        self.editarMenuToMenuSignal.emit()

    def switchToHamburguer(self):
        self.editarMenuToHamburguerSignal.emit()

    def switchToPizza(self):
        self.editarMenuToPizzaSignal.emit()



    def setupUi(self, EditarMenu):

        EditarMenu.setObjectName("EditarMenu")
        EditarMenu.resize(300, 250)
        self.centralwidget = QtWidgets.QWidget(EditarMenu)
        self.centralwidget.setObjectName("centralwidget")


# Buttons

        self.hamburguerBTN = QtWidgets.QPushButton(self.centralwidget)
        self.hamburguerBTN.setGeometry(QtCore.QRect(70, 40, 160, 30))
        self.hamburguerBTN.setObjectName("hamburguerBTN")

        # Abre a tela de edição de hambúrguer
        self.hamburguerBTN.clicked.connect(self.switchToHamburguer)



        self.pizzaBTN = QtWidgets.QPushButton(self.centralwidget)
        self.pizzaBTN.setGeometry(QtCore.QRect(70, 90, 160, 30))
        self.pizzaBTN.setObjectName("pizzaBTN")

        # Abre a tela de edição de pizza
        self.pizzaBTN.clicked.connect(self.switchToPizza)



        self.voltarBTN = QtWidgets.QPushButton(self.centralwidget)
        self.voltarBTN.setGeometry(QtCore.QRect(70, 140, 160, 30))
        self.voltarBTN.setObjectName("voltarBTN")

        # Volta para o menu
        self.voltarBTN.clicked.connect(self.switchToMenu)





        EditarMenu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(EditarMenu)
        self.statusbar.setObjectName("statusbar")
        EditarMenu.setStatusBar(self.statusbar)

        self.retranslateUi(EditarMenu)
        QtCore.QMetaObject.connectSlotsByName(EditarMenu)

    def retranslateUi(self, EditarMenu):
        _translate = QtCore.QCoreApplication.translate
        EditarMenu.setWindowTitle(_translate("EditarMenu", "Edição do cardápio"))
        self.hamburguerBTN.setText(_translate("EditarMenu", "Editar Hambúrguers"))
        self.pizzaBTN.setText(_translate("EditarMenu", "Editar Pizzas"))
        self.voltarBTN.setText(_translate("EditarMenu", "Voltar para o menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditarMenu = QtWidgets.QMainWindow()
    ui = Ui_EditarMenu()
    ui.setupUi(EditarMenu)
    EditarMenu.show()
    sys.exit(app.exec_())
