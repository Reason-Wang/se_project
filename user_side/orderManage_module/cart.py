# from ui_file.Ui_cart import Ui_MainWindow
# from ui_file.Ui_checkOrder2 import Ui_Form
import functools,sys,os,datetime
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)))
sys.path.append(os.path.dirname(__file__))
from ui_file.Ui_cart_order import Ui_MainWindow
from ui_file.Ui_pay import Ui_Dialog
from ui_file.Ui_detail import Ui_Form
from ui_file.Ui_input import Ui_Dialog as Ui_input
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from myUtils import db_operate,OrderItem
from PIL import Image,ImageQt
from io import BytesIO
class Cart(QMainWindow,Ui_MainWindow):#购物车页面
    def __init__(self):
        super().__init__()
        self.db=db_operate("se","lbc","123456")
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        self.returnCartBtn.setEnabled(False)
        self.checkAll.stateChanged.connect(self.checkAll_changed)
        self.checkOrderBtn.clicked.connect(self.checkOrderBtn_clicked)
        self.returnCartBtn.clicked.connect(self.returnCartBtn_clicked)
        self.payBtn.clicked.connect(self.payBtn_clicked)
        self.myOrderBtn.clicked.connect(self.myOrderBtn_clicked)
    def show(self):
        self.initAll()
        super(Cart, self).show()
    def initAll(self):
        self.initTable()
        self.init_history_table()
    def changeAccount(self,account):
        self.account=account
    def initTable(self):
        self.cart_dict=self.db.getCart(self.account)
        self.num=len(self.cart_dict)
        self.money=0
        self.table.clearContents()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        #选中、id、商品名、单价、数量、操作
        # self.table.setColumnWidth(0,40)
        # self.table.setColumnWidth(1,60)
        # self.table.setColumnWidth(2,100)
        # self.table.setColumnWidth(3,80)
        # self.table.setColumnWidth(4,80)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setRowCount(self.num)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.checkBox_list = list()
        self.spList=list()
        #self.deleteList=list()
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
            path=self.db.getMerPictureData(info[0][2])
            picture=createPictureLabel(path)
            # picture=QLabel()
            # picture.resize(200,200)
            # data=self.db.getMerPictureData(info[0][2])
            # if(data=="null"):
            #     picture.setText("图片不存在")
            # else:
            #     pixmap=ImageQt.toqpixmap(Image.open(BytesIO(data)))
            #     pixmap=pixmap.scaled(picture.width(),picture.height())
            #     picture.setPixmap(pixmap)
            
            #self.table.setItem(index,1,QTableWidgetItem(str(key)))#id
            self.table.setCellWidget(index,1,picture)
            self.table.setItem(index,2,QTableWidgetItem(info[0][0]))#商品名
            self.table.setItem(index,3,QTableWidgetItem("￥ "+str(info[0][1])))#单价
            self.name_dict[key]=info[0][0]
            self.value_dict[key]=info[0][1]
            for i in range(2):
                self.table.item(index,i+2).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            #设置商品个数，用spinbox实现手动调整
            self.spList.append(QSpinBox())
            self.spList[index].setValue(self.cart_dict[key])
            self.spList[index].setMinimum(1)
            self.spList[index].setMaximum(99)
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
            #self.deleteList.append(QPushButton("删除"))
            self.deleteBtn=QPushButton("删除")
            hLayout3=QHBoxLayout()
            hLayout3.addWidget(self.deleteBtn)
            hLayout3.setAlignment(self.deleteBtn, Qt.AlignCenter)
            hLayout3.setContentsMargins(10, 0, 10, 0)
            widget3 = QWidget()
            widget3.setLayout(hLayout3)
            self.table.setCellWidget(index,5,widget3)
            self.deleteBtn.clicked.connect(functools.partial(self.delete_clicked,index))
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
                #print(self.value_dict[key],value)
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
    def delete_bought(self):
        for id in self.mer_dict:
            del self.cart_dict[id]
        self.db.changeCart(self.account,self.cart_dict)
        self.initTable()
    def change_cart_dict(self,index):
        key=tuple(self.cart_dict)[index]
        #key=int(self.table.item(index,1).text())
        value=self.spList[index].value()
        self.cart_dict[key]=value
    def closeEvent(self,event):
        self.db.changeCart(self.account,self.cart_dict)
        #self.db.close()
        # reply = QMessageBox.question(self, 'Message',
        #     "确认退出?", QMessageBox.Yes | 
        #     QMessageBox.No, QMessageBox.No)

        # if reply == QMessageBox.Yes:
        #     self.db.changeCart(self.account,self.cart_dict)
        #     self.db.close()
        #     event.accept()
        # else:
        #     event.ignore()
    def init_con_info(self):
        # con_info=self.db.getCusInfo(self.account)
        # self.con_table.setColumnWidth(0,100)
        # self.con_table.setColumnWidth(1,180)
        # self.con_table.horizontalHeader().setStretchLastSection(True)
        # self.con_table.setRowCount(1)
        # for i in range(3):
        #     self.con_table.setItem(0,i,QTableWidgetItem(con_info[i]))
        #     self.con_table.item(0,i).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.con_info_dict=self.db.get_con_info_dict(self.account)
        if(len(self.con_info_dict)==0):
            self.con_info_dict[0]=self.db.getCusInfo(self.account)
            self.db.addCus_con_info(self.account,self.con_info_dict[0],0)
        self.con_table.setColumnWidth(0,100)
        self.con_table.setColumnWidth(1,180)
        self.con_table.horizontalHeader().setStretchLastSection(True)
        self.con_table.verticalHeader().setHidden(True)
        self.con_table.setRowCount(len(self.con_info_dict))
        self.con_table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.con_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.select_list=list()
        #print(sorted(self.con_info_dict.items()))
        for con_seq,con_info in sorted(self.con_info_dict.items()):
            self.select_list.append(QCheckBox())
            #print(con_seq)
            self.select_list[-1].stateChanged.connect(functools.partial(self.select_list_changed,con_seq))
            hLayout = QHBoxLayout()
            hLayout.addWidget(self.select_list[-1])
            hLayout.setAlignment(self.select_list[-1], Qt.AlignCenter)
            hLayout.setContentsMargins(10, 0, 10, 0)
            widget = QWidget()
            widget.setLayout(hLayout)
            self.con_table.setCellWidget(con_seq,0,widget)
            for i in range(3):
                self.con_table.setItem(con_seq,i+1,QTableWidgetItem(str(con_info[i])))
                self.con_table.item(con_seq,i+1).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            if(con_seq==0):
                addBtn=QPushButton("添加")
                addBtn.clicked.connect(self.addBtn_con_clicked)
                hLayout3 = QHBoxLayout()
                hLayout3.addWidget(addBtn)
                hLayout3.setAlignment(addBtn, Qt.AlignCenter)
                hLayout3.setContentsMargins(10, 0, 10, 0)
                widget3 = QWidget()
                widget3.setLayout(hLayout3)
                self.con_table.setCellWidget(con_seq,4,widget3)
            else:
                changeBtn=QPushButton("修改")
                changeBtn.clicked.connect(functools.partial(self.change_con_clicked,con_seq))
                deleteBtn=QPushButton("删除")
                deleteBtn.clicked.connect(functools.partial(self.delete_con_clicked,con_seq))
                hLayout2=QHBoxLayout()
                hLayout2.addWidget(changeBtn)
                hLayout2.addWidget(deleteBtn)
                widget2 = QWidget()
                widget2.setLayout(hLayout2)
                self.con_table.setCellWidget(con_seq,4,widget2)
        self.select_list[0].blockSignals(True)
        self.select_list[0].setChecked(True)
        self.select_list[0].blockSignals(False)
        self.con_info=self.con_info_dict[0]
        #print(len(self.select_list))
    def select_list_changed(self,index):
        if(self.select_list[index].isChecked()):
            for i in range(len(self.select_list)):
                if not (i==index):
                    self.select_list[i].setChecked(False)
            self.con_info=self.con_info_dict[index]
            #print(self.con_info)
    def addBtn_con_clicked(self):
        self.addWidget=InputWidget()
        self.addWidget.confirmBtn.clicked.connect(self.getConInfo) 
        returnCode=self.addWidget.exec()
        if returnCode:
            n=len(self.con_info_dict)
            self.con_info=(self.addWidget.nameEdit.text()[0:30],self.addWidget.phoneEdit.text()[0:20],self.addWidget.addrEdit.text()[0:50])
            self.con_info_dict[n]=self.con_info
            self.db.addCus_con_info(self.account,self.con_info,n)
            self.init_con_info()
    def getConInfo(self):
        self.con_info=(self.addWidget.nameEdit.text(),self.addWidget.phoneEdit.text(),self.addWidget.addrEdit.text())
    def change_con_clicked(self,index):
        self.changeWidget=InputWidget(self.con_info_dict[index])
        #self.changeWidget.confirmBtn.clicked.connect(self.getConInfo)
        returnCode=self.changeWidget.exec()
        if returnCode:
            self.con_info=(self.changeWidget.nameEdit.text()[0:20],self.changeWidget.phoneEdit.text()[0:20],self.changeWidget.addrEdit.text()[0:50])
            self.con_info_dict[index]=self.con_info
            self.db.changeCus_con_info(self.account,self.con_info,index)
            self.init_con_info()
    def delete_con_clicked(self,index):
        self.db.deleteCus_con_info(self.account,index,len(self.con_info_dict))
        self.init_con_info()
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
    def init_history_table(self):
        self.history_table.clearContents()
        self.history_table.setRowCount(0)
        self.order_dict=self.db.getOrderHistory(self.account)
        history_row=0
        for value in self.order_dict.values():
            history_row+=value.num
        self.history_table.setRowCount(history_row)
        self.history_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.history_table.verticalHeader().setHidden(True)
        self.history_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.history_table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        index_order=0
        index_mer=0
        for order_id,order_value in sorted(self.order_dict.items(),reverse=True):#订单id，订单类
            if(order_value.num>1):
                self.history_table.setSpan(index_order,0,order_value.num,1)
                self.history_table.setSpan(index_order,4,order_value.num,1)
            self.history_table.setItem(index_order,0,QTableWidgetItem("总金额 ￥"+str(order_value.total)+"\n\n"+order_value.status+"\n\n"+str(order_value.date)))
            self.history_table.item(index_order,0).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.orderBtns=OrderOperate(order_value.status)
            self.history_table.setCellWidget(index_order,4,self.orderBtns)
            self.orderBtns.viewBtn.clicked.connect(functools.partial(self.viewDetailBtn_clicked,order_id))
            if order_value.status=="未付款":
                self.orderBtns.payBtn.clicked.connect(functools.partial(self.payBtn_clicked,order_id))
                self.orderBtns.cancelBtn.clicked.connect(functools.partial(self.cancel_order,order_id))
            if order_value.status=="已付款" or order_value.status=="已准备":
                self.orderBtns.refundBtn.clicked.connect(functools.partial(self.refund_order,order_id))
            if order_value.status=="已准备" or order_value.status=="已发货":
                self.orderBtns.finishBtn.clicked.connect(functools.partial(self.finish_order,order_id))
            for mer_key,mer_value in order_value.mer_dict.items():#商品id,购买数量
                mer_info=self.db.getMerInfo(mer_key)
                #print(111111111111111)
                data=self.db.getMerPictureData(mer_info[0][2])
                picture=createPictureLabel(data)
                self.history_table.setCellWidget(index_mer,1,picture)
                #self.history_table.setItem(index_mer,1,QTableWidgetItem("图片"))
                self.history_table.setItem(index_mer,2,QTableWidgetItem(mer_info[0][0]))
                self.history_table.item(index_mer,2).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.history_table.setItem(index_mer,3,QTableWidgetItem(str(mer_value)))
                self.history_table.item(index_mer,3).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                index_mer+=1
            index_order+=order_value.num
    #确认订单
    def checkOrderBtn_clicked(self):
        self.returnCartBtn.setEnabled(True)
        self.myOrderBtn.setEnabled(False)
        self.init_con_info()
        self.init_mer_info()
        self.moneyLabel2.setText("总金额:￥"+str(self.money))
        self.moneyLabel2.adjustSize()
        self.stackedWidget.setCurrentIndex(1)
    #显示购物车
    def returnCartBtn_clicked(self):
        self.returnCartBtn.setEnabled(False)
        self.myOrderBtn.setEnabled(True)
        self.stackedWidget.setCurrentIndex(0)
    #支付
    def payBtn_clicked(self,order_id):
        if self.stackedWidget.currentIndex()==1:
            con_name=self.con_info[0]
            con_phone=self.con_info[1]
            con_addr=self.con_info[2]
            dis_method=self.methodBox.currentText()
            date=datetime.date.today()
            self.currentOrder=OrderItem((0,self.account,con_name,con_phone,con_addr,dis_method,"",str(self.mer_dict),self.money,date))
        else:
            self.currentOrder=self.order_dict[order_id]
        payWidget=Pay(self.currentOrder.total)
        returnCode=payWidget.exec()
        if(returnCode):
            self.currentOrder.setStatus("已付款")
        else:
            self.currentOrder.setStatus("未付款")
        if(self.currentOrder.order_id==0):
            self.db.addOrder(self.currentOrder)
        else:
            self.db.changeOrderStatus(self.currentOrder.order_id,self.currentOrder.status)
        self.delete_bought()
        self.myOrderBtn_clicked()
        self.init_history_table()
        pass
    #订单历史
    def myOrderBtn_clicked(self):
        self.returnCartBtn.setEnabled(True)
        self.myOrderBtn.setEnabled(False)
        self.stackedWidget.setCurrentIndex(2)
        #self.init_history_table()
    #显示详情
    def viewDetailBtn_clicked(self,id):
        self.currentOrder=self.order_dict[id]
        mer_info_list=list()
        mer_picture_data=list()
        for i in self.currentOrder.mer_dict:
            t=self.db.getMerInfo(i)
            mer_info_list.append(t)
            mer_picture_data.append(self.db.getMerPictureData(t[0][2]))
        self.detail=Detial(self.currentOrder,mer_info_list,mer_picture_data)
        self.detail.show()
    #完成订单
    def finish_order(self,order_id):
        self.db.changeOrderStatus(order_id,"完成订单")
        self.init_history_table()
    #取消订单
    def cancel_order(self,order_id):
        self.db.changeOrderStatus(order_id,"订单取消")
        self.init_history_table()
    
    #申请退款
    def refund_order(self,order_id):
        self.db.changeOrderStatus(order_id,"申请退款")
        self.init_history_table()
    
