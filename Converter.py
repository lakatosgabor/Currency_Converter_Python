# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\benban97\PycharmProjects\3. felev csoportos progbeadando\converter.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ConverterExceptions import MissingDataException
from ConverterExceptions import TypeError
from ConverterExceptions import TypeError2
from ConverterExceptions import SameDataException


class Ui_CurrenyConverter(object):

    lista = []      #currency, shortened form, exchange rate, country   (def comboAdd-ban van feltöltve)
    lista2 = []     #shortened form, exchange rate, country             (def show-ban van feltöltve)

    def setupUi(self, CurrenyConverter):
        CurrenyConverter.setObjectName("CurrenyConverter")
        CurrenyConverter.resize(456, 653)
        self.centralwidget = QtWidgets.QWidget(CurrenyConverter)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 100, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(300, 70, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.inFrom = QtWidgets.QComboBox(self.centralwidget)
        self.inFrom.setGeometry(QtCore.QRect(60, 70, 85, 27))
        self.inFrom.setObjectName("inFrom")
        self.inTo = QtWidgets.QComboBox(self.centralwidget)
        self.inTo.setGeometry(QtCore.QRect(330, 70, 85, 27))
        self.inTo.setObjectName("inTo")
        self.inAmount = QtWidgets.QLineEdit(self.centralwidget)
        self.inAmount.setGeometry(QtCore.QRect(100, 140, 71, 31))
        self.inAmount.setObjectName("inAmount")
        self.outAmount = QtWidgets.QListWidget(self.centralwidget)
        self.outAmount.setGeometry(QtCore.QRect(260, 140, 71, 31))
        self.outAmount.setObjectName("outAmount")
        self.btnConvert = QtWidgets.QPushButton(self.centralwidget)
        self.btnConvert.setGeometry(QtCore.QRect(170, 190, 91, 31))
        self.btnToAllCurrencies = QtWidgets.QPushButton(self.centralwidget)
        self.btnToAllCurrencies.setGeometry(QtCore.QRect(10, 190, 150, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnConvert.setFont(font)
        self.btnConvert.setObjectName("btnConvert")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(170, 150, 91, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 230, 451, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(160, 250, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 290, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 340, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(220, 340, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(220, 290, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.infoRate = QtWidgets.QListWidget(self.centralwidget)
        self.infoRate.setGeometry(QtCore.QRect(384, 286, 50, 26))
        self.infoRate.setObjectName("infoRate")
        self.infoShort = QtWidgets.QListWidget(self.centralwidget)
        self.infoShort.setGeometry(QtCore.QRect(130, 340, 50, 25))
        self.infoShort.setObjectName("infoShort")
        self.infoCountry = QtWidgets.QListWidget(self.centralwidget)
        self.infoCountry.setGeometry(QtCore.QRect(280, 340, 130, 45))
        self.infoCountry.setObjectName("infoCountry")
        self.infoCurrency = QtWidgets.QComboBox(self.centralwidget)
        self.infoCurrency.setGeometry(QtCore.QRect(80, 290, 135, 27))
        self.infoCurrency.setObjectName("infoCurrency")
        self.btnShow = QtWidgets.QPushButton(self.centralwidget)
        self.btnShow.setGeometry(QtCore.QRect(170, 390, 99, 27))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnShow.setFont(font)
        self.btnShow.setObjectName("btnShow")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 450, 451, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(177, 470, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(310, 510, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(150, 510, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(10, 510, 68, 17))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.addCurrency = QtWidgets.QLineEdit(self.centralwidget)
        self.addCurrency.setGeometry(QtCore.QRect(10, 530, 113, 27))
        self.addCurrency.setObjectName("addCurrency")
        self.addShort = QtWidgets.QLineEdit(self.centralwidget)
        self.addShort.setGeometry(QtCore.QRect(150, 530, 113, 27))
        self.addShort.setObjectName("addShort")
        self.addRate = QtWidgets.QLineEdit(self.centralwidget)
        self.addRate.setGeometry(QtCore.QRect(340, 530, 113, 27))
        self.addRate.setObjectName("addRate")
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(230, 580, 99, 27))
        self.btnShow.setFont(font)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(10, 560, 68, 17))
        self.addCountry = QtWidgets.QLineEdit(self.centralwidget)
        self.addCountry.setGeometry(QtCore.QRect(10, 580, 113, 27))
        self.addCountry.setObjectName("addCountry")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnAdd.setFont(font)
        self.btnAdd.setObjectName("btnAdd")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 530, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10.5)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        CurrenyConverter.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CurrenyConverter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 456, 25))
        self.menubar.setObjectName("menubar")
        CurrenyConverter.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CurrenyConverter)
        self.statusbar.setObjectName("statusbar")
        CurrenyConverter.setStatusBar(self.statusbar)

        self.retranslateUi(CurrenyConverter)
        QtCore.QMetaObject.connectSlotsByName(CurrenyConverter)

        self.infoCurrency.addItem(self.comboAdd())
        self.btnShow.clicked.connect(self.show)
        self.btnAdd.clicked.connect(self.addNew)
        self.inFrom.addItem(self.comboAddForConverting())
        self.btnConvert.clicked.connect(self.ootAmount)
        self.btnToAllCurrencies.clicked.connect(self.messageb)


    def retranslateUi(self, CurrenyConverter):
        _translate = QtCore.QCoreApplication.translate
        CurrenyConverter.setWindowTitle(_translate("CurrenyConverter", "Currency Converter"))
        self.label.setText(_translate("CurrenyConverter", "Currency Converter"))
        self.label_3.setText(_translate("CurrenyConverter", "amount:"))
        self.label_4.setText(_translate("CurrenyConverter", "To:"))
        self.label_5.setText(_translate("CurrenyConverter", "From:"))
        self.btnConvert.setText(_translate("CurrenyConverter", "Convert"))
        self.btnToAllCurrencies.setText(_translate("CurrenyConverter", "Convert to all currencies"))
        self.label_6.setText(_translate("CurrenyConverter", "Information"))
        self.label_7.setText(_translate("CurrenyConverter", "Currency:"))
        self.label_8.setText(_translate("CurrenyConverter", "Shortened form: "))
        self.label_9.setText(_translate("CurrenyConverter", "Country:"))
        self.label_10.setText(_translate("CurrenyConverter", "Exchange rate: 1 EUR - "))
        self.btnShow.setText(_translate("CurrenyConverter", "Show"))
        self.label_11.setText(_translate("CurrenyConverter", "Add new"))
        self.label_12.setText(_translate("CurrenyConverter", "Exchange rate:"))
        self.label_13.setText(_translate("CurrenyConverter", "Shortened form:"))
        self.label_14.setText(_translate("CurrenyConverter", "Currency:"))
        self.btnAdd.setText(_translate("CurrenyConverter", "Add"))
        self.label_2.setText(_translate("CurrenyConverter", "1 EUR - "))
        self.label_15.setText(_translate("CurrenyConverter", "Country"))


    def comboAddForConverting(self):    #feltöltjük a convert résznél a két legördülő comboboxot
        try:
            file = open('currency.txt', 'r')    #fájl megnyitása olvasásra, feldaraboljuk és így kinyerjük a txt-ből a szükséges információkat
            for line in file:
                tmp = line.split(':')
                tmp=[tmp[1],tmp[2],tmp[3]]
                self.lista2.append(tmp)

        except FileNotFoundError:
            print('The given file is not found!')
        for i in sorted(self.lista2):           #index alapján kinyerjük a rövidítéseket,ezekkel töltjük fel a comboboxokat + rendezzük a rövidítéseket betűrendbe
            self.inFrom.addItem(i[0])
            self.inTo.addItem(i[0])

        file.close()

    def ootAmount(self):        #ez maga a convert folyamat
        fromCurrency = self.inFrom.currentText()
        toCurrency = self.inTo.currentText()
        amount=self.inAmount.text()


        try:                       #megnézi,hogy a szám konvertálható-e(nem negatív és nem is betű, vagy egyéb jel, egy darab . megengedett de nem lehet kezdő karakter)
            if len(amount) != 0:
                tmp = []
                for i in amount:
                    tmp.append(i)

                summa = 0

                for i in tmp:       # . számlálása
                    if i == '.':
                        summa += 1


                for i in tmp:
                    if i != '0' and i != '1' and i != '2' and i!= '3' and i != '4' and i != '5' and i != '6' and i != '7' and i != '8' and i != '9' and i != '.' or summa > 1 or tmp[0]=='.':
                        raise TypeError

                if len(tmp) > 1 and tmp[0] == '0' and tmp[1] != '.':        #így nem lehet pl 012
                    raise TypeError

            else:
                raise TypeError

            if len(amount) > 0:
                x = float(self.inAmount.text())

            else:
                raise TypeError


        except TypeError as te:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Warning!')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Please give me a valid amount!")
            msg.exec()

        else:
            for i in range(len(self.lista)):    #kiválasztott elemmel megegyező elemet kerestünk a listánkban, annak az árfolyam indexét mentettük, amely kell majd a számoláshoz
                self.outAmount.clear()              #tisztítjuk az outAmountot, mert különben minden convertnél bentmarad az előző convertek eredménye
                if fromCurrency == self.lista[i][1]:
                    ind2 = i

                if toCurrency == self.lista[i][1]:
                    ind3 = i

            inRate = self.lista[ind2][2]            #amiből váltunk árfolyam
            outRate = self.lista[ind3][2]           #amibe váltani kell árfolyama



            gotAmount =str(round(x * (outRate/inRate),2))      #árfolyam váltás
            self.outAmount.addItem(gotAmount)


    def comboAdd(self):     # a show részben történő combobox feltöltés
        try:
            file = open('currency.txt', 'r')
            for line in file:
                tmp = line.split(':')
                tmp = [tmp[0],tmp[1],float(tmp[2]),tmp[3][:-1]]     #enter levágása a végén = tmp[3][:-1]
                self.lista.append(tmp)

        except FileNotFoundError:
            print('The given file is not found!')


        for i in sorted(self.lista):
            self.infoCurrency.addItem(i[0])


        file.close()

    def show(self):     #a show rész függvénye
        selectedCurrency = self.infoCurrency.currentText()

        try:
            file = open('currency.txt', 'r')
            for line in file:
                tmp = line.split(':')
                tmp=[tmp[1],tmp[2],tmp[3]]
                self.lista2.append(tmp)

        except FileNotFoundError:
            print('The given file is not found!')


        for i in range (len(self.lista)):
            if selectedCurrency == self.lista[i][0]:        #kiválasztott árfolyamhoz tartozó index megkeresése
                ind = i
                self.infoRate.clear()       # minden gombnyomásra tisztítja a mezőket, így nem ír semmit többször
                self.infoShort.clear()
                self.infoCountry.clear()

                self.infoRate.addItem(self.lista2[ind][1])      #mezőkhöz való hozzáadás
                self.infoShort.addItem(self.lista2[ind][0])
                self.infoCountry.addItem(self.lista2[ind][2])

        file.close()

    def addNew(self):       #új valuta beillesztése a fájlba

        country = self.addCountry.text()
        shortened = self.addShort.text()
        rate = self.addRate.text()
        currency = self.addCurrency.text()

        abc = ['a','á','b','c','d','e','é','f','g','gy','h','i','í','j','k','l','m',
             'n','o','ó','ö','ő','p','q','r','s','t','u','ú','ü','ű','v','w','x',
             'y','z',' ']                                                               #ellenőrzésképpen, hogy csak betű kerülhessen az adott mezőkhöz, kisbetű és nagybetű egyaránt

        abc2 = ['A', 'Á', 'B', 'C', 'D', 'E', 'É', 'F', 'G', 'H', 'I', 'Í', 'J', 'K', 'L', 'M',
               'N', 'O', 'Ó', 'Ö', 'Ő', 'P', 'Q', 'R', 'S', 'T', 'U', 'Ú', 'Ü', 'Ű', 'V', 'W', 'X',
               'Y', 'Z', ' ']

        currencyList = []
        exchangeList=[]
        countryList=[]
        shortenList=[]

        tmp=0

        for i in currency:
            currencyList.append(i)
        for i in country:
            countryList.append(i)
        for i in rate:
            exchangeList.append(i)
        for i in shortened:
            shortenList.append(i)


        try:

            if len(country) == 0:
                raise MissingDataException('country')

            if len(shortened) == 0:
                raise MissingDataException('shortened form')

            if len(rate) == 0:
                raise MissingDataException('exchange rate')

            if len(currency) == 0:
                raise MissingDataException('currency')



            if countryList[0] == ',' or countryList[0] == ' ':       #nem kezdődhet vesszővel, de lehet benne ha több ország lenne egy valutához
                raise TypeError2('country')

            if currencyList[0] == ' ':
                raise TypeError2('currency')

            if shortenList[0] == ' ':
                raise TypeError2('shortenned form')

            if exchangeList[0] == ' ':
                raise TypeError2('exchange rate')

            for i in range (len(countryList)):
                if countryList[i] not in abc and countryList[i] not in abc2 and countryList[i] != ',' or countryList[-1] == ' ':              #ha nem felel meg a csak betűnek és spacenek, vagy az exchange ratenél nem felel meg a számnak, vagy a pontnak akkor dobja a hibát
                    raise TypeError2('country')

            for i in currencyList:
                if i not in abc and i not in abc2 or currencyList[-1] == ' ':
                    raise TypeError2('currency')

            for i in shortenList:
                if i not in abc and i not in abc2 or shortenList[-1] == ' ':
                    raise TypeError2('shortened form')

            for i in exchangeList:
                if i == '.':
                    tmp += 1

            for i in exchangeList:
                if i != '0' and i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6' and i != '7' and i != '8' and i != '9' and i != '.' or tmp > 1 or exchangeList[-1] == ' ':
                    raise TypeError2('exchange rate')

            if len(exchangeList) > 1 and exchangeList[0] == '0' and exchangeList[1] != '.' or(len(exchangeList)==1 and exchangeList[0] == '0'):         #így nem lehet olyan hogy 023
                raise TypeError2('exchange rate')




        except MissingDataException as mse:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Warning!')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText(mse.__str__())
            msg.exec()

        except TypeError2 as te:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Warning!')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText(te.__str__())
            msg.exec()

        else:
            helpL=[]

            readFile = open("currency.txt", 'r')
            for i in readFile:
                 tmp = i.split(':')
                 helpL.append([tmp[0],tmp[1]])


            try:
                for i in helpL:
                    if i[0] == currency.upper() and i[1] == shortened.upper():          #felnagyítjuk a beírt betúket, így nem lehet kisbetű nagybetű eltérés és nem lehet olyan ami már van a fájlban
                        raise SameDataException

            except SameDataException as dse:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Warning!')
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText('This currency already exists!')
                    msg.exec()

            else:
                readFile.close()
                writeFile = open("currency.txt",'a')
                writeFile.writelines("\n" + self.addCurrency.text().upper() + ':' + self.addShort.text().upper() + ':' + self.addRate.text() + ':' + self.addCountry.text().upper())        #fájlba beíratás egységesen naggyal
                writeFile.close()

                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('New Currency Added')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('The currency has been succesfully added!\nPlease restart the program to refresh the database!')
                msg.exec()


    def messageb(self):
        list=[]
        file=open("currency.txt",'r')
        for line in file:
            tmp=line.split(":")
            tmp=[tmp[1],tmp[2]]
            list.append(tmp)

        amount=self.inAmount.text()
        fromCurrency = self.inFrom.currentText()
        rate=0
        string = ""
        x=0


        try:                                   #hibavizsgálat, nem lehet nem megfelelő formátumú, olyan mint az előbb
            if len(amount) != 0:
                tmp2 = []
                for i in amount:
                    tmp2.append(i)

                summa = 0

                for i in tmp2:
                    if i == '.':
                        summa += 1


                for i in tmp2:
                    if i != '0' and i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6' and i != '7' and i != '8' and i != '9' and i != '.' or summa > 1 or tmp2[0]=='.':
                        raise TypeError


                if len(tmp2) > 1 and tmp2[0] == '0' and tmp2[1] != '.':
                    raise TypeError


            else:
                raise TypeError

            if len(amount) > 0:
                amount=float(self.inAmount.text())

            else:
                raise TypeError

        except TypeError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Warning!')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('Give me a valid format!')
            msg.exec()


        else:
            for i in list:
                if i[0] == fromCurrency:
                    rate = i[1]

            rate=float(rate)
            list = sorted(list)

            for i in range(len(list)):                                  #sztringhez fűzés majd kiíratás a message box segítségével
                x = round(amount * (float(list[i][1])/rate),2)
                x = str(x)
                string+=list[i][0] + " = " + x + "\n"


            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle(str(amount)+"  "+fromCurrency)
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText(string)
            msg.exec()

        file.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CurrenyConverter = QtWidgets.QMainWindow()
    ui = Ui_CurrenyConverter()
    ui.setupUi(CurrenyConverter)
    CurrenyConverter.show()
    sys.exit(app.exec_())
