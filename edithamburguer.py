from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QMessageBox, QWidget, QApplication
import mysql.connector




class Ui_Hamburguers(QWidget):

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
    mycursor.execute("CREATE TABLE IF NOT EXISTS hamburguer (id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT, nome VARCHAR(50), pao VARCHAR(50), carne VARCHAR(50), queijo VARCHAR(50), cebola VARCHAR(50), ovo VARCHAR(50), alface VARCHAR(50), tomate VARCHAR(50))")
    mydb.commit()
    # Encerra a conexão com o banco
    mycursor.close()
    mydb.close()


    # Variáveis que definem o tamnho máximo da entrada de cada variável
    maxNome = 200



    # Sinal emitido para retornar ao menu
    hamburguersToEditMenuSignal = pyqtSignal(name = "hamburguersToEditMenuSignal")

    def switchToEditMenu(self):
        self.hamburguersToEditMenuSignal.emit()





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

        idCount = "SELECT id FROM hamburguer"
        mycursor.execute(idCount)
            
        numHamburguers = len(mycursor.fetchall())

        # Adiciona uma nova linha na tabela da interface
        self.hamburguerTable.setRowCount(numHamburguers)

        # Lendo os dados e colocando dentro da tabela

        item = QtWidgets.QTableWidgetItem

        # Adicionando os nomes
        mycursor.execute("SELECT nome FROM hamburguer")
        nomes = mycursor.fetchall()
        quantidade = int(len(nomes))

        if(quantidade == 0):
            self.hamburguerTable.setItem(0, 0, item(''))
        else:
            for i in range(0, quantidade):
                nome = nomes[i]
                self.hamburguerTable.setItem(i, 0, item(str(nome[0])))
        


        # Adicionando os pães
        mycursor.execute("SELECT pao FROM hamburguer")
        paes = mycursor.fetchall()
        quantidade = int(len(paes))

        if(quantidade == 0):
            self.hamburguerTable.setItem(0, 1, item(''))
        else:
            for i in range(0, quantidade):
                pao = paes[i]
                self.hamburguerTable.setItem(i, 1, item(str(pao[0])))



        # Adicionando as carnes
        mycursor.execute("SELECT carne FROM hamburguer")
        carnes = mycursor.fetchall()
        quantidade = int(len(carnes))

        if(quantidade == 0):
            self.hamburguerTable.setItem(0, 2, item(''))
        else:
            for i in range(0, quantidade):
                carne = carnes[i]
                self.hamburguerTable.setItem(i, 2, item(str(carne[0])))



        # Adicionando os queijos
        mycursor.execute("SELECT queijo FROM hamburguer")
        queijos = mycursor.fetchall()
        quantidade = int(len(queijos))

        if(quantidade == 0):
            self.hamburguerTable.setItem(0, 3, item(''))
        else:
            for i in range(0, quantidade):
                queijo = queijos[i]
                self.hamburguerTable.setItem(i, 3, item(str(queijo[0])))

        mydb.commit()



        # Adicionando as cebolas
        mycursor.execute("SELECT cebola FROM hamburguer")
        cebolas = mycursor.fetchall()
        quantidade = int(len(cebolas))

        if(quantidade == 0):
            self.hamburguerTable.setItem(0, 4, item(''))
        else:
            for i in range(0, quantidade):
                cebola = cebolas[i]
                self.hamburguerTable.setItem(i, 4, item(str(cebola[0])))

        mydb.commit()



        # Adicionando os ovos
        mycursor.execute("SELECT ovo FROM hamburguer")
        ovos = mycursor.fetchall()
        quantidade = int(len(ovos))

        if(quantidade == 0):
            self.hamburguerTable.setItem(0, 5, item(''))
        else:
            for i in range(0, quantidade):
                ovo = ovos[i]
                self.hamburguerTable.setItem(i, 5, item(str(ovo[0])))

        mydb.commit()



        # Adicionando as alfaces
        mycursor.execute("SELECT alface FROM hamburguer")
        alfaces = mycursor.fetchall()
        quantidade = int(len(alfaces))

        if(quantidade == 0):
            self.hamburguerTable.setItem(0, 6, item(''))
        else:
            for i in range(0, quantidade):
                alface = alfaces[i]
                self.hamburguerTable.setItem(i, 6, item(str(alface[0])))

        mydb.commit()



        # Adicionando os tomates
        mycursor.execute("SELECT tomate FROM hamburguer")
        tomates = mycursor.fetchall()
        quantidade = int(len(tomates))

        if(quantidade == 0):
            self.hamburguerTable.setItem(0, 7, item(''))
        else:
            for i in range(0, quantidade):
                tomate = tomates[i]
                self.hamburguerTable.setItem(i, 7, item(str(tomate[0])))

        

        # Adicionando os molhos
        mycursor.execute("SELECT molho FROM hamburguer")
        molhos = mycursor.fetchall()
        quantidade = int(len(molhos))

        if(quantidade == 0):
            self.hamburguerTable.setItem(0, 8, item(''))
        else:
            for i in range(0, quantidade):
                molho = molhos[i]
                self.hamburguerTable.setItem(i, 8, item(str(molho[0])))

        mydb.commit()

        # Encerrando a conexão com o banco
        mycursor.close()
        mydb.close()





    def cadastro(self):
        nome = self.nomeTB.text()
        pao = self.paoCB.currentText()
        carne = self.carneCB.currentText()
        queijo = self.queijoCB.currentText()
        cebola = self.cebolaCB.currentText()
        ovo = self.ovoCB.currentText()
        alface = self.alfaceCB.currentText()
        tomate = self.tomateCB.currentText()
        molho = self.molhoCB.currentText()


        if(nome == ''):
            self.nomeVazioMSG()
        elif(len(nome) > self.maxNome):
            self.nomeGrandeMSG()
        elif(self.procuraNome(nome) != 0):
            self.nomeJaCadastradoMSG()

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


            cadastra = "INSERT INTO hamburguer (nome, pao, carne, queijo, cebola, ovo, alface, tomate, molho) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            dados = (nome, pao, carne, queijo, cebola, ovo, alface, tomate, molho)
            mycursor.execute(cadastra, dados)
            mydb.commit()


            # Encerrando a conexão com o banco
            mycursor.close()
            mydb.close()

            

            # Mostra na tabela os dados que foram cadastrados
            self.preencheTabela()
            self.cadastroConcluidoMSG()





    def procuraNome(self, nome):
        # Conecta ao banco de dados
            mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "35c4p3fromh3ll",
            database = "trabalhoPOO"
            )
            mycursor = mydb.cursor()

            procura = "SELECT nome FROM hamburguer WHERE nome = %s"
            dado = (nome,)
            mycursor.execute(procura, dado)
            hamburguer = mycursor.fetchall()
            # Encerrando a conexão com o banco
            mycursor.close()
            mydb.close()
            if(hamburguer ==  []):
                return 0
            else: 
                return hamburguer





    def exclui(self):
        nome = self.nomeTB.text()

        if(nome == ''):
            self.nomeVazioMSG()
        elif(len(nome) > self.maxNome):
            self.nomeGrandeMSG()
        # Caso passe em todos os tratamentos de excessão, será feito a exclusão
        else:
            # Conecta ao banco de dados
            mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "35c4p3fromh3ll",
            database = "trabalhoPOO"
            )
            mycursor = mydb.cursor()

            hamburguer = self.procuraNome(nome)

            if(hamburguer != 0):
                ans = self.confirmaExcluirMSG(hamburguer)
                if(ans == 1):
                    exclui = "DELETE FROM hamburguer WHERE nome = %s"
                    dados = (nome,)
                    mycursor.execute(exclui, dados)
                    mydb.commit()

                    self.excluidoComSucessoMSG()
            else:
                self.nomeInexistenteMSG()

            # Encerrando a conexão com o banco
                mycursor.close()
                mydb.close()

            # Mostra na tabela os dados que foram cadastrados
            self.preencheTabela()
            




    def atualiza(self):
        nome = self.nomeTB.text()
        pao = self.paoCB.currentText()
        carne = self.carneCB.currentText()
        queijo = self.queijoCB.currentText()
        cebola = self.cebolaCB.currentText()
        ovo = self.ovoCB.currentText()
        alface = self.alfaceCB.currentText()
        tomate = self.tomateCB.currentText()
        molho = self.molhoCB.currentText()


        if(nome == ''):
            self.nomeVazioMSG()
        elif(len(nome) > self.maxNome):
            self.nomeGrandeMSG()
        elif(self.procuraNome(nome) != 0):
            self.nomeJaCadastradoMSG()
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

            hamburguer = self.procuraNome(nome)

            if(hamburguer != 0):
                ans = self.confirmaAtualizarMSG(hamburguer)
                if(ans == 1):
                    update = "UPDATE hamburguer SET nome = %s, pao = %s, carne = %s, queijo = %s, cebola = %s, ovo = %s, alface = %s, tomate = %s, molho = %s WHERE nome = %s"
                    dados = (nome, pao, carne, queijo, cebola, ovo, alface, tomate, molho, nome)
                    mycursor.execute(update, dados)
                    mydb.commit()
            else:
                self.nomeInexistenteMSG()
            
            # Encerrando a conexão com o banco
                mycursor.close()
                mydb.close()

            # Mostra na tabela os dados que foram cadastrados
            self.preencheTabela()
            self.atualizadoComSucessoMSG()





    def procura(self):
        nome = self.nomeTB.text()

        if(nome == ''):
            self.nomeVazioMSG()
        else:
            # Conecta ao banco de dados
            mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "35c4p3fromh3ll",
            database = "trabalhoPOO"
            )
            mycursor = mydb.cursor()

            hamburguer = self.procuraNome(nome)

            if(hamburguer != 0):
                procura = "SELECT nome, pao, carne, queijo, cebola, ovo, alface, tomate, molho FROM hamburguer WHERE nome = %s"
                dados = (nome,)
                mycursor.execute(procura, dados)

                hamburguer = mycursor.fetchall()

                # Setando as caixas de texto com as informações do cadastro encontrado
                self.nomeTB.setText(str(hamburguer[0][0]))

                # Atualizando as combo boxes
                
                # Pao
                procuraPao = "SELECT pao FROM hamburguer WHERE nome = %s"
                dados = (nome,)
                mycursor.execute(procuraPao, dados)

                listaPao = mycursor.fetchall()
                numberOfIndex = self.paoCB.count()
                for x in range (0, numberOfIndex):
                    if(str(listaPao[0][0]) == self.paoCB.itemText(x)):
                        self.paoCB.setCurrentIndex(x)

                

                # Carne
                procuraCarne = "SELECT carne FROM hamburguer WHERE nome = %s"
                dados = (nome,)
                mycursor.execute(procuraCarne, dados)

                listaCarne = mycursor.fetchall()
                numberOfIndex = self.carneCB.count()
                for x in range (0, numberOfIndex):
                    if(str(listaCarne[0][0]) == self.carneCB.itemText(x)):
                        self.carneCB.setCurrentIndex(x)

                

                # Queijo
                procuraQueijo = "SELECT queijo FROM hamburguer WHERE nome = %s"
                dados = (nome,)
                mycursor.execute(procuraQueijo, dados)

                listaQueijo = mycursor.fetchall()
                numberOfIndex = self.queijoCB.count()
                for x in range (0, numberOfIndex):
                    if(str(listaQueijo[0][0]) == self.queijoCB.itemText(x)):
                        self.queijoCB.setCurrentIndex(x)
                


                # Cebola
                procuraCebola = "SELECT cebola FROM hamburguer WHERE nome = %s"
                dados = (nome,)
                mycursor.execute(procuraCebola, dados)

                listaCebola = mycursor.fetchall()
                numberOfIndex = self.cebolaCB.count()
                for x in range (0, numberOfIndex):
                    if(str(listaCebola[0][0]) == self.cebolaCB.itemText(x)):
                        self.cebolaCB.setCurrentIndex(x)
                


                # Ovo
                procuraOvo = "SELECT ovo FROM hamburguer WHERE nome = %s"
                dados = (nome,)
                mycursor.execute(procuraOvo, dados)

                listaOvo = mycursor.fetchall()
                numberOfIndex = self.ovoCB.count()
                for x in range (0, numberOfIndex):
                    if(str(listaOvo[0][0]) == self.ovoCB.itemText(x)):
                        self.ovoCB.setCurrentIndex(x)

                

                # Alface
                procuraAlface = "SELECT alface FROM hamburguer WHERE nome = %s"
                dados = (nome,)
                mycursor.execute(procuraAlface, dados)

                listaAlface = mycursor.fetchall()
                numberOfIndex = self.alfaceCB.count()
                for x in range (0, numberOfIndex):
                    if(str(listaAlface[0][0]) == self.alfaceCB.itemText(x)):
                        self.alfaceCB.setCurrentIndex(x)


            
                # Tomate
                procuraTomate = "SELECT tomate FROM hamburguer WHERE nome = %s"
                dados = (nome,)
                mycursor.execute(procuraTomate, dados)

                listaTomate = mycursor.fetchall()
                numberOfIndex = self.tomateCB.count()
                for x in range (0, numberOfIndex):
                    if(str(listaTomate[0][0]) == self.tomateCB.itemText(x)):
                        self.tomateCB.setCurrentIndex(x)


                
                # Molho
                procuraMolho = "SELECT molho FROM hamburguer WHERE nome = %s"
                dados = (nome,)
                mycursor.execute(procuraMolho, dados)

                listaMolho = mycursor.fetchall()
                numberOfIndex = self.molhoCB.count()
                for x in range (0, numberOfIndex):
                    if(str(listaMolho[0][0]) == self.molhoCB.itemText(x)):
                        self.molhoCB.setCurrentIndex(x)


                self.encontradoComSucessoMSG()
            else:
                self.nomeInexistenteMSG()

            # Mostra na tabela os dados que foram cadastrados
            self.preencheTabela()
            
            # Encerra a conexão com o banco
            mycursor.close()
            mydb.close()
        



    def setupUi(self, Hamburguers):

        Hamburguers.setObjectName("Hamburguers")
        Hamburguers.resize(500, 700)
        self.centralwidget = QtWidgets.QWidget(Hamburguers)
        self.centralwidget.setObjectName("centralwidget")





