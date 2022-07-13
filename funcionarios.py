from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QMessageBox, QWidget, QApplication
import mysql.connector

class Ui_Funcionarios(QWidget):

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
    mycursor.execute("CREATE TABLE IF NOT EXISTS funcionarios (id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT, nome VARCHAR(200), CPF VARCHAR(11), telefone VARCHAR(15), endereco VARCHAR(250), email VARCHAR(50), senha VARCHAR(100), setor VARCHAR(30))")
    # Encerra a conexão com o banco
    mycursor.close()
    mydb.close()



    # Variáveis que definem o tamnho máximo da entrada de cada variável
    maxNome = 200
    maxCPF = 11
    maxTelefone = 11
    maxEndereco = 250
    maxEmail = 50
    maxSenha = 100
    maxSetor = 30



    # Sinal emitido para retornar ao menu
    funcionariosToMenuSignal = pyqtSignal(name = "funcionariosToMenuSignal")

    def switchToMenu(self):
        self.funcionariosToMenuSignal.emit()





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

        idCount = "SELECT id FROM funcionarios"
        mycursor.execute(idCount)
            
        numFuncionarios = len(mycursor.fetchall())

        # Adiciona uma nova linha na tabela da interface
        self.funcionariosTable.setRowCount(numFuncionarios)


        # Lendo os dados e colocando dentro da tabela

        item = QtWidgets.QTableWidgetItem

        # Adicionando os nomes
        mycursor.execute("SELECT nome FROM funcionarios")
        nomes = mycursor.fetchall()
        quantidade = int(len(nomes))

        if(quantidade == 0):
            self.funcionariosTable.setItem(0, 0, item(''))
        else:
            for i in range(0, quantidade):
                nome = nomes[i]
                self.funcionariosTable.setItem(i, 0, item(str(nome[0])))
        


        # Adicionando os CPF's
        mycursor.execute("SELECT CPF FROM funcionarios")
        cpfs = mycursor.fetchall()
        quantidade = int(len(cpfs))

        if(quantidade == 0):
            self.funcionariosTable.setItem(0, 1, item(''))
        else:
            for i in range(0, quantidade):
                cpf = cpfs[i]
                self.funcionariosTable.setItem(i, 1, item(str(cpf[0])))



        # Adicionando os telefones
        mycursor.execute("SELECT telefone FROM funcionarios")
        telefones = mycursor.fetchall()
        quantidade = int(len(telefones))

        if(quantidade == 0):
            self.funcionariosTable.setItem(0, 2, item(''))
        else:
            for i in range(0, quantidade):
                telefone = telefones[i]
                self.funcionariosTable.setItem(i, 2, item(str(telefone[0])))



        # Adicionando os enderecos
        mycursor.execute("SELECT endereco FROM funcionarios")
        enderecos = mycursor.fetchall()
        quantidade = int(len(enderecos))

        if(quantidade == 0):
            self.funcionariosTable.setItem(0, 3, item(''))
        else:
            for i in range(0, quantidade):
                endereco = enderecos[i]
                self.funcionariosTable.setItem(i, 3, item(str(endereco[0])))
        


        # Adicionando os emails
        mycursor.execute("SELECT email FROM funcionarios")
        emails = mycursor.fetchall()
        quantidade = int(len(enderecos))

        if(quantidade == 0):
            self.funcionariosTable.setItem(0, 4, item(''))
        else:
            for i in range(0, quantidade):
                email = emails[i]
                self.funcionariosTable.setItem(i, 4, item(str(email[0])))
        


        # Adicionando as senhas
        mycursor.execute("SELECT senha FROM funcionarios")
        senhas = mycursor.fetchall()
        quantidade = int(len(enderecos))

        if(quantidade == 0):
            self.funcionariosTable.setItem(0, 5, item(''))
        else:
            for i in range(0, quantidade):
                senha = senhas[i]
                self.funcionariosTable.setItem(i, 5, item(str(senha[0])))


    
        # Adicionando os setores
        mycursor.execute("SELECT setor FROM funcionarios")
        setores = mycursor.fetchall()
        quantidade = int(len(enderecos))

        if(quantidade == 0):
            self.funcionariosTable.setItem(0, 6, item(''))
        else:
            for i in range(0, quantidade):
                setor = setores[i]
                self.funcionariosTable.setItem(i, 6, item(str(setor[0])))

        mydb.commit()

        # Encerrando a conexão com o banco
        mycursor.close()
        mydb.close()





    def cadastro(self):
        nome = self.nomeTB.text()
        CPF = self.cpfTB.text()
        telefone = self.telefoneTB.text()
        endereco = self.enderecoTB.text()
        email = self.emailTB.text()
        senha = self.senhaTB.text()
        setor = self.setorTB.text()


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

        
        elif(email == ''):
            self.emailVazioMSG()
        elif(len(email) > self.maxEmail):
            self.emailGrandeMSG()
        elif(self.checaEmail(email) == 0):
            self.emailInvalidoMSG()

        
        elif(senha == ''):
            self.senhaVazioMSG()
        elif(len(senha) > self.maxSenha):
            self.senhaGrandeMSG()

        
        elif(setor == ''):
            self.setorVazioMSG()
        elif(len(email) > self.maxSetor):
            self.setorGrandeMSG()


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

            emailComposto = email + self.emailCB.currentText()

            cadastra = "INSERT INTO funcionarios (nome, CPF, telefone, endereco, email, senha, setor) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            dados = (nome, CPF, telefone, endereco, emailComposto, senha, setor)
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

        procura = "SELECT nome, CPF FROM funcionarios WHERE CPF = %s"
        dado = (CPF,)
        mycursor.execute(procura, dado)
        funcionario = mycursor.fetchall()
        # Encerrando a conexão com o banco
        mycursor.close()
        mydb.close()
        if(funcionario ==  []):
            return 0
        else: 
            return funcionario





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

            funcionario = self.procuraCPF(CPF)

            if(funcionario != 0):
                ans = self.confirmaExcluirMSG(funcionario)
                if(ans == 1):
                    exclui = "DELETE FROM funcionarios WHERE CPF = %s"
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
        email = self.emailTB.text()
        setor = self.setorTB.text()
        senha = self.senhaTB.text()


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

        
        elif(email == ''):
            self.emailVazioMSG()
        elif(len(email) > self.maxEmail):
            self.emailGrandeMSG()
        elif(self.checaEmail(email) == 0):
            self.emailInvalidoMSG()
        

        elif(senha == ''):
            self.senhaVazioMSG()
        elif(len(senha) > self.maxSenha):
            self.senhaGrandeMSG()

        
        elif(setor == ''):
            self.setorVazioMSG()
        elif(len(setor) > self.maxSetor):
            self.setorGrandeMSG()

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


            emailComposto = email + self.emailCB.currentText()

            funcionario = self.procuraCPF(CPF)

            if(funcionario != 0):
                ans = self.confirmaAtualizarMSG(funcionario)
                if(ans == 1):
                    update = "UPDATE funcionarios SET nome = %s, CPF = %s, telefone = %s, endereco = %s, email = %s, senha = %s, setor = %s WHERE CPF = %s"
                    dados = (nome, CPF, telefone, endereco, emailComposto, senha, setor, CPF)
                    mycursor.execute(update, dados)
                    mydb.commit()
                    self.atualizadoComSucessoMSG()
            else:
                self.cpfInexistenteMSG()
            
            # Encerrando a conexão com o banco
                mycursor.close()
                mydb.close()

            # Mostra na tabela os dados que foram cadastrados
            self.preencheTabela()
            





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

            funcionario = self.procuraCPF(CPF)

            if(funcionario != 0):
                procura = "SELECT nome, CPF, telefone, endereco, email, senha, setor FROM funcionarios WHERE CPF = %s"
                dados = (CPF,)
                mycursor.execute(procura, dados)

                funcionario = mycursor.fetchall()
                
                # Arrumando o email para colocar na caixa
                finalEmail = ''
                comecoEmail = ''
                # Pega a parte inicial do email antes do @
                for x in funcionario[0][4]:
                    if(x == '@'):
                        break
                    comecoEmail = str(comecoEmail) + str(x)



                # Isola a parte final do email
                aux = str(funcionario[0][4]) 
                if comecoEmail in aux:
                    finalEmail = aux.replace(comecoEmail, "")

                

                # Arrumando o index da combo box baseado na terminação do email
                numberOfIndex = self.emailCB.count()
                for x in range (0, numberOfIndex):
                    if(str(finalEmail) == self.emailCB.itemText(x)):
                       self.emailCB.setCurrentIndex(x)
                


                # Setando as caixas de texto com as informações do cadastro encontrado
                self.nomeTB.setText(str(funcionario[0][0]))
                self.cpfTB.setText(str(funcionario[0][1]))
                self.telefoneTB.setText(str(funcionario[0][2]))
                self.enderecoTB.setText(str(funcionario[0][3]))
                self.emailTB.setText(str(comecoEmail))
                self.senhaTB.setText(str(funcionario[0][5]))
                self.setorTB.setText(str(funcionario[0][6]))

                # Encerrando a conexão com o banco
                mycursor.close()
                mydb.close()
                self.encontradoComSucessoMSG()
            else:
                self.cpfInexistenteMSG()

            # Mostra na tabela os dados que foram cadastrados
            self.preencheTabela()



    def checaEmail(self, email):
        for x in email:
            if(x == ' ' or x == '@' or x == '~' or x == '^' or x == '`' or x == '´' or x == '[' or x == ']' or x == '{' or x == '}' or x == '(' or x == ')' or x == '$'):
                return 0
        return 1




    def setupUi(self, Funcionarios):

        Funcionarios.setObjectName("Funcionarios")
        Funcionarios.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(Funcionarios)
        self.centralwidget.setObjectName("centralwidget")





