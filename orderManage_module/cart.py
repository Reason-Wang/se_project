from Ui_cart import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from myUtils import *
class Cart(QMainWindow,Ui_MainWindow):#购物车页面
    def __init__(self,id_dict):
        super().__init__()
        self.num=len(id_dict)
        self.id_dict=id_dict
        self.setupUi(self)
        self.initTable()
        self.checkAll.stateChanged.connect(self.checkAll_changed)
    def show(self):
        super().show()

    def initTable(self):
        self.table.setColumnWidth(0,40)
        self.table.setColumnWidth(1,80)
        self.table.setRowCount(self.num)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.checkList = list()
        index=0
        for key in self.id_dict:
            self.checkList.append(QCheckBox())
            self.table.setCellWidget(index,0,self.checkList[index])
            self.checkList[index].stateChanged.connect(self.checkList_changed)
            info=execute_read_query(db_connect,"select name,price from merchan2 where id=%d"%(key))
            self.table.setItem(index,1,QTableWidgetItem(str(key)))
            self.table.setItem(index,2,QTableWidgetItem(str(info[0][0])))
            self.table.setItem(index,3,QTableWidgetItem(str(info[0][1])))
            self.table.setItem(index,4,QTableWidgetItem(str(self.id_dict[key])))
            for i in range(4):
                self.table.item(index,i+1).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
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

