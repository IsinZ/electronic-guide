# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\KONSTANTIN\Documents\ui\LoginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(400, 170)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelLogin = QtWidgets.QLabel(self.centralwidget)
        self.labelLogin.setGeometry(QtCore.QRect(50, 50, 50, 15))
        self.labelLogin.setObjectName("labelLogin")
        self.labelPass = QtWidgets.QLabel(self.centralwidget)
        self.labelPass.setGeometry(QtCore.QRect(50, 100, 50, 15))
        self.labelPass.setObjectName("labelPass")
        self.lineEditLogin = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditLogin.setGeometry(QtCore.QRect(125, 50, 130, 20))
        self.lineEditLogin.setObjectName("lineEditLogin")
        self.lineEditPass = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPass.setGeometry(QtCore.QRect(125, 100, 130, 20))
        self.lineEditPass.setObjectName("lineEditPass")
        self.ok = QtWidgets.QPushButton(self.centralwidget)
        self.ok.setGeometry(QtCore.QRect(300, 65, 75, 40))
        self.ok.setObjectName("ok")
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login"))
        self.labelLogin.setText(_translate("LoginWindow", "Login:"))
        self.labelPass.setText(_translate("LoginWindow", "Password:"))
        self.ok.setText(_translate("LoginWindow", "Ok"))