# Labels


        self.funcionariosLabel = QtWidgets.QLabel(self.centralwidget)
        self.funcionariosLabel.setGeometry(QtCore.QRect(50, 10, 130, 30))
        self.funcionariosLabel.setObjectName("funcionariosLabel")
        


        self.nomeLabel = QtWidgets.QLabel(self.centralwidget)
        self.nomeLabel.setGeometry(QtCore.QRect(100, 240, 30, 30))
        self.nomeLabel.setObjectName("nomeLabel")



        self.cpfLabel = QtWidgets.QLabel(self.centralwidget)
        self.cpfLabel.setGeometry(QtCore.QRect(100, 280, 30, 30))
        self.cpfLabel.setObjectName("cpfLabel")



        self.telefoneLabel = QtWidgets.QLabel(self.centralwidget)
        self.telefoneLabel.setGeometry(QtCore.QRect(100, 320, 50, 30))
        self.telefoneLabel.setObjectName("telefoneLabel")



        self.enderecoLabel = QtWidgets.QLabel(self.centralwidget)
        self.enderecoLabel.setGeometry(QtCore.QRect(100, 360, 50, 30))
        self.enderecoLabel.setObjectName("enderecoLabel")



        self.emailLabel = QtWidgets.QLabel(self.centralwidget)
        self.emailLabel.setGeometry(QtCore.QRect(100, 400, 50, 30))
        self.emailLabel.setObjectName("emailLabel")



        self.senhaLabel = QtWidgets.QLabel(self.centralwidget)
        self.senhaLabel.setGeometry(QtCore.QRect(100, 440, 50, 30))
        self.senhaLabel.setObjectName("senhaLabel")



        self.setorLabel = QtWidgets.QLabel(self.centralwidget)
        self.setorLabel.setGeometry(QtCore.QRect(100, 480, 50, 30))
        self.setorLabel.setObjectName("setorLabel")



