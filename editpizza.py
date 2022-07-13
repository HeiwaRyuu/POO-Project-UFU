from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QMessageBox, QWidget, QApplication
import mysql.connector




class Ui_Clientes(QWidget):

    # Conecta ao banco de dados
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "35c4p3fromh3ll",
    database = "trabalhoPOO"
    )

    # Cria o banco e a tabela caso não existam
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS trabalhoPOO")
    mycursor.execute("CREATE TABLE IF NOT EXISTS pizza (id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT, nome VARCHAR(50), principal VARCHAR(50), queijo VARCHAR(50), cebola VARCHAR(50), ovo VARCHAR(50), milho VARCHAR(50), tomate VARCHAR(50), azeitona VARCHAR(50), borda VARCHAR(50))")
    mydb.commit()
    # Encerra a conexão com o banco
    mycursor.close()
    mydb.close()



    # Variáveis que definem o tamnho máximo da entrada de cada variável
    maxNome = 200
    maxCPF = 11
    maxTelefone = 11
    maxEndereco = 250



    # Sinal emitido para retornar ao menu
    clientesToMenuSignal = pyqtSignal(name = "clientesToMenuSignal")

    def switchToMenu(self):
        self.clientesToMenuSignal.emit()





    # Definição de funções de tratamento de erros

    def isInt(self, numero):
        try:
            int(numero)
            return 1
        except:
            return 0



    def isString(self, nome):
        aux = 1
        for x in nome:
            try:
                int(x)
                aux = 0
            except:
                pass
        return aux      



    def existeCPF(self, CPF):
        if(self.procuraCPF(CPF) != 0):
            return 1
        else:
            return 0

        




    # Definição das funções que envolvem o CRUD no banco

    def preencheTabela(self):
        # Conecta ao banco de dados
        mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "35c4p3fromh3ll",
        database = "trabalhoPOO"
        )
        mycursor = mydb.cursor()

        idCount = "SELECT id FROM clientes"
        mycursor.execute(idCount)
            
        numClientes = len(mycursor.fetchall())

        # Adiciona uma nova linha na tabela da interface
        self.clientesTable.setRowCount(numClientes)

        # Lendo os dados e colocando dentro da tabela

        item = QtWidgets.QTableWidgetItem

        # Adicionando os nomes
        mycursor.execute("SELECT nome FROM clientes")
        nomes = mycursor.fetchall()
        quantidade = int(len(nomes))

        if(quantidade == 0):
            self.clientesTable.setItem(0, 0, item(''))
        else:
            for i in range(0, quantidade):
                nome = nomes[i]
                self.clientesTable.setItem(i, 0, item(str(nome[0])))
        


        # Adicionando os CPF's
        mycursor.execute("SELECT CPF FROM clientes")
        cpfs = mycursor.fetchall()
        quantidade = int(len(cpfs))

        if(quantidade == 0):
            self.clientesTable.setItem(0, 1, item(''))
        else:
            for i in range(0, quantidade):
                cpf = cpfs[i]
                self.clientesTable.setItem(i, 1, item(str(cpf[0])))



        # Adicionando os telefones
        mycursor.execute("SELECT telefone FROM clientes")
        telefones = mycursor.fetchall()
        quantidade = int(len(telefones))

        if(quantidade == 0):
            self.clientesTable.setItem(0, 2, item(''))
        else:
            for i in range(0, quantidade):
                telefone = telefones[i]
                self.clientesTable.setItem(i, 2, item(str(telefone[0])))



        # Adicionando os enderecos
        mycursor.execute("SELECT endereco FROM clientes")
        enderecos = mycursor.fetchall()
        quantidade = int(len(enderecos))

        if(quantidade == 0):
            self.clientesTable.setItem(0, 3, item(''))
        else:
            for i in range(0, quantidade):
                endereco = enderecos[i]
                self.clientesTable.setItem(i, 3, item(str(endereco[0])))

        mydb.commit()

        # Encerrando a conexão com o banco
        mycursor.close()
        mydb.close()





    def cadastro(self):
        nome = self.nomeTB.text()
        CPF = self.cpfTB.text()
        telefone = self.telefoneTB.text()
        endereco = self.enderecoTB.text()


        if(nome == ''):
            self.nomeVazioMSG()
        elif(self.isString(nome) != 1):
            self.naoStringMSG()
        elif(len(nome) > self.maxNome):
            self.nomeGrandeMSG()


        elif(CPF == ''):
            self.cpfVazioMSG()
        elif(self.isInt(CPF) != 1):
            self.naoNumeroCPFMSG()
        elif(len(CPF) != self.maxCPF):
            self.cpfInvalidoMSG()
        elif(self.existeCPF(CPF) == 1):
            self.cpfJaCadastradoMSG()


        elif(telefone == ''):
            self.telefoneVazioMSG()
        elif(self.isInt(telefone) != 1):
            self.naoNumeroTelefoneMSG()
        elif(len(telefone) != self.maxTelefone):
            self.telefoneInvalidoMSG()


        elif(endereco == ''):
            self.enderecoVazioMSG()
        elif(len(endereco) > self.maxEndereco):
            self.enderecoGrandeMSG()

        # Caso passe em todos os tratamentos de excessão, será adicionado ao banco
        else:
            # Conecta ao banco de dados
            mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "35c4p3fromh3ll",
            database = "trabalhoPOO"
            )
            mycursor = mydb.cursor()


            cadastra = "INSERT INTO clientes (nome, CPF, telefone, endereco) VALUES (%s, %s, %s, %s)"
            dados = (nome, CPF, telefone, endereco)
            mycursor.execute(cadastra, dados)
            mydb.commit()


            # Encerrando a conexão com o banco
            mycursor.close()
            mydb.close()

            

            # Mostra na tabela os dados que foram cadastrados
            self.preencheTabela()
            self.cadastroConcluidoMSG()





    def procuraCPF(self, CPF):
        # Conecta ao banco de dados
            mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "35c4p3fromh3ll",
            database = "trabalhoPOO"
            )
            mycursor = mydb.cursor()

            procura = "SELECT nome, CPF FROM clientes WHERE CPF = %s"
            dado = (CPF,)
            mycursor.execute(procura, dado)
            cliente = mycursor.fetchall()
            # Encerrando a conexão com o banco
            mycursor.close()
            mydb.close()
            if(cliente ==  []):
                return 0
            else: 
                return cliente





    def exclui(self):
        CPF = self.cpfTB.text()

        if(CPF == ''):
            self.cpfVazioMSG()
        elif(self.isInt(CPF) != 1):
            self.naoNumeroCPFMSG()
        else:
            # Conecta ao banco de dados
            mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "35c4p3fromh3ll",
            database = "trabalhoPOO"
            )
            mycursor = mydb.cursor()

            cliente = self.procuraCPF(CPF)

            if(cliente != 0):
                ans = self.confirmaExcluirMSG(cliente)
                if(ans == 1):
                    exclui = "DELETE FROM clientes WHERE CPF = %s"
                    dados = (CPF,)
                    mycursor.execute(exclui, dados)
                    mydb.commit()

                    self.excluidoComSucessoMSG()
            else:
                self.cpfInexistenteMSG()

            # Encerrando a conexão com o banco
                mycursor.close()
                mydb.close()

            # Mostra na tabela os dados que foram cadastrados
            self.preencheTabela()
            

 



    def atualiza(self):
        nome = self.nomeTB.text()
        CPF = self.cpfTB.text()
        telefone = self.telefoneTB.text()
        endereco = self.enderecoTB.text()


        if(nome == ''):
            self.nomeVazioMSG()
        elif(self.isString(nome) != 1):
            self.naoStringMSG()
        elif(len(nome) > self.maxNome):
            self.nomeGrandeMSG()


        elif(CPF == ''):
            self.cpfVazioMSG()
        elif(self.isInt(CPF) != 1):
            self.naoNumeroCPFMSG()
        elif(len(CPF) != self.maxCPF):
            self.cpfInvalidoMSG()



        elif(telefone == ''):
            self.telefoneVazioMSG()
        elif(self.isInt(telefone) != 1):
            self.naoNumeroTelefoneMSG()
        elif(len(telefone) != self.maxTelefone):
            self.telefoneInvalidoMSG()


        elif(endereco == ''):
            self.enderecoVazioMSG()
        elif(len(endereco) > self.maxEndereco):
            self.enderecoGrandeMSG()

        # Caso passe em todos os tratamentos de excessão, será feito o update
        else:
            # Conecta ao banco de dados
            mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "35c4p3fromh3ll",
            database = "trabalhoPOO"
            )
            mycursor = mydb.cursor()

            cliente = self.procuraCPF(CPF)

            if(cliente != 0):
                ans = self.confirmaAtualizarMSG(cliente)
                if(ans == 1):
                    update = "UPDATE clientes SET nome = %s, CPF = %s, telefone = %s, endereco = %s WHERE CPF = %s"
                    dados = (nome, CPF, telefone, endereco, CPF)
                    mycursor.execute(update, dados)
                    mydb.commit()
            else:
                self.cpfInexistenteMSG()
            
            # Encerrando a conexão com o banco
                mycursor.close()
                mydb.close()

            # Mostra na tabela os dados que foram cadastrados
            self.preencheTabela()
            self.atualizadoComSucessoMSG()





    def procura(self):
        CPF = self.cpfTB.text()

        if(CPF == ''):
            self.cpfVazioMSG()
        elif(self.isInt(CPF) != 1):
            self.naoNumeroCPFMSG()
        else:
            # Conecta ao banco de dados
            mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "35c4p3fromh3ll",
            database = "trabalhoPOO"
            )
            mycursor = mydb.cursor()

            cliente = self.procuraCPF(CPF)

            if(cliente != 0):
                procura = "SELECT nome, CPF, telefone, endereco FROM clientes WHERE CPF = %s"
                dados = (CPF,)
                mycursor.execute(procura, dados)

                cliente = mycursor.fetchall()

                # Setando as caixas de texto com as informações do cadastro encontrado
                self.nomeTB.setText(str(cliente[0][0]))
                self.cpfTB.setText(str(cliente[0][1]))
                self.telefoneTB.setText(str(cliente[0][2]))
                self.enderecoTB.setText(str(cliente[0][3]))


                self.encontradoComSucessoMSG()
            else:
                self.cpfInexistenteMSG()

            # Mostra na tabela os dados que foram cadastrados
            self.preencheTabela()
            
            # Encerra a conexão com o banco
            mycursor.close()
            mydb.close()
        



    def setupUi(self, Clientes):

        Clientes.setObjectName("Clientes")
        Clientes.resize(500, 550)
        self.centralwidget = QtWidgets.QWidget(Clientes)
        self.centralwidget.setObjectName("centralwidget")