class Pay(QDialog,Ui_Dialog):
    def __init__(self,money):
        super().__init__()
        self.setupUi(self)
        self.money_label.setText("￥ "+str(money))
        self.money_label.setAlignment(Qt.AlignCenter)
        self.money_label.setFont(QFont("Roman times",28,QFont.Bold))
        self.confirmBtn.clicked.connect(self.accept)
        self.cancelBtn.clicked.connect(self.reject)
class OrderOperate(QWidget):
    def __init__(self,status:str):
        super().__init__()
        self.viewBtn=QPushButton("查看详情")
        vlayout=QVBoxLayout()
        vlayout.addWidget(self.viewBtn)
        if(status=="未付款"):
            self.payBtn=QPushButton("去支付")
            self.cancelBtn=QPushButton("取消订单")
            vlayout.addWidget(self.payBtn)
            vlayout.addWidget(self.cancelBtn)
        if(status=="已付款"or status=="已准备"):
            self.refundBtn=QPushButton("申请退款")
            vlayout.addWidget(self.refundBtn)
        if(status=="已发货"or status=="已准备"):
            self.finishBtn=QPushButton("确认收货")
            vlayout.addWidget(self.finishBtn)
        self.setLayout(vlayout)
class InputWidget(QDialog,Ui_input):
    def __init__(self,con_info=["","",""]):
        super(QDialog,self).__init__()
        self.setupUi(self)
        self.nameEdit.setText(con_info[0])
        self.phoneEdit.setText(str(con_info[1]))
        self.addrEdit.setText(con_info[2])
        self.phoneEdit.setValidator(QRegExpValidator(QRegExp("[0-9]+$")))
        self.confirmBtn.clicked.connect(self.accept)
        self.cancelBtn.clicked.connect(self.reject)