# Table

        self.funcionariosTable = QtWidgets.QTableWidget(self.centralwidget)
        self.funcionariosTable.setGeometry(QtCore.QRect(40, 40, 520, 120))
        self.funcionariosTable.setObjectName("funcionariosTable")

        # Seta o número de colunas da tabela
        self.funcionariosTable.setColumnCount(7)

        # Seta o nome das colunas da tabela
        item = QtWidgets.QTableWidgetItem()
        self.funcionariosTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.funcionariosTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.funcionariosTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.funcionariosTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.funcionariosTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.funcionariosTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.funcionariosTable.setHorizontalHeaderItem(6, item)



        item = self.funcionariosTable.horizontalHeaderItem(0)
        item.setText("Nome")
        item = self.funcionariosTable.horizontalHeaderItem(1)
        item.setText("CPF")
        item = self.funcionariosTable.horizontalHeaderItem(2)
        item.setText("Telefone")
        item = self.funcionariosTable.horizontalHeaderItem(3)
        item.setText("Endereço")
        item = self.funcionariosTable.horizontalHeaderItem(4)
        item.setText("E-mail")
        item = self.funcionariosTable.horizontalHeaderItem(5)
        item.setText("Senha")
        item = self.funcionariosTable.horizontalHeaderItem(6)
        item.setText("Número do Setor")

        # Seta o número de linhas da tabela
        self.funcionariosTable.setRowCount(1)



