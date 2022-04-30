# from ui_file.Ui_cart import Ui_MainWindow
# from ui_file.Ui_checkOrder2 import Ui_Form
from ui_file.Ui_cart_order import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from myUtils import *
import functools
class Cart(QMainWindow,Ui_MainWindow):#购物车页面
    def __init__(self,cus_acc):
        super().__init__()
        self.account=cus_acc
        self.setupUi(self)
        #self.stackedWidget.setCurrentWidget(0)
        self.initTable()
        self.checkAll.stateChanged.connect(self.checkAll_changed)
        self.checkOrderBtn.clicked.connect(self.checkOrderBtn_clicked)
        self.returnCartBtn.clicked.connect(self.returnCartBtn_clicked)
    # def show(self):
    #     super().show()

    def initTable(self):
        self.id_dict=getCart(self.account)
        self.num=len(self.id_dict)
        self.total=0
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
        index=0
        for key in self.id_dict:
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
            info=execute_read_query(db_connect,"select name,price from merchan2 where id=%d"%(key))
            self.table.setItem(index,1,QTableWidgetItem(str(key)))#id
            self.table.setItem(index,2,QTableWidgetItem(str(info[0][0])))#商品名
            self.table.setItem(index,3,QTableWidgetItem("￥ "+str(info[0][1])))#单价
            for i in range(3):
                self.table.item(index,i+1).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            #设置商品个数，用spinbox实现手动调整
            self.spList.append(QSpinBox())
            self.spList[index].setValue(self.id_dict[key])
            self.spList[index].setMinimum(1)
            self.spList[index].setMaximum(9)
            hLayout2=QHBoxLayout()
            hLayout2.addWidget(self.spList[index])
            hLayout2.setAlignment(self.spList[index], Qt.AlignCenter)
            hLayout2.setContentsMargins(10, 0, 10, 0)
            widget2 = QWidget()
            widget2.setLayout(hLayout2)
            self.table.setCellWidget(index,4,widget2)
            self.spList[index].valueChanged.connect(self.calculation_amount)
            self.spList[index].valueChanged.connect(functools.partial(self.change_id_dict,index))
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
        index=0
        self.total=0
        while(index<self.num):
            if(self.checkBox_list[index].isChecked()):
                self.total+=float(self.table.item(index,3).text()[2:])*self.spList[index].value()
            index+=1
        self.totalLabel.setText("总金额:￥"+str(self.total))
        self.totalLabel.adjustSize()
    def delete_clicked(self,index):
        reply=QMessageBox.question(self,"Message","您确认要删除该商品吗？",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            deleteKey=int(self.table.item(index,1).text())#id
            deleteCart(self.account,deleteKey)
            self.initTable()
        else:
            return
    def change_id_dict(self,index):
        key=int(self.table.item(index,1).text())
        value=self.spList[index].value()
        self.id_dict[key]=value
    def closeEvent(self,event):
        reply = QMessageBox.question(self, 'Message',
            "确认退出?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            changeCart(self.account,self.id_dict)
            event.accept()
        else:
            event.ignore()
    def checkOrderBtn_clicked(self):
        self.stackedWidget.setCurrentIndex(1)
    def returnCartBtn_clicked(self):
        self.stackedWidget.setCurrentIndex(0)

# class CheckOrder(QWidget,Ui_Form):
#     def __init__(self,cus_acc,id_dict):
#         super().__init__()
#         self.setupUi(self)
#     # def exec(self):
#     #     super.exec()
#     # def show(self):
#     #     super().show()