class Detial(QWidget,Ui_Form):
    def __init__(self,order_item:OrderItem,mer_info_list,data_list,parent=None):
        super(QWidget,self).__init__(parent)
        self.setupUi(self)
        #self.db=db_operate("se","lbc","123456")
        self.mer_table.setColumnWidth(0,150)
        self.mer_table.setColumnWidth(1,120)
        self.mer_table.setColumnWidth(2,120)
        self.mer_table.setColumnWidth(3,80)
        self.mer_table.horizontalHeader().setStretchLastSection(True)
        self.mer_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.mer_table.verticalHeader().setHidden(True)
        self.mer_table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.mer_table.setRowCount(order_item.num)
        self.mer_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        index=0
        for mer_num in order_item.mer_dict.values():
            info=mer_info_list[index]
            picture=createPictureLabel(data_list[index])
            #self.mer_table.setItem(index,0,QTableWidgetItem("图片"))
            self.mer_table.setCellWidget(index,0,picture)
            self.mer_table.setItem(index,1,QTableWidgetItem(info[0][0]))
            self.mer_table.setItem(index,2,QTableWidgetItem("￥ "+str(info[0][1])))
            self.mer_table.setItem(index,3,QTableWidgetItem(str(mer_num)))
            index+=1
        self.id_label.setText("订单编号:    "+str(order_item.order_id))
        self.total_label.setText("总金额: ￥ "+str(order_item.total))
        self.status_label.setText("订单状态: "+order_item.status+"\t"+str(order_item.date))
        self.con_label.setText("收货人信息:"+order_item.con_name+','+str(order_item.con_phone)+','+order_item.con_addr)
        #self.db.close()
        self.pushButton.clicked.connect(self.close)
def createPictureLabel(path):
    picture=QLabel()
    picture.resize(100,100)
    if path=="null":
        picture.setText("暂无图片")
        return picture
    pixmap=QPixmap(path)
    #pixmap=ImageQt.toqpixmap(Image.open(BytesIO(data)))
    pixmap=pixmap.scaled(picture.width(),picture.height())
    picture.setPixmap(pixmap)
    return picture
if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # #test=OrderOperate("未付款")
    # test=InputWidget()
    # test.show()
    # sys.exit(app.exec_())
    db=db_operate("se","lbc","123456")
    data=db.getMerPictureData(11)
    #print(self.data)
    pixmap=ImageQt.toqpixmap(Image.open(BytesIO(data)))
    print(pixmap.height(),pixmap.width())
    #pixmap=pixmap.scaled(picture.width(),picture.height())
    pass