# Text Boxes
        

        self.nomeTB = QtWidgets.QLineEdit(self.centralwidget)
        self.nomeTB.setGeometry(QtCore.QRect(190, 240, 251, 30))
        self.nomeTB.setObjectName("nomeTB")



        self.cpfTB = QtWidgets.QLineEdit(self.centralwidget)
        self.cpfTB.setGeometry(QtCore.QRect(190, 280, 251, 30))
        self.cpfTB.setObjectName("cpfTB")



        self.telefoneTB = QtWidgets.QLineEdit(self.centralwidget)
        self.telefoneTB.setGeometry(QtCore.QRect(190, 320, 251, 30))
        self.telefoneTB.setObjectName("telefoneTB")

      
        
        self.enderecoTB = QtWidgets.QLineEdit(self.centralwidget)
        self.enderecoTB.setGeometry(QtCore.QRect(190, 360, 251, 30))
        self.enderecoTB.setObjectName("enderecoTB")



        self.emailTB = QtWidgets.QLineEdit(self.centralwidget)
        self.emailTB.setGeometry(QtCore.QRect(190, 400, 150, 30))
        self.emailTB.setObjectName("emailTB")



        self.senhaTB = QtWidgets.QLineEdit(self.centralwidget)
        self.senhaTB.setGeometry(QtCore.QRect(190, 440, 251, 30))
        self.senhaTB.setObjectName("senhaTB")



        self.setorTB = QtWidgets.QLineEdit(self.centralwidget)
        self.setorTB.setGeometry(QtCore.QRect(190, 480, 251, 30))
        self.setorTB.setObjectName("setorTB")



# Combo boxes

        self.emailCB = QtWidgets.QComboBox(self.centralwidget)
        self.emailCB.setGeometry(QtCore.QRect(340, 400, 100, 30))
        self.emailCB.setObjectName("emailCB1")

        # Adicionando as opções de @
        self.emailCB.addItem("@gmail.com")
        self.emailCB.addItem("@hotmail.com")
        self.emailCB.addItem("@outlook.com")
        self.emailCB.addItem("@yahoo.com")



