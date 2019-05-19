# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Info.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

class Ui_Info(object):
    def setupUi(self, Info):
        Info.setObjectName("Info")
        Info.setWindowIcon(QIcon("GUI/UI/icon.png"))
        Info.resize(600, 450)
        self.centralwidget = QtWidgets.QWidget(Info)
        self.centralwidget.setObjectName("centralwidget")
        self.info = QtWidgets.QTextBrowser(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(20, 20, 560, 360))
        self.info.setObjectName("info")
        self.readBtn = QtWidgets.QPushButton(self.centralwidget)
        self.readBtn.setGeometry(QtCore.QRect(20, 400, 560, 30))
        self.readBtn.setObjectName("readBtn")
        Info.setCentralWidget(self.centralwidget)

        self.retranslateUi(Info)
        QtCore.QMetaObject.connectSlotsByName(Info)

    def retranslateUi(self, Info):
        _translate = QtCore.QCoreApplication.translate
        Info.setWindowTitle(_translate("Info", "Info"))
        self.readBtn.setText(_translate("Info", "Read"))