# Labels 


        self.clientesLabel = QtWidgets.QLabel(self.centralwidget)
        self.clientesLabel.setGeometry(QtCore.QRect(50, 10, 120, 30))
        self.clientesLabel.setObjectName("clientesLabel")



        self.nomeLabel = QtWidgets.QLabel(self.centralwidget)
        self.nomeLabel.setGeometry(QtCore.QRect(75, 240, 50, 30))
        self.nomeLabel.setObjectName("nomeLabel")



        self.cpfLabel = QtWidgets.QLabel(self.centralwidget)
        self.cpfLabel.setGeometry(QtCore.QRect(75, 280, 50, 30))
        self.cpfLabel.setObjectName("cpfLabel")



        self.telefoneLabel = QtWidgets.QLabel(self.centralwidget)
        self.telefoneLabel.setGeometry(QtCore.QRect(75, 320, 50, 30))
        self.telefoneLabel.setObjectName("telefoneLabel")



        self.enderecoLabel = QtWidgets.QLabel(self.centralwidget)
        self.enderecoLabel.setGeometry(QtCore.QRect(75, 360, 50, 30))
        self.enderecoLabel.setObjectName("enderecoLabel")





# Table

        self.clientesTable = QtWidgets.QTableWidget(self.centralwidget)
        self.clientesTable.setGeometry(QtCore.QRect(40, 40, 420, 120))
        self.clientesTable.setObjectName("clientesTable")
        
        # Seta o número de colunas da tabela
        self.clientesTable.setColumnCount(4)

        # Seta o nome das colunas da tabela
        item = QtWidgets.QTableWidgetItem()
        self.clientesTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.clientesTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.clientesTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.clientesTable.setHorizontalHeaderItem(3, item)



        item = self.clientesTable.horizontalHeaderItem(0)
        item.setText("Nome")
        item = self.clientesTable.horizontalHeaderItem(1)
        item.setText("CPF")
        item = self.clientesTable.horizontalHeaderItem(2)
        item.setText("Telefone")
        item = self.clientesTable.horizontalHeaderItem(3)
        item.setText("Endereço")

        # Seta o número de linhas da tabela
        self.clientesTable.setRowCount(1)



