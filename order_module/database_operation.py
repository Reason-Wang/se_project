from utils.db_utils import *
from order_module.订单 import Ui_Form
se_connection=create_connection("se","kyn","123456")#数据库连接
se_connection.autocommit=True

def query_table():  #查询订单表,返回一个list对象
    temp=execute_read_query(se_connection,"SELECT * FROM order_table_kang")
    return temp

def query_table_according_orderID(a):
    temp = execute_read_query(se_connection, "SELECT * FROM order_table_kang WHERE order_id='%s'"%a)
    return temp

def query_table_mer_dict_according_orderID(a):
    temp = execute_read_query(se_connection, "SELECT mer_dict FROM order_table_kang WHERE order_id='%s'"%a)
    return temp

def query_bincheng_order_table():
    temp = execute_read_query(se_connection, "SELECT * FROM order_table")
    return temp

def query_yining_order_table():
    temp = execute_read_query(se_connection, "SELECT * FROM order_table_kang")
    return temp

def query_bincheng_order_table_mer_dict_according_orderID(a):
    temp = execute_read_query(se_connection, "SELECT mer_dict FROM order_table WHERE order_id='%s'"%a)
    return temp

def query_food_number_according_foodID(a):
    #temp = execute_read_query(se_connection, "SELECT number FROM food WHERE name =
    temp = execute_read_query(se_connection, "SELECT number FROM food WHERE name ='%d'"%a)
    return temp

def change_food_number(a,b):
    temp=execute_query(se_connection,"UPDATE food SET number ='%d' WHERE name='%d'"%(b,a))

def query_row_number():
    temp = execute_read_query(se_connection,"SELECT COUNT(*) FROM order_table_kang");
    return temp

def yes_change_order_status_according_orderID(a):
    temp = execute_query(se_connection, "UPDATE order_table_kang SET order_status ='已发货'  FROM food WHERE order_id ='%s'"%a)


def no_change_order_status_according_orderID(a):
    temp = execute_query(se_connection, "UPDATE order_table_kang SET order_status ='订单取消'  FROM food WHERE order_id ='%s'"%a)

def query_name_accordingID(a):
    temp=execute_read_query(se_connection,"SELECT name FROM merchan2 WHERE id='%d'"%a)
    return temp


