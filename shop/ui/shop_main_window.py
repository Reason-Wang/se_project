# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/shop_main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_shop_main(object):
    def setupUi(self, shop_main):
        shop_main.setObjectName("shop_main")
        shop_main.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(shop_main)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 10, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(230, 100, 321, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.shop_info = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.shop_info.setFont(font)
        self.shop_info.setObjectName("shop_info")
        self.verticalLayout.addWidget(self.shop_info)
        shop_main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(shop_main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        shop_main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(shop_main)
        self.statusbar.setObjectName("statusbar")
        shop_main.setStatusBar(self.statusbar)

        self.retranslateUi(shop_main)
        QtCore.QMetaObject.connectSlotsByName(shop_main)

    def retranslateUi(self, shop_main):
        _translate = QtCore.QCoreApplication.translate
        shop_main.setWindowTitle(_translate("shop_main", "购物商城商家端"))
        self.label.setText(_translate("shop_main", "购物商城商家端"))

        self.shop_info.setText(_translate("shop_main", "店铺信息"))
