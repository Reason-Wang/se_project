# create type method as enum('超市配送','自行取货');
# create type order_status as enum('未付款','已付款','已准备','已发货',' 完成订单','申请退款','订单取消');
# create table order_table(
#     order_id serial primary key, #订单编号
#     cus_acc varchar(30) not null,#账号
#     con_name varchar(20),        #收货人姓名
#     con_phone int,               #收货人联系方式
#     con_addr varchar(50),        #收货地址
#     dis_method method,           #配送方式
#     order_status order_status    #订单状态
#     mer_dict text,
# );
# create table acc_cart(#购物车信息
#     cus_acc varchar(30),         
#     cart text,
#     primary key (cus_acc)
# );
# create table purchase_info(#废案
#     order_id int references order_table(order_id),
#     mer_id int not null,         #商品id
#     quantity int not null        #购买数量
# );
# create table cart_info(#废案
#     cus_acc varchar(30),         #账号
#     mer_id int not null,         #商品id
#     quantity int not null,       #购买数量
#     primary key(cus_acc,mer_id)  
# );


from distutils.log import info
import os,sys,ast
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)))
from utils.db_utils import *
class db_operate():
    def __init__(self,db_name,user_name,pass_word):
        self.db_connect=create_connection(db_name,user_name,pass_word)
        self.db_connect.autocommit=True
    def getMerInfo(self,id):
        info=execute_read_query(self.db_connect,"select name,price from merchan2 where id=%d"%(id))
        return info
    def getCart(self,cus_acc):
        cart_str=(execute_read_query(self.db_connect,"select cart from acc_cart where cus_acc='%s'"%cus_acc))[0][0]
        #print(cart_str)
        cart_dict=ast.literal_eval(cart_str)
        return cart_dict
    def changeCart(self,cus_acc,cart_dict):
        execute_query(self.db_connect,"update acc_cart set cart='{cart_dict}' where cus_acc='{cus_acc}'".format(cart_dict=str(cart_dict),cus_acc=cus_acc))
    def deleteCart(self,cus_acc,id):
        execute_query(self.db_connect,"delete from cart_info where cus_acc='{cus_acc}' and mer_id={id}".format(cus_acc=cus_acc,id=id))
    def getCusInfo(self,cus_acc):
        info_list=execute_read_query(self.db_connect,"select cus_name,cus_phone,cus_addr from customer where cus_acc='%s'"%cus_acc)
        return info_list[0]

# db_connect=create_connection("se","lbc","123456")#数据库连接
# db_connect.autocommit=True
# def getMerInfo(id):
#     info=execute_read_query(db_connect,"select name,price from merchan2 where id=%d"%(id))
#     return info
# def getCart(cus_acc):
#     cart_str=(execute_read_query(db_connect,"select cart from acc_cart where cus_acc='%s'"%cus_acc))[0][0]
#     #print(cart_str)
#     cart_dict=ast.literal_eval(cart_str)
#     return cart_dict
# def changeCart(cus_acc,cart_dict):
#     execute_query(db_connect,"update acc_cart set cart='{cart_dict}' where cus_acc='{cus_acc}'".format(cart_dict=str(cart_dict),cus_acc=cus_acc))
# def deleteCart(cus_acc,id):
#     execute_query(db_connect,"delete from cart_info where cus_acc='{cus_acc}' and mer_id={id}".format(cus_acc=cus_acc,id=id))
# def getCusInfo(cus_acc):
#     info_str=execute_read_query(db_connect,"select cus_name,cus_phone,cus_addr from customer where cus_acc='%s'"%cus_acc)
#     print(info_str)
if __name__ == '__main__':
    db=db_operate("se","lbc","123456")
    db.getCusInfo("20191234")
    pass
    # execute_query(db_connect,"insert into cart_info(cus_acc,mer_id,quantity)values('20191234',1,4)")
    # execute_query(db_connect,"insert into cart_info(cus_acc,mer_id,quantity)values('20191234',2,5)")
    # execute_query(db_connect,"insert into cart_info(cus_acc,mer_id,quantity)values('20191234',3,2)")
    #execute_query(db_connect,"insert into cart_info(cus_acc,mer_id,quantity)values('20191234',6,99)")
    #execute_query(db_connect,"insert into customer(cus_acc,cus_pass,cus_name,cus_phone,cus_addr)values('20191234','abc','李华',123456,'五舍b436')")
    #deleteCart("20191234",1)
    #execute_query(db_connect,"delete from cart_info where cus_acc='20191234' and mer_id=1")
    #execute_query(db_connect,r"insert into acc_cart(cus_acc,cart)values('20191234','{2:5,3:4,1:7}')")
    #getCart("20191234")
    #getCusInfo("20191234")
    