# Labels 


        self.hamburguerLabel = QtWidgets.QLabel(self.centralwidget)
        self.hamburguerLabel.setGeometry(QtCore.QRect(50, 10, 120, 30))
        self.hamburguerLabel.setObjectName("hamburguerLabel")



        self.nomeLabel = QtWidgets.QLabel(self.centralwidget)
        self.nomeLabel.setGeometry(QtCore.QRect(75, 240, 50, 30))
        self.nomeLabel.setObjectName("nomeLabel")



        self.paoLabel = QtWidgets.QLabel(self.centralwidget)
        self.paoLabel.setGeometry(QtCore.QRect(75, 280, 50, 30))
        self.paoLabel.setObjectName("paoLabel")



        self.carneLabel = QtWidgets.QLabel(self.centralwidget)
        self.carneLabel.setGeometry(QtCore.QRect(75, 320, 50, 30))
        self.carneLabel.setObjectName("carneLabel")



        self.queijoLabel = QtWidgets.QLabel(self.centralwidget)
        self.queijoLabel.setGeometry(QtCore.QRect(75, 360, 50, 30))
        self.queijoLabel.setObjectName("queijoLabel")



        self.cebolaLabel = QtWidgets.QLabel(self.centralwidget)
        self.cebolaLabel.setGeometry(QtCore.QRect(75, 400, 50, 30))
        self.cebolaLabel.setObjectName("cebolaLabel")



        self.ovoLabel = QtWidgets.QLabel(self.centralwidget)
        self.ovoLabel.setGeometry(QtCore.QRect(75, 440, 50, 30))
        self.ovoLabel.setObjectName("ovoLabel")



        self.alfaceLabel = QtWidgets.QLabel(self.centralwidget)
        self.alfaceLabel.setGeometry(QtCore.QRect(75, 480, 50, 30))
        self.alfaceLabel.setObjectName("alfaceLabel")



        self.tomateLabel = QtWidgets.QLabel(self.centralwidget)
        self.tomateLabel.setGeometry(QtCore.QRect(75, 520, 50, 30))
        self.tomateLabel.setObjectName("tomateLabel")



        self.molhoLabel = QtWidgets.QLabel(self.centralwidget)
        self.molhoLabel.setGeometry(QtCore.QRect(75, 560, 50, 30))
        self.molhoLabel.setObjectName("molhoLabel")





