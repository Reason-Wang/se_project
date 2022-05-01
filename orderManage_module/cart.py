# from ui_file.Ui_cart import Ui_MainWindow
# from ui_file.Ui_checkOrder2 import Ui_Form
from ui_file.Ui_cart_order import Ui_MainWindow
from ui_file.Ui_pay import Ui_Dialog
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from myUtils import db_operate
import functools
class Cart(QMainWindow,Ui_MainWindow):#购物车页面
    def __init__(self,cus_acc):
        super().__init__()
        self.db=db_operate("se","lbc","123456")
        self.account=cus_acc
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        self.returnCartBtn.setEnabled(False)
        self.initTable()
        self.checkAll.stateChanged.connect(self.checkAll_changed)
        self.checkOrderBtn.clicked.connect(self.checkOrderBtn_clicked)
        self.returnCartBtn.clicked.connect(self.returnCartBtn_clicked)
        self.payBtn.clicked.connect(self.payBtn_clicked)
        self.myOrderBtn.clicked.connect(self.myOrderBtn_clicked)
    def initTable(self):
        self.cart_dict=self.db.getCart(self.account)
        self.num=len(self.cart_dict)
        self.money=0
        self.table.clearContents()
        self.table.horizontalHeader().resizeSections(QHeaderView.ResizeToContents)
        #选中、id、商品名、单价、数量、操作
        self.table.setColumnWidth(0,40)
        self.table.setColumnWidth(1,60)
        self.table.setColumnWidth(2,100)
        self.table.setColumnWidth(3,80)
        self.table.setColumnWidth(4,80)
        self.table.setColumnWidth(5,80)
        self.table.setRowCount(self.num)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.checkBox_list = list()
        self.spList=list()
        self.deleteList=list()
        self.value_dict=dict()
        self.name_dict=dict()
        index=0
        for key in self.cart_dict:
            #设置每个商品的选中框，布局，激活函数
            self.checkBox_list.append(QCheckBox())
            hLayout = QHBoxLayout()
            hLayout.addWidget(self.checkBox_list[index])
            hLayout.setAlignment(self.checkBox_list[index], Qt.AlignCenter)
            hLayout.setContentsMargins(10, 0, 10, 0)
            widget = QWidget()
            widget.setLayout(hLayout)
            self.table.setCellWidget(index,0,widget)
            self.checkBox_list[index].stateChanged.connect(self.checkBox_list_changed)
            #获取数据库中相关信息并填表，布局
            info=self.db.getMerInfo(key)
            self.table.setItem(index,1,QTableWidgetItem(str(key)))#id
            self.table.setItem(index,2,QTableWidgetItem(info[0][0]))#商品名
            self.table.setItem(index,3,QTableWidgetItem("￥ "+str(info[0][1])))#单价
            self.name_dict[key]=info[0][0]
            self.value_dict[key]=info[0][1]
            for i in range(3):
                self.table.item(index,i+1).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            #设置商品个数，用spinbox实现手动调整
            self.spList.append(QSpinBox())
            self.spList[index].setValue(self.cart_dict[key])
            self.spList[index].setMinimum(1)
            self.spList[index].setMaximum(9)
            hLayout2=QHBoxLayout()
            hLayout2.addWidget(self.spList[index])
            hLayout2.setAlignment(self.spList[index], Qt.AlignCenter)
            hLayout2.setContentsMargins(10, 0, 10, 0)
            widget2 = QWidget()
            widget2.setLayout(hLayout2)
            self.table.setCellWidget(index,4,widget2)
            self.spList[index].valueChanged.connect(functools.partial(self.change_cart_dict,index))
            self.spList[index].valueChanged.connect(self.calculation_amount)
            #设置操作按钮
            self.deleteList.append(QPushButton("删除"))
            hLayout3=QHBoxLayout()
            hLayout3.addWidget(self.deleteList[index])
            hLayout3.setAlignment(self.deleteList[index], Qt.AlignCenter)
            hLayout3.setContentsMargins(10, 0, 10, 0)
            widget3 = QWidget()
            widget3.setLayout(hLayout3)
            self.table.setCellWidget(index,5,widget3)
            self.deleteList[index].clicked.connect(functools.partial(self.delete_clicked,index))
            index+=1
        self.calculation_amount()
    def checkBox_list_changed(self):
        self.calculation_amount()
        self.checkAll.blockSignals(True)
        index=0
        while(index<self.num):
            if(not self.checkBox_list[index].isChecked()):
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
                self.checkBox_list[index].setChecked(True)
                index+=1
        else:
            index=0
            while(index<self.num):
                self.checkBox_list[index].setChecked(False)
                index+=1
    def calculation_amount(self):
        self.checkOrderBtn.setEnabled(False)
        self.mer_dict=dict()
        index=0
        self.money=0
        for key,value in self.cart_dict.items():
            if(self.checkBox_list[index].isChecked()):
                self.money+=self.value_dict[key]*value
                self.mer_dict[key]=value
                self.checkOrderBtn.setEnabled(True)
            index+=1
        self.moneyLabel.setText("总金额:￥"+str(self.money))
        self.moneyLabel.adjustSize()
    def delete_clicked(self,index):
        reply=QMessageBox.question(self,"Message","您确认要删除该商品吗？",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            #deleteKey=int(self.table.item(index,1).text())#id
            del self.cart_dict[tuple(self.cart_dict)[index]]
            self.db.changeCart(self.account,self.cart_dict)
            self.initTable()
        else:
            return
    def change_cart_dict(self,index):
        key=tuple(self.cart_dict)[index]
        #key=int(self.table.item(index,1).text())
        value=self.spList[index].value()
        self.cart_dict[key]=value
    def closeEvent(self,event):
        reply = QMessageBox.question(self, 'Message',
            "确认退出?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.db.changeCart(self.account,self.cart_dict)
            event.accept()
        else:
            event.ignore()
    def init_con_info(self):
        con_info=self.db.getCusInfo(self.account)
        self.con_table.setColumnWidth(0,100)
        self.con_table.setColumnWidth(1,180)
        self.con_table.horizontalHeader().setStretchLastSection(True)
        self.con_table.setRowCount(1)
        for i in range(3):
            self.con_table.setItem(0,i,QTableWidgetItem(con_info[i]))
            self.con_table.item(0,i).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    def init_mer_info(self):
        self.mer_table.setRowCount(len(self.mer_dict))
        self.mer_table.horizontalHeader().resizeSections(QHeaderView.ResizeToContents)
        self.mer_table.setColumnWidth(0,180)
        self.mer_table.setColumnWidth(1,80)
        self.mer_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        index=0
        for key,value in self.mer_dict.items():
            #print(i)
            self.mer_table.setItem(index,0,QTableWidgetItem(self.name_dict[key]))#商品名
            self.mer_table.setItem(index,1,QTableWidgetItem("￥ "+str(self.value_dict[key])))#单价
            self.mer_table.setItem(index,2,QTableWidgetItem(str(value)))#购买数量
            for i in range(3):
                self.mer_table.item(index,i).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            index+=1

    def checkOrderBtn_clicked(self):
        self.returnCartBtn.setEnabled(True)
        self.init_con_info()
        self.init_mer_info()
        self.moneyLabel2.setText("总金额:￥"+str(self.money))
        self.moneyLabel2.adjustSize()
        self.stackedWidget.setCurrentIndex(1)
    def returnCartBtn_clicked(self):
        self.returnCartBtn.setEnabled(False)
        self.myOrderBtn.setEnabled(True)
        self.stackedWidget.setCurrentIndex(0)
    def payBtn_clicked(self):
        payWidget=Pay(self.money)
        returnCode=payWidget.exec()
        if(returnCode):
            self.stackedWidget.setCurrentIndex(2)
        pass
    def myOrderBtn_clicked(self):
        self.returnCartBtn.setEnabled(True)
        self.myOrderBtn.setEnabled(False)
        self.stackedWidget.setCurrentIndex(2)
        self.topFiller=QWidget()
        self.topFiller.setMinimumSize(250, 2000)
        #self.test=list()
        for index in range(20):
            # self.test.append(QPushButton(self.topFiller))
            # self.test[index].setText(str(index))
            # self.test[index].move(10,index*40)
            self.test=QPushButton(self.topFiller)
            self.test.setText(str(index))
            self.test.move(10,index*40)
        self.scrollArea.setWidget(self.topFiller)
class Pay(QDialog,Ui_Dialog):
    def __init__(self,money):
        super().__init__()
        self.setupUi(self)
        self.money_label.setText("￥ "+str(money))
        self.money_label.setAlignment(Qt.AlignCenter)
        self.money_label.setFont(QFont("Roman times",28,QFont.Bold))
        self.confirmBtn.clicked.connect(self.accept)
        self.cancelBtn.clicked.connect(self.reject)

