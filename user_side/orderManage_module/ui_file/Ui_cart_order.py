# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\11487\Desktop\code\se_project\orderManage_module\ui_file\cart_order.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 614)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(150, -1, 150, -1)
        self.horizontalLayout.setSpacing(150)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.returnCartBtn = QtWidgets.QPushButton(self.centralwidget)
        self.returnCartBtn.setMinimumSize(QtCore.QSize(0, 50))
        self.returnCartBtn.setObjectName("returnCartBtn")
        self.horizontalLayout.addWidget(self.returnCartBtn)
        self.myOrderBtn = QtWidgets.QPushButton(self.centralwidget)
        self.myOrderBtn.setMinimumSize(QtCore.QSize(0, 50))
        self.myOrderBtn.setObjectName("myOrderBtn")
        self.horizontalLayout.addWidget(self.myOrderBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table = QtWidgets.QTableWidget(self.page)
        self.table.setEnabled(True)
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
        self.verticalLayout.addWidget(self.table)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, 50, -1)
        self.horizontalLayout_2.setSpacing(150)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkAll = QtWidgets.QCheckBox(self.page)
        self.checkAll.setObjectName("checkAll")
        self.horizontalLayout_2.addWidget(self.checkAll)
        self.moneyLabel = QtWidgets.QLabel(self.page)
        self.moneyLabel.setObjectName("moneyLabel")
        self.horizontalLayout_2.addWidget(self.moneyLabel)
        self.checkOrderBtn = QtWidgets.QPushButton(self.page)
        self.checkOrderBtn.setMinimumSize(QtCore.QSize(0, 50))
        self.checkOrderBtn.setObjectName("checkOrderBtn")
        self.horizontalLayout_2.addWidget(self.checkOrderBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.con_table = QtWidgets.QTableWidget(self.page_2)
        self.con_table.setObjectName("con_table")
        self.con_table.setColumnCount(5)
        self.con_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.con_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.con_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.con_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.con_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.con_table.setHorizontalHeaderItem(4, item)
        self.verticalLayout_5.addWidget(self.con_table)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.mer_table = QtWidgets.QTableWidget(self.page_2)
        self.mer_table.setMinimumSize(QtCore.QSize(399, 287))
        self.mer_table.setObjectName("mer_table")
        self.mer_table.setColumnCount(3)
        self.mer_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.mer_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.mer_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.mer_table.setHorizontalHeaderItem(2, item)
        self.verticalLayout_4.addWidget(self.mer_table)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.methodBox = QtWidgets.QComboBox(self.page_2)
        self.methodBox.setMinimumSize(QtCore.QSize(150, 40))
        self.methodBox.setObjectName("methodBox")
        self.methodBox.addItem("")
        self.methodBox.addItem("")
        self.horizontalLayout_3.addWidget(self.methodBox)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.moneyLabel2 = QtWidgets.QLabel(self.page_2)
        self.moneyLabel2.setMinimumSize(QtCore.QSize(150, 30))
        self.moneyLabel2.setMaximumSize(QtCore.QSize(150, 30))
        self.moneyLabel2.setObjectName("moneyLabel2")
        self.horizontalLayout_4.addWidget(self.moneyLabel2)
        self.payBtn = QtWidgets.QPushButton(self.page_2)
        self.payBtn.setMinimumSize(QtCore.QSize(120, 50))
        self.payBtn.setMaximumSize(QtCore.QSize(120, 16777215))
        self.payBtn.setObjectName("payBtn")
        self.horizontalLayout_4.addWidget(self.payBtn)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.page_3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.history_table = QtWidgets.QTableWidget(self.page_3)
        self.history_table.setObjectName("history_table")
        self.history_table.setColumnCount(5)
        self.history_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.history_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.history_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.history_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.history_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.history_table.setHorizontalHeaderItem(4, item)
        self.history_table.verticalHeader().setMinimumSectionSize(37)
        self.horizontalLayout_7.addWidget(self.history_table)
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.returnCartBtn.setText(_translate("MainWindow", "购物车"))
        self.myOrderBtn.setText(_translate("MainWindow", "我的订单"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "选中"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "商品图片"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "商品名"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "单价"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "购买数量"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "操作"))
        self.checkAll.setText(_translate("MainWindow", "全选"))
        self.moneyLabel.setText(_translate("MainWindow", "TextLabel"))
        self.checkOrderBtn.setText(_translate("MainWindow", "确认订单"))
        self.label_3.setText(_translate("MainWindow", "请完善订单信息"))
        self.label.setText(_translate("MainWindow", "选择收货人信息："))
        item = self.con_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "选择"))
        item = self.con_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.con_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "联系方式"))
        item = self.con_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "地址信息"))
        item = self.con_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "操作"))
        self.label_4.setText(_translate("MainWindow", "商品清单："))
        item = self.mer_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "商品名"))
        item = self.mer_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "单价"))
        item = self.mer_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "购买数量"))
        self.label_2.setText(_translate("MainWindow", "取货方式："))
        self.methodBox.setItemText(0, _translate("MainWindow", "超市配送"))
        self.methodBox.setItemText(1, _translate("MainWindow", "自行取货"))
        self.moneyLabel2.setText(_translate("MainWindow", "TextLabel"))
        self.payBtn.setText(_translate("MainWindow", "确认支付"))
        item = self.history_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "订单状态"))
        item = self.history_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "商品图片"))
        item = self.history_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "商品名"))
        item = self.history_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "商品数量"))
        item = self.history_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "操作"))