# Table

        self.hamburguerTable = QtWidgets.QTableWidget(self.centralwidget)
        self.hamburguerTable.setGeometry(QtCore.QRect(40, 40, 420, 120))
        self.hamburguerTable.setObjectName("hamburguerTable")
        
        # Seta o número de colunas da tabela
        self.hamburguerTable.setColumnCount(9)

        # Seta o nome das colunas da tabela
        item = QtWidgets.QTableWidgetItem()
        self.hamburguerTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.hamburguerTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.hamburguerTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.hamburguerTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.hamburguerTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.hamburguerTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.hamburguerTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.hamburguerTable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.hamburguerTable.setHorizontalHeaderItem(8, item)



        item = self.hamburguerTable.horizontalHeaderItem(0)
        item.setText("Nome")
        item = self.hamburguerTable.horizontalHeaderItem(1)
        item.setText("Pão")
        item = self.hamburguerTable.horizontalHeaderItem(2)
        item.setText("Carne")
        item = self.hamburguerTable.horizontalHeaderItem(3)
        item.setText("Queijo")
        item = self.hamburguerTable.horizontalHeaderItem(4)
        item.setText("Cebola")
        item = self.hamburguerTable.horizontalHeaderItem(5)
        item.setText("Ovo")
        item = self.hamburguerTable.horizontalHeaderItem(6)
        item.setText("Alface")
        item = self.hamburguerTable.horizontalHeaderItem(7)
        item.setText("Tomate")
        item = self.hamburguerTable.horizontalHeaderItem(8)
        item.setText("Molho")

        # Seta o número de linhas da tabela
        self.hamburguerTable.setRowCount(1)



