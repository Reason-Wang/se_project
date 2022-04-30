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
# );
# create table purchase_info(
#     order_id int references order_table(order_id),
#     mer_id int not null,         #商品id
#     quantity int not null        #购买数量
# );
# create table cart_info(
#     cus_acc varchar(30),         #账号
#     mer_id int not null,         #商品id
#     quantity int not null,       #购买数量
#     primary key(cus_acc,mer_id)  
# );

import os,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)))
from utils.db_utils import *
# from checkOrder import CheckOrder
db_connect=create_connection("se","lbc","123456")#数据库连接
db_connect.autocommit=True
def getCart(cus_acc):#返回购物车信息
    temp=execute_read_query(db_connect,"select mer_id,quantity from cart_info where cus_acc='%s'"%cus_acc)
    id_dict=dict()
    for i in temp:
        id_dict[i[0]]=i[1]
    return id_dict
def changeCart(cus_acc,id_dict):
    for key,value in id_dict.items():
        execute_query(db_connect,"update cart_info set quantity={quantity} where cus_acc='{cus_acc}' and mer_id={id}".format(quantity=value,cus_acc=cus_acc,id=key))
def deleteCart(cus_acc,id):
    execute_query(db_connect,"delete from cart_info where cus_acc='{cus_acc}' and mer_id={id}".format(cus_acc=cus_acc,id=id))
# def show_checkOrder(cus_acc,id_dict):
#     co=CheckOrder(cus_acc,id_dict)
#     co.show()
if __name__ == '__main__':
    # execute_query(db_connect,"insert into cart_info(cus_acc,mer_id,quantity)values('20191234',1,4)")
    # execute_query(db_connect,"insert into cart_info(cus_acc,mer_id,quantity)values('20191234',2,5)")
    # execute_query(db_connect,"insert into cart_info(cus_acc,mer_id,quantity)values('20191234',3,2)")
    execute_query(db_connect,"insert into cart_info(cus_acc,mer_id,quantity)values('20191234',6,99)")
    #deleteCart("20191234",1)
    #execute_query(db_connect,"delete from cart_info where cus_acc='20191234' and mer_id=1")
