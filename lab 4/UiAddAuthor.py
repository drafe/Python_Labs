# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiAddAuthor.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(524, 335)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line_author = QtWidgets.QLineEdit(self.centralwidget)
        self.line_author.setObjectName("line_author")
        self.verticalLayout.addWidget(self.line_author)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.line_country = QtWidgets.QLineEdit(self.centralwidget)
        self.line_country.setObjectName("line_country")
        self.verticalLayout.addWidget(self.line_country)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.line_years = QtWidgets.QLineEdit(self.centralwidget)
        self.line_years.setObjectName("line_years")
        self.verticalLayout.addWidget(self.line_years)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.button_add = QtWidgets.QPushButton(self.centralwidget)
        self.button_add.setMinimumSize(QtCore.QSize(150, 70))
        self.button_add.setObjectName("button_add")
        self.verticalLayout_2.addWidget(self.button_add)
        self.button_close = QtWidgets.QPushButton(self.centralwidget)
        self.button_close.setMinimumSize(QtCore.QSize(150, 70))
        self.button_close.setObjectName("button_close")
        self.verticalLayout_2.addWidget(self.button_close)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Добавить автора"))
        self.label.setText(_translate("MainWindow", "Имя и фамилия автора"))
        self.label_2.setText(_translate("MainWindow", "Страна"))
        self.label_3.setText(_translate("MainWindow", "Годы жизни"))
        self.button_add.setText(_translate("MainWindow", "Добавить автора"))
        self.button_close.setText(_translate("MainWindow", "Закрыть окно"))