# Text Boxes


        self.nomeTB = QtWidgets.QLineEdit(self.centralwidget)
        self.nomeTB.setGeometry(QtCore.QRect(165, 240, 250, 30))
        self.nomeTB.setObjectName("nomeTB")



        self.cpfTB = QtWidgets.QLineEdit(self.centralwidget)
        self.cpfTB.setGeometry(QtCore.QRect(165, 280, 250, 30))
        self.cpfTB.setObjectName("cpfTB")



        self.telefoneTB = QtWidgets.QLineEdit(self.centralwidget)
        self.telefoneTB.setGeometry(QtCore.QRect(165, 320, 250, 30))
        self.telefoneTB.setObjectName("telefoneTB")



        self.enderecoTB = QtWidgets.QLineEdit(self.centralwidget)
        self.enderecoTB.setGeometry(QtCore.QRect(165, 360, 250, 30))
        self.enderecoTB.setObjectName("enderecoTB")



# Buttons


        self.cadastrarBTN = QtWidgets.QPushButton(self.centralwidget)
        self.cadastrarBTN.setGeometry(QtCore.QRect(40, 180, 75, 30))
        self.cadastrarBTN.setObjectName("cadastrarBTN")

        # Ativa a função cadastrar
        self.cadastrarBTN.clicked.connect(self.cadastro)



        self.atualizarBTN = QtWidgets.QPushButton(self.centralwidget)
        self.atualizarBTN.setGeometry(QtCore.QRect(270, 180, 75, 30))
        self.atualizarBTN.setObjectName("atualizarBTN")

        # Ativa a função atualizar
        self.atualizarBTN.clicked.connect(self.atualiza)



        self.excluirBTN = QtWidgets.QPushButton(self.centralwidget)
        self.excluirBTN.setGeometry(QtCore.QRect(385, 180, 75, 30))
        self.excluirBTN.setObjectName("excluirBTN")

        # Ativa a função excluir
        self.excluirBTN.clicked.connect(self.exclui)



        self.procurarBTN = QtWidgets.QPushButton(self.centralwidget)
        self.procurarBTN.setGeometry(QtCore.QRect(155, 180, 75, 30))
        self.procurarBTN.setObjectName("procurarBTN")

        # Ativa a função procurar
        self.procurarBTN.clicked.connect(self.procura)



        self.voltarBTN = QtWidgets.QPushButton(self.centralwidget)
        self.voltarBTN.setGeometry(QtCore.QRect(200, 450, 100, 30))
        self.voltarBTN.setObjectName("voltarBTN")

        # Volta para o menu
        self.voltarBTN.clicked.connect(self.switchToMenu)





        Clientes.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Clientes)
        self.statusbar.setObjectName("statusbar")
        Clientes.setStatusBar(self.statusbar)

        self.retranslateUi(Clientes)
        QtCore.QMetaObject.connectSlotsByName(Clientes)

    def retranslateUi(self, Clientes):
        _translate = QtCore.QCoreApplication.translate
        Clientes.setWindowTitle(_translate("Clientes", "Cadastrar Clientes"))
        self.clientesLabel.setText(_translate("Clientes", "Clientes Cadastrados:"))
        self.nomeLabel.setText(_translate("Clientes", "Nome:"))
        self.cpfLabel.setText(_translate("Clientes", "CPF:"))
        self.telefoneLabel.setText(_translate("Clientes", "Telefone:"))
        self.cadastrarBTN.setText(_translate("Clientes", "Cadastrar"))
        self.enderecoLabel.setText(_translate("Clientes", "Endereço:"))
        self.atualizarBTN.setText(_translate("Clientes", "Atualizar"))
        self.excluirBTN.setText(_translate("Clientes", "Excluir"))
        self.procurarBTN.setText(_translate("Clientes", "Procurar"))
        self.voltarBTN.setText(_translate("Clientes", "Voltar"))





    # Mensagens de tratamento de excessão

    def nomeVazioMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Nome vazio!")
        msg.setText("Por favor, entre com o nome!")

        msg.exec_()



    def cpfVazioMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("CPF vazio!")
        msg.setText("Por favor, entre com o CPF!")

        msg.exec_()



    def telefoneVazioMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Telefone vazio!")
        msg.setText("Por favor, entre com o telefone!")

        msg.exec_()



    def enderecoVazioMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Endereco vazio!")
        msg.setText("Por favor, entre com o endereço!")

        msg.exec_()
    


    def naoNumeroCPFMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Entrada do CPF inválida!")
        msg.setText("Por favor, entre o CPF somente com números e sem espaços!")

        msg.exec_()

    

    def naoNumeroTelefoneMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Entrada do telefone inválida!")
        msg.setText("Por favor, entre o telefone somente com números e sem espaços!")

        msg.exec_()

    

    def naoStringMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Entrada de nome inválida!")
        msg.setText("O nome não pode pode conter números!")

        msg.exec_()



    def cpfInvalidoMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Entrada de CPF inválida!")
        msg.setText("Por favor, entre um CDP válido (11 números)!")

        msg.exec_()



    def telefoneInvalidoMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Entrada de telefone inválida!")
        msg.setText("Por favor, entre um telefone válido (11 dígitos, incluindo DDD)!")

        msg.exec_()



    def nomeGrandeMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Entrada de nome inválida!")
        msg.setText("O nome que está tentando inserir ultrapassa o limite de 200 caracteres!")

        msg.exec_()
    


    def enderecoGrandeMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Entrada de endereço inválida!")
        msg.setText("O endereço que está tentando inserir ultrapassa o limite de 250 caracteres!")

        msg.exec_()



    def cpfInexistenteMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("CPF não encontrado!")
        msg.setText("Esse CPF não está cadastrado!")

        msg.exec_() 



    def cpfJaCadastradoMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("CPF já cadastrado!")
        msg.setText("Esse CPF já está cadastrado!")

        msg.exec_()


    # Caixas de confirmação de ações

    def confirmaExcluirMSG(self, cliente):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Pedido de confirmação!")
        msg.setText("Deseja realmente excluir o cadastro do cliente " + str(cliente[0][0]) + " de CPF " + str(cliente[0][1]) + "?")

        msg.setStandardButtons(QMessageBox.Yes| QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)

        reply = msg.exec_()

        if(reply == QMessageBox.Yes):
            return 1
        else:
            return 0
    


    def confirmaAtualizarMSG(self, cliente):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Pedido de confirmação!")
        msg.setText("Deseja realmente atualizar o cadastro do cliente " + str(cliente[0][0]) + " de CPF " + str(cliente[0][1]) + "?")

        msg.setStandardButtons(QMessageBox.Yes| QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)

        reply = msg.exec_()

        if(reply == QMessageBox.Yes):
            return 1
        else:
            return 0


        
		

    
    # Mensagens de ações bem sucedidas

    def cadastroConcluidoMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Cadastro bem sucedido!")
        msg.setText("O cliente foi cadastrado com sucesso!")

        msg.exec_()
    


    def excluidoComSucessoMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Excluído com sucesso!")
        msg.setText("O cadastro foi deletado com sucesso!")

        msg.exec_()



    def atualizadoComSucessoMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Atualizado com sucesso!")
        msg.setText("Os dados foram atualizados com sucesso!")

        msg.exec_()



    def encontradoComSucessoMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Cadastro encontrado com sucesso!")
        msg.setText("O cliente foi encontrado com sucesso!")

        msg.exec_()
    





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Clientes = QtWidgets.QMainWindow()
    ui = Ui_Clientes()
    ui.setupUi(Clientes)
    Clientes.show()
    sys.exit(app.exec_())
