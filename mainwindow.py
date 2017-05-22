# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        MainWindow.setStyleSheet("background-color: rgb(82, 175, 50);\n"
"font: 75 12pt \"Courier 10 Pitch\";")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.frame_2 = QtWidgets.QFrame(self.centralWidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 0, 381, 241))
        self.frame_2.setStyleSheet("background-color: rgb(29, 67, 111);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(16, 21, 351, 201))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 20, 331, 171))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../index-logo-altec.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 24))
        self.menuBar.setObjectName("menuBar")
        self.menuSGD = QtWidgets.QMenu(self.menuBar)
        self.menuSGD.setObjectName("menuSGD")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionAlta_de_Documentos = QtWidgets.QAction(MainWindow)
        self.actionAlta_de_Documentos.setObjectName("actionAlta_de_Documentos")
        self.actionBuscar_Documentos = QtWidgets.QAction(MainWindow)
        self.actionBuscar_Documentos.setObjectName("actionBuscar_Documentos")
        self.actionDescarga_documentos = QtWidgets.QAction(MainWindow)
        self.actionDescarga_documentos.setObjectName("actionDescarga_documentos")
        self.menuSGD.addAction(self.actionAlta_de_Documentos)
        self.menuSGD.addAction(self.actionBuscar_Documentos)
        self.menuBar.addAction(self.menuSGD.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuSGD.setTitle(_translate("MainWindow", "SGD"))
        self.actionAlta_de_Documentos.setText(_translate("MainWindow", "Alta de Documentos"))
        self.actionBuscar_Documentos.setText(_translate("MainWindow", "Buscar Documentos y Descargar"))
        self.actionDescarga_documentos.setText(_translate("MainWindow", "Descarga documentos"))