# Buttons


        self.cadastrarBTN = QtWidgets.QPushButton(self.centralwidget)
        self.cadastrarBTN.setGeometry(QtCore.QRect(40, 180, 100, 30))
        self.cadastrarBTN.setObjectName("cadastrarBTN")

        # Ativa a função cadastrar
        self.cadastrarBTN.clicked.connect(self.cadastro)



        self.atualizarBTN = QtWidgets.QPushButton(self.centralwidget)
        self.atualizarBTN.setGeometry(QtCore.QRect(320, 180, 100, 30))
        self.atualizarBTN.setObjectName("atualizarBTN")

        # Ativa a função atualizar
        self.atualizarBTN.clicked.connect(self.atualiza)



        self.excluirBTN = QtWidgets.QPushButton(self.centralwidget)
        self.excluirBTN.setGeometry(QtCore.QRect(460, 180, 100, 30))
        self.excluirBTN.setObjectName("excluirBTN")

        # Ativa a função excluir
        self.excluirBTN.clicked.connect(self.exclui)



        self.procurarBTN = QtWidgets.QPushButton(self.centralwidget)
        self.procurarBTN.setGeometry(QtCore.QRect(180, 180, 100, 30))
        self.procurarBTN.setObjectName("procurarBTN")

        # Ativa a função procurar
        self.procurarBTN.clicked.connect(self.procura)



        self.voltarBTN = QtWidgets.QPushButton(self.centralwidget)
        self.voltarBTN.setGeometry(QtCore.QRect(250, 540, 100, 30))
        self.voltarBTN.setObjectName("voltarBTN")

        # Volta para o menu
        self.voltarBTN.clicked.connect(self.funcionariosToMenuSignal)





        Funcionarios.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Funcionarios)
        self.statusbar.setObjectName("statusbar")
        Funcionarios.setStatusBar(self.statusbar)

        self.retranslateUi(Funcionarios)
        QtCore.QMetaObject.connectSlotsByName(Funcionarios)

    def retranslateUi(self, Funcionarios):
        _translate = QtCore.QCoreApplication.translate
        Funcionarios.setWindowTitle(_translate("Funcionarios", "Cadastrar Funcionários"))
        self.funcionariosLabel.setText(_translate("Funcionarios", "Funcionários Cadastrados:"))
        self.nomeLabel.setText(_translate("Funcionarios", "Nome:"))
        self.cpfLabel.setText(_translate("Funcionarios", "CPF:"))
        self.telefoneLabel.setText(_translate("Funcionarios", "Telefone:"))
        self.emailLabel.setText(_translate("Funcionarios", "Email:"))
        self.setorLabel.setText(_translate("Funcionarios", "Setor:"))
        self.senhaLabel.setText(_translate("Funcionarios", "Senha:"))
        self.cadastrarBTN.setText(_translate("Funcionarios", "Cadastrar"))
        self.enderecoLabel.setText(_translate("Funcionarios", "Endereço:"))
        self.atualizarBTN.setText(_translate("Funcionarios", "Atualizar"))
        self.excluirBTN.setText(_translate("Funcionarios", "Excluir"))
        self.procurarBTN.setText(_translate("Funcionarios", "Procurar"))
        self.voltarBTN.setText(_translate("Funcionarios", "Voltar"))





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



    def emailVazioMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Email vazio!")
        msg.setText("Por favor, entre com o email!")

        msg.exec_() 
    


    def senhaVazioMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Senha vazia!")
        msg.setText("Por favor, entre com a senha!")

        msg.exec_()



    def setorVazioMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Setor vazio!")
        msg.setText("Por favor, entre com o setor!")

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

    

    def emailGrandeMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Entrada de email inválida!")
        msg.setText("O email que está tentando inserir ultrapassa o limite de 50 caracteres!")

        msg.exec_()



    def senhaGrandeMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Entrada de senha inválida!")
        msg.setText("A senha que está tentando inserir ultrapassa o limite de 100 caracteres!")

        msg.exec_()



    def setorGrandeMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Entrada de setor inválida!")
        msg.setText("O setor que está tentando inserir ultrapassa o limite de 30 caracteres!")

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

    

    def emailInvalidoMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Email inválido!")
        msg.setText("O email informado contém caracteres inválidos!")

        msg.exec_()


    # Caixas de confirmação de ações

    def confirmaExcluirMSG(self, funcionario):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Pedido de confirmação!")
        msg.setText("Deseja realmente excluir o cadastro do funcionario " + str(funcionario[0][0]) + " de CPF " + str(funcionario[0][1]) + "?")

        msg.setStandardButtons(QMessageBox.Yes| QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)

        reply = msg.exec_()

        if(reply == QMessageBox.Yes):
            return 1
        else:
            return 0
    


    def confirmaAtualizarMSG(self, funcionario):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Pedido de confirmação!")
        msg.setText("Deseja realmente atualizar o cadastro do funcionario " + str(funcionario[0][0]) + " de CPF " + str(funcionario[0][1]) + "?")

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
        msg.setText("O funcionario foi cadastrado com sucesso!")

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
        msg.setText("O funcionario foi encontrado com sucesso!")

        msg.exec_()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Funcionarios = QtWidgets.QMainWindow()
    ui = Ui_Funcionarios()
    ui.setupUi(Funcionarios)
    Funcionarios.show()
    sys.exit(app.exec_())
