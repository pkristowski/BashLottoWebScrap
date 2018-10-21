# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lotto.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import datetime #do ściągnięcia daty
import glob
import os
from PyQt5 import QtCore, QtGui, QtWidgets #do uruchomienia utworzonego GUI

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(668, 354)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)
        self.aktualnyEuro = QtWidgets.QPushButton(self.centralwidget)
        self.aktualnyEuro.setObjectName("aktualnyEuro")
        self.aktualnyEuro.clicked.connect(self.aktualnyEuro_clicked)
        
        self.gridLayout.addWidget(self.aktualnyEuro, 7, 1, 1, 1)
        self.aktualnyEkstra = QtWidgets.QPushButton(self.centralwidget)
        self.aktualnyEkstra.setObjectName("aktualnyEkstra")
        self.aktualnyEkstra.clicked.connect(self.aktualnyEkstra_clicked)
        
        self.gridLayout.addWidget(self.aktualnyEkstra, 6, 1, 1, 1)
        self.dataEkstra = QtWidgets.QDateEdit(self.centralwidget)
        self.dataEkstra.setObjectName("dataEkstra")
        self.gridLayout.addWidget(self.dataEkstra, 6, 2, 1, 1)
        self.dataEuro = QtWidgets.QDateEdit(self.centralwidget)
        self.dataEuro.setObjectName("dataEuro")
        self.gridLayout.addWidget(self.dataEuro, 7, 2, 1, 1)
        self.aktualnyLotto = QtWidgets.QPushButton(self.centralwidget)
        self.aktualnyLotto.setObjectName("aktualnyLotto")
        self.aktualnyLotto.clicked.connect(self.aktualnyLotto_clicked)
        
        self.gridLayout.addWidget(self.aktualnyLotto, 2, 1, 1, 1)
        self.aktualnyMini = QtWidgets.QPushButton(self.centralwidget)
        self.aktualnyMini.setObjectName("aktualnyMini")
        self.aktualnyMini.clicked.connect(self.aktualnyMini_clicked)
        
        self.gridLayout.addWidget(self.aktualnyMini, 3, 1, 1, 1)
        self.dataMulti = QtWidgets.QDateEdit(self.centralwidget)
        self.dataMulti.setObjectName("dataMulti")
        self.gridLayout.addWidget(self.dataMulti, 4, 2, 1, 1)
        self.dataLotto = QtWidgets.QDateEdit(self.centralwidget)
        self.dataLotto.setObjectName("dataLotto")
        self.gridLayout.addWidget(self.dataLotto, 2, 2, 1, 1)
        self.dataMini = QtWidgets.QDateEdit(self.centralwidget)
        self.dataMini.setObjectName("dataMini")
        self.gridLayout.addWidget(self.dataMini, 3, 2, 1, 1)
        self.dataKaskada = QtWidgets.QDateEdit(self.centralwidget)
        self.dataKaskada.setObjectName("dataKaskada")
        self.gridLayout.addWidget(self.dataKaskada, 5, 2, 1, 1)
        self.aktualnyKaskada = QtWidgets.QPushButton(self.centralwidget)
        self.aktualnyKaskada.setObjectName("aktualnyKaskada")
        self.aktualnyKaskada.clicked.connect(self.aktualnyKaskada_clicked)
        
        self.gridLayout.addWidget(self.aktualnyKaskada, 5, 1, 1, 1)
        self.aktualnyMulti = QtWidgets.QPushButton(self.centralwidget)
        self.aktualnyMulti.setObjectName("aktualnyMulti")
        self.aktualnyMulti.clicked.connect(self.aktualnyMulti_clicked)
        
        self.gridLayout.addWidget(self.aktualnyMulti, 4, 1, 1, 1)
        self.wynik = QtWidgets.QTextBrowser(self.centralwidget)
        self.wynik.setObjectName("wynik")
        self.gridLayout.addWidget(self.wynik, 10, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 8, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 668, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Lotto"))
        self.label_4.setText(_translate("MainWindow", "MultiMulti"))
        self.label_5.setText(_translate("MainWindow", "Kaskada"))
        self.label_7.setText(_translate("MainWindow", "Euro Jackpot"))
        self.label_6.setText(_translate("MainWindow", "Ekstra Pensja"))
        self.label_2.setText(_translate("MainWindow", "MiniLotto"))
        self.label_3.setText(_translate("MainWindow", "Aplikacja do pobierania wyników Lotto"))
        self.aktualnyEuro.setText(_translate("MainWindow", "Aktualny wynik"))
        self.aktualnyEkstra.setText(_translate("MainWindow", "Aktualny wynik"))
        self.aktualnyLotto.setText(_translate("MainWindow", "Aktualny wynik"))
        self.aktualnyMini.setText(_translate("MainWindow", "Aktualny wynik"))
        self.aktualnyKaskada.setText(_translate("MainWindow", "Aktualny wynik"))
        self.aktualnyMulti.setText(_translate("MainWindow", "Aktualny wynik"))
    #funkcje uaktywniane po kliknięciu
    def aktualnyEuro_clicked(self):
        _translate = QtCore.QCoreApplication.translate
        #list_of_files = glob.glob('./EuroJackpot/*')
        #latest_file = max(list_of_files, key=lambda x:'./EuroJackpot/\d{1,2}-\d{1,2}-*')
        #newest = open(latest_file)
        today=datetime.date.today()
        for i in range(0, 31):
                file_path='./EuroJackpot/' + today.strftime('%d-%m-%Y')
                if os.path.isfile(file_path):
                        newest = open(file_path)
                        self.wynik.setText(_translate("MainWindow", newest.read()))
                        break
                else:
                        today=today - datetime.timedelta(1)
                        #self.wynik.setText(_translate("MainWindow", str(today)))
    def aktualnyLotto_clicked(self):
        today=datetime.date.today()
        
    def aktualnyMini_clicked(self):
        today=datetime.date.today()
        
    def aktualnyMulti_clicked(self):
        today=datetime.date.today()
        
    def aktualnyEkstra_clicked(self):
        today=datetime.date.today()
        
    def aktualnyKaskada_clicked(self):
        today=datetime.date.today()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

