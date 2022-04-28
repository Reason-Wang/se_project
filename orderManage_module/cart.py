from tabnanny import check
from Ui_cart import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Cart(QMainWindow,Ui_MainWindow):
    def __init__(self,num):
        super().__init__()
        self.num=num
        self.setupUi(self)
        #self.btn_add.clicked.connect(self.btn_add_clicked)
        self.initTable()
        self.checkAll.stateChanged.connect(self.checkAll_changed)
    def show(self):
        super().show()
    def initTable(self):
        self.table.setColumnWidth(0,40)
        self.table.setRowCount(self.num)
        self.checkList = list()
        index=0
        while(index<self.num):
            self.checkList.append(QCheckBox())
            self.table.setCellWidget(index,0,self.checkList[index])
            self.checkList[index].stateChanged.connect(self.checkList_changed)
            index+=1
    def checkList_changed(self):
        self.checkAll.blockSignals(True)
        index=0
        while(index<self.num):
            if(not self.checkList[index].isChecked()):
                self.checkAll.setChecked(False)
                self.checkAll.blockSignals(False)
                return
            index+=1
        self.checkAll.setChecked(True)
        self.checkAll.blockSignals(False)
    def checkAll_changed(self):
        if(self.checkAll.isChecked()):
            index=0
            while(index<self.num):
                self.checkList[index].setChecked(True)
                index+=1
        else:
            index=0
            while(index<self.num):
                self.checkList[index].setChecked(False)
                index+=1