# Text Boxes

        self.nomeTB = QtWidgets.QLineEdit(self.centralwidget)
        self.nomeTB.setGeometry(QtCore.QRect(165, 240, 250, 30))
        self.nomeTB.setObjectName("nomeTB")



# Combo Boxes

        self.paoCB = QtWidgets.QComboBox(self.centralwidget)
        self.paoCB.setGeometry(QtCore.QRect(165, 280, 250, 30))
        self.paoCB.setObjectName("paoTB")

        # Adicionando os tiposde pão
        self.paoCB.addItem("Francês")
        self.paoCB.addItem("Gergelim")
        self.paoCB.addItem("Milho")
        self.paoCB.addItem("Italiano branco")
        self.paoCB.addItem("Gergelim")




        self.carneCB = QtWidgets.QComboBox(self.centralwidget)
        self.carneCB.setGeometry(QtCore.QRect(165, 320, 250, 30))
        self.carneCB.setObjectName("carneTB")

        # Adicionando os tiposde carne
        self.carneCB.addItem("Costela")
        self.carneCB.addItem("Picanha")
        self.carneCB.addItem("Patinho")
        self.carneCB.addItem("Filé Mignom")
        self.carneCB.addItem("Contra filé")
        self.carneCB.addItem("Frango")
        self.carneCB.addItem("Costela de porco")



        self.queijoCB = QtWidgets.QComboBox(self.centralwidget)
        self.queijoCB.setGeometry(QtCore.QRect(165, 360, 250, 30))
        self.queijoCB.setObjectName("queijoTB")

        # Adicionando os tiposde queijo
        self.queijoCB.addItem("Prato")
        self.queijoCB.addItem("Mussarela")
        self.queijoCB.addItem("Cheddar")
        self.queijoCB.addItem("Catupiry")
        self.queijoCB.addItem("Gorgonzola")



        self.cebolaCB = QtWidgets.QComboBox(self.centralwidget)
        self.cebolaCB.setGeometry(QtCore.QRect(165, 400, 250, 30))
        self.cebolaCB.setObjectName("cebolaTB")

        # Adicionando opções de cebola
        self.cebolaCB.addItem("Com cebola")
        self.cebolaCB.addItem("Cebola roxa")
        self.cebolaCB.addItem("Cebola caramelizada")
        self.cebolaCB.addItem("Sem cebola")



        self.ovoCB = QtWidgets.QComboBox(self.centralwidget)
        self.ovoCB.setGeometry(QtCore.QRect(165, 440, 250, 30))
        self.ovoCB.setObjectName("ovoCB")

        # Adicionando opções de ovo
        self.ovoCB.addItem("Com ovo")
        self.ovoCB.addItem("Sem ovo")



        self.alfaceCB = QtWidgets.QComboBox(self.centralwidget)
        self.alfaceCB.setGeometry(QtCore.QRect(165, 480, 250, 30))
        self.alfaceCB.setObjectName("alfaceCB")

        # Adicionando opções de alface
        self.alfaceCB.addItem("Com alface")
        self.alfaceCB.addItem("Sem alface")



        self.tomateCB = QtWidgets.QComboBox(self.centralwidget)
        self.tomateCB.setGeometry(QtCore.QRect(165, 520, 250, 30))
        self.tomateCB.setObjectName("tomateCB")

        # Adicionando opções de tomate
        self.tomateCB.addItem("Com tomate")
        self.tomateCB.addItem("Sem tomate")



        self.molhoCB = QtWidgets.QComboBox(self.centralwidget)
        self.molhoCB.setGeometry(QtCore.QRect(165, 560, 250, 30))
        self.molhoCB.setObjectName("molhoCB")

        # Adicionando opções de molho
        self.molhoCB.addItem("Maionese")
        self.molhoCB.addItem("Mostarda e mel")
        



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
        self.voltarBTN.setGeometry(QtCore.QRect(200, 620, 100, 30))
        self.voltarBTN.setObjectName("voltarBTN")

        # Volta para o menu
        self.voltarBTN.clicked.connect(self.switchToEditMenu)





        Hamburguers.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Hamburguers)
        self.statusbar.setObjectName("statusbar")
        Hamburguers.setStatusBar(self.statusbar)

        self.retranslateUi(Hamburguers)
        QtCore.QMetaObject.connectSlotsByName(Hamburguers)


    def retranslateUi(self, Hamburguers):

        _translate = QtCore.QCoreApplication.translate
        Hamburguers.setWindowTitle(_translate("Hamburguers", "Editar cardápio de hamburguers"))
        self.hamburguerLabel.setText(_translate("Hamburguers", "Cardápio de hamburguers :"))
        self.nomeLabel.setText(_translate("Hamburguers", "Nome:"))
        self.paoLabel.setText(_translate("Hamburguers", "Pão:"))
        self.carneLabel.setText(_translate("Hamburguers", "Carne:"))
        self.queijoLabel.setText(_translate("Hamburguers", "Queijo:"))
        self.cebolaLabel.setText(_translate("Hamburguers", "Cebola:"))
        self.ovoLabel.setText(_translate("Hamburguers", "Ovo:"))
        self.alfaceLabel.setText(_translate("Hamburguers", "Alface:"))
        self.tomateLabel.setText(_translate("Hamburguers", "Tomate:"))
        self.molhoLabel.setText(_translate("Hamburguers", "Molho:"))
        self.cadastrarBTN.setText(_translate("Hamburguers", "Cadastrar"))
        self.atualizarBTN.setText(_translate("Hamburguers", "Atualizar"))
        self.excluirBTN.setText(_translate("Hamburguers", "Excluir"))
        self.procurarBTN.setText(_translate("Hamburguers", "Procurar"))
        self.voltarBTN.setText(_translate("Hamburguers", "Voltar"))





    # Mensagens de tratamento de excessão

    def nomeVazioMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Nome vazio!")
        msg.setText("Por favor, entre com o nome!")

        msg.exec_()

    

    def naoNumeroTelefoneMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Entrada do telefone inválida!")
        msg.setText("Por favor, entre o telefone somente com números e sem espaços!")

        msg.exec_()



    def nomeGrandeMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Entrada de nome inválida!")
        msg.setText("O nome que está tentando inserir ultrapassa o limite de 200 caracteres!")

        msg.exec_()
    


    def nomeInexistenteMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Hamburguer não encontrado!")
        msg.setText("Esse hamburguer não está cadastrado!")

        msg.exec_()



    def nomeJaCadastradoMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Nome em uso!")
        msg.setText("Já existe um cadastro com esse nome!")

        msg.exec_() 



    # Caixas de confirmação de ações

    def confirmaExcluirMSG(self, hamburguer):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Pedido de confirmação!")
        msg.setText("Deseja realmente excluir o cadastro do hamburguer " + str(hamburguer[0][0]) + "?")

        msg.setStandardButtons(QMessageBox.Yes| QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)

        reply = msg.exec_()

        if(reply == QMessageBox.Yes):
            return 1
        else:
            return 0
    


    def confirmaAtualizarMSG(self, hamburguer):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Pedido de confirmação!")
        msg.setText("Deseja realmente atualizar o hamburguer de nome" + str(hamburguer[0][0]) + "?")

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
        msg.setText("O hamburguer foi cadastrado com sucesso!")

        msg.exec_()
    


    def excluidoComSucessoMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Excluído com sucesso!")
        msg.setText("O hamburguer foi deletado com sucesso!")

        msg.exec_()



    def atualizadoComSucessoMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Atualizado com sucesso!")
        msg.setText("Os dados do hamburguer foram atualizados com sucesso!")

        msg.exec_()



    def encontradoComSucessoMSG(self):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle("Cadastro encontrado com sucesso!")
        msg.setText("O hamburguer foi encontrado com sucesso!")

        msg.exec_()
    





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Hamburguers = QtWidgets.QMainWindow()
    ui = Ui_Hamburguers()
    ui.setupUi(Hamburguers)
    Hamburguers.show()
    sys.exit(app.exec_())
