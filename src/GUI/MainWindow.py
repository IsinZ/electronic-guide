# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.recognizer = QtWidgets.QPushButton(self.centralwidget)
        self.recognizer.setGeometry(QtCore.QRect(550, 50, 150, 50))
        self.recognizer.setObjectName("recognizer")
        self.qr = QtWidgets.QPushButton(self.centralwidget)
        self.qr.setGeometry(QtCore.QRect(550, 150, 150, 50))
        self.qr.setObjectName("qr")
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(550, 450, 150, 50))
        self.login.setObjectName("login")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(50, 50, 450, 450))
        self.tableView.setObjectName("tableView")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Guide"))
        self.recognizer.setText(_translate("MainWindow", "Recognizer"))
        self.qr.setText(_translate("MainWindow", "Qr"))
        self.login.setText(_translate("MainWindow", "Login"))

