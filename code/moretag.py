# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow-untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *
from outshow_rc import myshowout,addcart

class MyQLabel(QLabel):
    # 自定义信号, 注意信号必须为类属性
    button_clicked_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(MyQLabel, self).__init__(parent)

    def mouseReleaseEvent(self, QMouseEvent):
        self.button_clicked_signal.emit()

    # 可在外部与槽函数连接
    def connect_customized_slot(self, func):
        self.button_clicked_signal.connect(func)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 900)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 20, 700, 800))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QWidget()
        self.page.setObjectName("page")
        self.searchEdit = QLineEdit(self.page)
        self.searchEdit.setObjectName("lineEdit")
        self.searchlabel = MyQLabel(self.page)
        self.searchlabel.setObjectName("label")
        self.showbar =myshowout(self.page)
        self.showbar.setObjectName("label_2")
        self.searchbutton = QtWidgets.QPushButton()
        self.searchbutton.setObjectName("checkOrderBtn")
        self.prePage = QPushButton(self.page)
        self.prePage.setObjectName("PREPAGE")
        self.curPage = MyQLabel(self.page)
        self.curPage.setObjectName("CURPAGE")
        self.nextPage = QPushButton(self.page)
        self.nextPage.setObjectName("NEXTPAGE")
        self.totalPage = MyQLabel(self.page)
        self.totalPage.setObjectName("totalPage")
        self.skipLable_0 = MyQLabel(self.page)
        self.skipLable_0.setObjectName("skipLable_0")
        self.skipPage = QLineEdit(self.page)
        self.skipPage.setObjectName("SKIPPAGE")
        self.skipLabel_1 = MyQLabel(self.page)
        self.skipLabel_1.setObjectName("skipLable_1")
        self.confirmSkip = QPushButton(self.page)
        self.confirmSkip.setObjectName("confirmSkip")
        self.page.hbox1 = QHBoxLayout()
        self.page.hbox6 = QHBoxLayout()
        self.page.vbox1 = QVBoxLayout()
        self.page.hbox1.setContentsMargins(11, 11, 11, 11)
        self.page.hbox6.setContentsMargins(11, 11, 11, 11)
        self.showbar.setContentsMargins(11,11,11,11)
        self.page.hbox1.addWidget(self.searchlabel)
        self.page.hbox1.addWidget(self.searchEdit)
        self.page.hbox1.addWidget(self.searchbutton)
        self.page.hbox6.addWidget(self.prePage)
        self.page.hbox6.addWidget(self.curPage)
        self.page.hbox6.addWidget(self.nextPage)
        self.page.hbox6.addWidget(self.totalPage)
        self.page.hbox6.addWidget(self.skipLable_0)
        self.page.hbox6.addWidget(self.skipPage)
        self.page.hbox6.addWidget(self.skipLabel_1)
        self.page.hbox6.addWidget(self.confirmSkip)
        self.page.vbox1.addLayout(self.page.hbox1)
        self.page.vbox1.addWidget(self.showbar)
        self.page.vbox1.addLayout(self.page.hbox6)
        self.page.setLayout(self.page.vbox1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.grid=QGridLayout(self.page_2)
        self.page_2.setLayout(self.grid)
        self.tiplabel=MyQLabel(self.page_2)
        self.tiplabel.setText("全部分类")
        self.page_2.setObjectName("page_2")
        font = QtGui.QFont()
        font.setFamily("BIZ UDGothic")
        font.setPointSize(16)
        font.setBold(True)
        self.tiplabel.setFont(font)
        self.grid.setContentsMargins(11, 11, 11, 600)
        self.grid.addWidget(self.tiplabel,0,2)
        self.tiplabel.show()
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.seemer=addcart(self.page_3)
        Vbox2=QVBoxLayout()
        Vbox2.addWidget(self.seemer)
        self.page_3.setLayout(Vbox2)
        self.stackedWidget.addWidget(self.page_3)
        self.mything = QtWidgets.QPushButton(self.centralwidget)
        self.mything .setGeometry(QtCore.QRect(500, 840, 93, 28))
        self.mything .setObjectName("pushButton_4")
        self.homepage  = QtWidgets.QPushButton(self.centralwidget)
        self.homepage .setGeometry(QtCore.QRect(100, 840, 93, 28))
        self.homepage .setObjectName("pushButton_5")
        self.mycart = QtWidgets.QPushButton(self.centralwidget)
        self.mycart.setGeometry(QtCore.QRect(300, 840, 93, 28))
        self.mycart.setObjectName("pushButton_6")
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
        self.searchlabel.setText(_translate("MainWindow", ""))
        self.showbar.tag1.setText(_translate("MainWindow", "零食"))
        self.showbar.tag2.setText(_translate("MainWindow", "水果"))
        self.showbar.tag3.setText(_translate("MainWindow", "生活用品"))
        self.showbar.tag4.setText(_translate("MainWindow", "饮品"))
        self.showbar.tag5.setText(_translate("MainWindow", "所有分类"))
        self.showbar.tag6.setText(_translate("MainWindow", "全部商品"))
        self.prePage.setText(_translate("MainWindow", "<上一页"))
        self.curPage.setText(_translate("MainWindow", "1"))
        self.nextPage.setText(_translate("MainWindow", "下一页>"))
        self.skipLable_0.setText(_translate("MainWindow", "跳到"))
        self.skipLabel_1.setText(_translate("MainWindow", "页"))
        self.totalPage.setText(_translate("MainWindow", "共1页"))
        self.searchbutton.setText(_translate("MainWindow", "搜索"))
        self.skipPage.setValidator(QIntValidator())
        self.confirmSkip.setText(_translate("MainWindow", "确定"))
        self.homepage.setText(_translate("MainWindow", "返回首页"))
        self.mycart.setText(_translate("MainWindow", "购物车"))
        self.mything.setText(_translate("MainWindow", "我的"))
        self.seemer.addbutton.setText(_translate("MainWindow", "加入购物车"))
        self.seemer.returnpage.setText(_translate("MainWindow","返回"))