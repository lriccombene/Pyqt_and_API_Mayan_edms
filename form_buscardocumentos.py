# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_buscardocumentos.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_buscadordocumentos(object):
    def setupUi(self, form_buscadordocumentos):
        form_buscadordocumentos.setObjectName("form_buscadordocumentos")
        form_buscadordocumentos.resize(792, 580)
        self.tabWidget_2 = QtWidgets.QTabWidget(form_buscadordocumentos)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 10, 771, 481))
        self.tabWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_id = QtWidgets.QLabel(self.tab_2)
        self.lbl_id.setText("")
        self.lbl_id.setObjectName("lbl_id")
        self.horizontalLayout_2.addWidget(self.lbl_id)
        self.boton_buscar = QtWidgets.QPushButton(self.tab_2)
        self.boton_buscar.setStyleSheet("background-color: rgb(82, 175, 50);")
        self.boton_buscar.setObjectName("boton_buscar")
        self.horizontalLayout_2.addWidget(self.boton_buscar)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.tw_document = QtWidgets.QTableWidget(self.tab_2)
        self.tw_document.setStyleSheet("background-color: rgb(64, 101, 143);")
        self.tw_document.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw_document.setObjectName("tw_document")
        self.tw_document.setColumnCount(3)
        self.tw_document.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw_document.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_document.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_document.setHorizontalHeaderItem(2, item)
        self.tw_document.horizontalHeader().setDefaultSectionSize(175)
        self.gridLayout_3.addWidget(self.tw_document, 1, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_2, "")
        self.boton_descargar = QtWidgets.QPushButton(form_buscadordocumentos)
        self.boton_descargar.setGeometry(QtCore.QRect(624, 510, 161, 27))
        self.boton_descargar.setStyleSheet("background-color: rgb(64, 101, 143);")
        self.boton_descargar.setObjectName("boton_descargar")
        self.label = QtWidgets.QLabel(form_buscadordocumentos)
        self.label.setGeometry(QtCore.QRect(20, 510, 101, 17))
        self.label.setObjectName("label")
        self.lne_nom_arch = QtWidgets.QLabel(form_buscadordocumentos)
        self.lne_nom_arch.setGeometry(QtCore.QRect(140, 510, 411, 17))
        self.lne_nom_arch.setText("")
        self.lne_nom_arch.setObjectName("lne_nom_arch")

        self.retranslateUi(form_buscadordocumentos)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(form_buscadordocumentos)

    def retranslateUi(self, form_buscadordocumentos):
        _translate = QtCore.QCoreApplication.translate
        form_buscadordocumentos.setWindowTitle(_translate("form_buscadordocumentos", "Form"))
        self.boton_buscar.setText(_translate("form_buscadordocumentos", "Buscar"))
        item = self.tw_document.horizontalHeaderItem(0)
        item.setText(_translate("form_buscadordocumentos", "ID"))
        item = self.tw_document.horizontalHeaderItem(1)
        item.setText(_translate("form_buscadordocumentos", "Nombre"))
        item = self.tw_document.horizontalHeaderItem(2)
        item.setText(_translate("form_buscadordocumentos", "Fecha"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("form_buscadordocumentos", "Listado"))
        self.boton_descargar.setText(_translate("form_buscadordocumentos", "DESCARGAR"))
        self.label.setText(_translate("form_buscadordocumentos", "Seleccionado:"))

