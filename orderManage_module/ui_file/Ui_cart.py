# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\11487\Desktop\code\se_project\orderManage_module\cart.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkAll = QtWidgets.QCheckBox(self.centralwidget)
        self.checkAll.setGeometry(QtCore.QRect(560, 20, 61, 19))
        self.checkAll.setObjectName("checkAll")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(30, 10, 499, 529))
        self.table.setObjectName("table")
        self.table.setColumnCount(6)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        self.totalLabel = QtWidgets.QLabel(self.centralwidget)
        self.totalLabel.setGeometry(QtCore.QRect(560, 100, 71, 31))
        self.totalLabel.setObjectName("totalLabel")
        self.checkBtn = QtWidgets.QPushButton(self.centralwidget)
        self.checkBtn.setGeometry(QtCore.QRect(570, 200, 93, 28))
        self.checkBtn.setObjectName("checkBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.checkAll.setText(_translate("MainWindow", "全选"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "选中"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "商品id"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "商品名"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "单价"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "购买数量"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "操作"))
        self.totalLabel.setText(_translate("MainWindow", "TextLabel"))
        self.checkBtn.setText(_translate("MainWindow", "确认订单"))