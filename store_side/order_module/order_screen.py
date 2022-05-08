import ast

import setuptools.config.setupcfg

from order_module.订单 import Ui_Form
from PyQt5.QtWidgets import *
from order_module.database_operation import *
from PyQt5 import QtWidgets
import functools

class orderScreen(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(orderScreen, self).__init__(parent)
        self.setupUi(self)
        #self.lalala()
        self.refresh_order_table()
        self.setWindowTitle('订单管理')
        #self.pushButton_ex.clicked.connect
        self.pushButton_3.clicked.connect(self.refresh_order_table)     #刷新按钮可以直接连接
        self.lineEdit.setReadOnly(True)
    def refresh_order_table(self):     #刷新订单表
        a=0
        b=0
        self.tableWidget.setRowCount(query_row_number()[0][0])
        self.tableWidget.setColumnCount(11)
        for id in query_yining_order_table():
            for xiao_id in id:
                item=QtWidgets.QTableWidgetItem(f"{xiao_id}")
                self.tableWidget.setItem(a,b,item)
                b=b+1
                if b==10:
                    b=0
                    a=a+1
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  #设置表格内容不可编辑
        # self.pushButton_2.clicked.connect(self.change_Commodity_Number)
        for k in range(0,(query_row_number()[0][0])):
            bt = QPushButton('处理')
            bt.clicked.connect(functools.partial(self.solve_order,self.tableWidget.item(k,0).text()))
            #bt.clicked.connect(functools.partial(self.change_Commodity_Number_button,self.tableWidget.item(k,0).text()))
            self.tableWidget.setCellWidget(k,10,bt)
        #下面的函数就是商品ID变成商品名字然后写进表里的函数
        for t in range(0,(query_row_number()[0][0])):       #先正常建表,然后单独该字典
            mer_dict = ast.literal_eval((query_order_table_kang_mer_dict_accordingID(self.tableWidget.item(t,0).text())[0][0]))
            string=''
            for i, j in mer_dict.items():
                if (query_name_accordingID(i)[0][0])=='0':
                        M='商品下架'
                else:
                    M=query_name_accordingID(i)[0][0]
                string = string+(str(M)+':'+str(j)+',')
            string=string.strip(',')
            Dict=QtWidgets.QTableWidgetItem(f"{string}")
            self.tableWidget.setItem(t,7,Dict)
        self.tableWidget.resizeColumnToContents(7)  #自动设置第7列的宽度


    #改变商品库里面商品数量，按照名字查找一定要认真使用query_table的返回对象,
    def change_Commodity_Number(self):   #这个是手动输入订单编号的函数
        info = self.textEdit.toPlainText()
        mer_dict = ast.literal_eval((query_bincheng_order_table_mer_dict_according_orderID(info)[0][0]))
        a=1
        for i,j in mer_dict.items():
            # print((query_food_number_according_foodID((i))[0][0]))  #非常完美，我已经能够查找到表中数量了
            # print(j)
            if(j>(query_food_number_according_foodID((i))[0][0])):
                a=0
        print(a)
        if (a==1):
            for i,j in mer_dict.items():
                t=(query_food_number_according_foodID((i))[0][0])-j
                change_food_number(i,t)
                #yes_change_order_status_according_orderID(info)
                QMessageBox.about(self, '处理反馈', '订单处理成功！')
            else:
                no_change_order_status_according_orderID(info)
                # print("无法处理，库存数量不满足订单要求")
                QMessageBox.about(self, '处理反馈', '无法处理，库存数量不满足订单要求！订单自动取消！')

    #
    # def lalala(self):
    #     print(query_bincheng_order_table_rowCount()[0][0])

    def solve_order(self,order_id):
        info = order_id
        if (query_order_status_according_orderID(info)[0][0])=='申请退款':
            change_refund_accordingID(info)
            QMessageBox.about(self, '处理反馈', '退款成功！')

        else:
            mer_dict = ast.literal_eval((query_order_table_kang_mer_dict_accordingID(info)[0][0]))
            a = 1
            for i, j in mer_dict.items():
                # print((query_food_number_according_foodID((i))[0][0]))  #非常完美，我已经能够查找到表中数量了
                # print(j)
                if (j > (query_merchan_kang_number_according_ID((i))[0][0])):
                    a = 0
            #print(a)
            if (a == 1):
                for i, j in mer_dict.items():
                    t = (query_merchan_kang_number_according_ID((i))[0][0]) - j
                    change_merchan_kang_number(i, t)
                if (query_dis_method_accordingID(info)=='超市配送'):
                    yes_change_order_status_market_delivery(info)
                else:
                    yes_change_order_status_take_individual(info)
                QMessageBox.about(self, '处理反馈', '订单处理成功！')
            else:
                no_change_order_status_according_orderID(info)
                #print("无法处理，库存数量不满足订单要求")
                QMessageBox.about(self, '处理反馈','无法处理，库存数量不满足订单要求！订单自动取消！')









    def change_Commodity_Number_button(self, order_id):
        info = order_id
        mer_dict = ast.literal_eval((query_bincheng_order_table_mer_dict_according_orderID(info)[0][0]))
        a = 1
        for i, j in mer_dict.items():
            # print((query_food_number_according_foodID((i))[0][0]))  #非常完美，我已经能够查找到表中数量了
            # print(j)
            if (j > (query_food_number_according_foodID((i))[0][0])):
                a = 0
        # print(a)
        if (a == 1):
            for i, j in mer_dict.items():
                t = (query_food_number_according_foodID((i))[0][0]) - j
                change_food_number(i, t)
                #(info)
                QMessageBox.about(self, '处理反馈', '订单处理成功！')
        else:
            no_change_order_status_according_orderID(info)
            # print("无法处理，库存数量不满足订单要求")
            QMessageBox.about(self, '处理反馈', '无法处理，库存数量不满足订单要求！订单自动取消！')













