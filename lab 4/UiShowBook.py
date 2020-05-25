# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiShowBook.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(512, 373)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_auth_id = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_auth_id.setFont(font)
        self.label_auth_id.setObjectName("label_auth_id")
        self.verticalLayout_2.addWidget(self.label_auth_id)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.verticalLayout_2.addWidget(self.label_name)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_pages = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_pages.setFont(font)
        self.label_pages.setObjectName("label_pages")
        self.verticalLayout_2.addWidget(self.label_pages)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_publisher = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_publisher.setFont(font)
        self.label_publisher.setObjectName("label_publisher")
        self.verticalLayout_2.addWidget(self.label_publisher)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.label_years = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_years.setFont(font)
        self.label_years.setObjectName("label_years")
        self.verticalLayout_2.addWidget(self.label_years)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_save_xml = QtWidgets.QPushButton(self.centralwidget)
        self.button_save_xml.setMinimumSize(QtCore.QSize(150, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_save_xml.setFont(font)
        self.button_save_xml.setObjectName("button_save_xml")
        self.verticalLayout.addWidget(self.button_save_xml)
        self.button_save_json = QtWidgets.QPushButton(self.centralwidget)
        self.button_save_json.setMinimumSize(QtCore.QSize(150, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_save_json.setFont(font)
        self.button_save_json.setObjectName("button_save_json")
        self.verticalLayout.addWidget(self.button_save_json)
        self.button_close = QtWidgets.QPushButton(self.centralwidget)
        self.button_close.setMinimumSize(QtCore.QSize(150, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_close.setFont(font)
        self.button_close.setObjectName("button_close")
        self.verticalLayout.addWidget(self.button_close)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Информация о книге"))
        self.label.setText(_translate("MainWindow", "ID автора"))
        self.label_auth_id.setText(_translate("MainWindow", "1"))
        self.label_3.setText(_translate("MainWindow", "Название книги"))
        self.label_name.setText(_translate("MainWindow", "2"))
        self.label_5.setText(_translate("MainWindow", "Количество страниц"))
        self.label_pages.setText(_translate("MainWindow", "3"))
        self.label_6.setText(_translate("MainWindow", "Издательство"))
        self.label_publisher.setText(_translate("MainWindow", "4"))
        self.label_10.setText(_translate("MainWindow", "Годы публикации"))
        self.label_years.setText(_translate("MainWindow", "5"))
        self.button_save_xml.setText(_translate("MainWindow", "Сохранить в .xml"))
        self.button_save_json.setText(_translate("MainWindow", "Сохранить в .json"))
        self.button_close.setText(_translate("MainWindow", "Закрыть окно"))