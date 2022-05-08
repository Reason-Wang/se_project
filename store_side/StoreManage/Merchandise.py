# Merchandise类 为商品的数据结构
# 使用数据库中的表MERCHAN来存储商品信息


#     MERCHAN表的定义:
#         CREATE TABLE IF NOT EXISTS MERCHAN(
#             ID INT PRIMARY KEY,
#             NAME VARCHAR(30),
#             PRICE INT,
#             NUMBER INT 
#         )


# todo
# 为新商品获取唯一标识 & 在数据库中的存储 (初步想法 ：SERIAL)




import sys
import os
print(os.path.abspath('.'))
sys.path.append(os.path.abspath('.'))
from random import random
print(sys.path)
from utils_for_store.db_utils import *



# class Merchandise:
#     def __init__(self,id,name,price,number):
#         self.id=id          #商品唯一标识
#         self.name=name        #商品名称
#         self.price=price       #商品价格
#         self.number=number      #商品库存量
        

#     def toCell(self):
#         return (self.name,self.price,self.number)


# class Merchandise_Manage:
#     def __init__(self):
#         self.user=""
#         self.db_user="lhd"
#         self.passwd="123456"
#         self.tablename = "MERCHAN_SERIAL_ID"
#         self.connection = create_connection(db_name='se',db_user=self.db_user,db_password=self.passwd)
#         self.connection.autocommit = True
#         # self.init_MERCHAN_table()
#         self.merchandise_list=self.get_merchandise_list()
        


#     #only for init table
#     def init_MERCHAN_table(self):
#         connection = self.connection

#         create_MERCHAN_table = f"""
#             CREATE TABLE IF NOT EXISTS {self.tablename}(
#             ID SERIAL PRIMARY KEY,
#             NAME VARCHAR(30),
#             PRICE INT,
#             NUMBER INT 
#             )
#         """
#         execute_query(connection,create_MERCHAN_table)

#         origin_list=[]
#         for i in range(10):
#             id=i
#             name = "name_" + str(i)
#             price = int(random()*100)
#             number = 100
#             origin_list.append(Merchandise(i,name,price,number))
#         for item in origin_list:
#             insert_origin_info = f"""
#             INSERT INTO {self.tablename} (NAME,PRICE,NUMBER)
#                 VALUES {item.toCell()}
#             """
#             execute_query(connection,insert_origin_info)
#         print("insert done")

#         # close(connection)
    
#     def get_merchandise_list(self):
#         connection = self.connection
#         select_all_from_MERCHAN=f"""
#             SELECT * FROM {self.tablename} ORDER BY ID;
#         """
#         result = execute_read_query(connection,select_all_from_MERCHAN)
#         # close(connection)

#         RE = []
#         for tuple in result:
#             RE.append(Merchandise(*tuple))
        
#         return RE

#     def insert_merchandise(self,merch):
#         connection = self.connection
#         insert_query=f"""
#             INSERT INTO {self.tablename} (NAME,PRICE,NUMBER)
#                 VALUES {merch.toCell()}
#         """
#         execute_query(connection,insert_query)
#         self.merchandise_list = self.get_merchandise_list()
#         # close(connection)
#         return


#     def delete_merchandise(self,merch_id):
#         connection = self.connection
#         delete_query = f"""
#             DELETE FROM {self.tablename} WHERE ID = {merch_id};
#         """
#         execute_query(connection,delete_query)
#         self.merchandise_list = self.get_merchandise_list()
#         # close(connection)
#         return

#     def delete_merchandise_byOBJ(self,merch):
#         connection = self.connection
#         delete_query = f"""
#             DELETE FROM {self.tablename} WHERE ID = {merch.id};
#         """
#         execute_query(connection,delete_query)
#         self.merchandise_list = self.get_merchandise_list()
#         # close(connection)
#         return

#     def serch_merchandise(self,merch_id):
#         connection = self.connection
#         serch_query = f"""
#             SELECT * FROM {self.tablename} WHERE ID = {merch_id};
#         """
#         result = execute_read_query(connection,serch_query)
#         if(len(result)==1):
#             return Merchandise(*result[0])
#         return None
#     def update_merchandise(self,merch):
#         connection = self.connection
#         update_query = f"""
#             UPDATE {self.tablename} SET NAME = '{merch.name}' , PRICE ={merch.price} , NUMBER = {merch.number} WHERE ID = {merch.id};
#         """
#         execute_query(connection,update_query)
#         self.merchandise_list = self.get_merchandise_list()
#         # close(connection)
#         return




class Merchandise:
    def __init__(self,id,name,price,number,cat="",info="",pic_id=1):
        self.id=id          #商品唯一标识
        self.name=name        #商品名称
        self.price=price       #商品价格
        self.number=number      #商品库存量
        self.cat = cat
        self.info = info
        self.pic_id = pic_id

    def toCell(self):
        return (self.name,self.price,self.number,self.cat,self.info,self.pic_id)

    def get_pic(self,data):
        self.picture = data

class Merchandise_Manage:
    def __init__(self):
        self.user=""
        self.db_user="lhd"
        self.passwd="123456"
        self.tablename = "MERCHAN_SERIAL_ID"
        self.connection = create_connection(db_name='se',db_user=self.db_user,db_password=self.passwd)
        self.connection.autocommit = True
        # self.init_MERCHAN_table()
        # self.merchandise_list=self.get_merchandise_list()

    #only for init table
    def init_MERCHAN_table(self):
        connection = self.connection

        create_MERCHAN_table = f"""
            CREATE TABLE IF NOT EXISTS {self.tablename}(
            ID SERIAL PRIMARY KEY,
            NAME VARCHAR(30),
            PRICE INT,
            NUMBER INT,
            CAT TEXT,
            INFO TEXT,
            PIC_ID INT 
            )
        """
        execute_query(connection,create_MERCHAN_table)

        origin_list=[]
        for i in range(10):
            id=i
            name = "name_" + str(i)
            price = int(random()*100)
            number = 100
            origin_list.append(Merchandise(i,name,price,number))
        for item in origin_list:
            insert_origin_info = f"""
            INSERT INTO {self.tablename} (NAME,PRICE,NUMBER,CAT,INFO,PIC_ID)
                VALUES {item.toCell()}
            """
            execute_query(connection,insert_origin_info)
        print("insert done")

        # close(connection)
    
    def get_picture_data(self,id):
        connection = self.connection
        tablename = "picture"
        select_picture=f"""
            SELECT * FROM {tablename};
        """
        result = execute_read_query(connection,select_picture)
        return result

    def get_merchandise_list(self):
        connection = self.connection
        select_all_from_MERCHAN=f"""
            SELECT * FROM {self.tablename} ORDER BY ID;
        """
        result = execute_read_query(connection,select_all_from_MERCHAN)
        # close(connection)

        RE = []
        for tuple in result:
            print(tuple)
            RE.append(Merchandise(*tuple))
        return RE

    def insert_merchandise(self,merch):
        connection = self.connection
        insert_query=f"""
            INSERT INTO {self.tablename} (NAME,PRICE,NUMBER,CAT,INFO,PIC_ID)
                VALUES {merch.toCell()}
            """
        execute_query(connection,insert_query)
        self.merchandise_list = self.get_merchandise_list()
        # close(connection)
        return


    def delete_merchandise(self,merch_id):
        connection = self.connection
        delete_query = f"""
            DELETE FROM {self.tablename} WHERE ID = {merch_id};
        """
        execute_query(connection,delete_query)
        self.merchandise_list = self.get_merchandise_list()
        # close(connection)
        return

    def delete_merchandise_byOBJ(self,merch):
        connection = self.connection
        delete_query = f"""
            DELETE FROM {self.tablename} WHERE ID = {merch.id};
        """
        execute_query(connection,delete_query)
        self.merchandise_list = self.get_merchandise_list()
        # close(connection)
        return

    def serch_merchandise(self,merch_id):
        connection = self.connection
        serch_query = f"""
            SELECT * FROM {self.tablename} WHERE ID = {merch_id};
        """
        result = execute_read_query(connection,serch_query)
        if(len(result)==1):
            return Merchandise(*result[0])
        return None
    def update_merchandise(self,merch):
        connection = self.connection
        update_query = f"""
            UPDATE {self.tablename} SET NAME = '{merch.name}' , PRICE ={merch.price} , NUMBER = {merch.number},
            CAT = '{merch.cat}',INFO='{merch.info}',PIC_ID = {merch.pic_id} WHERE ID = {merch.id};
        """
        execute_query(connection,update_query)
        self.merchandise_list = self.get_merchandise_list()
        # close(connection)
        return

    def upload_img(self,picpath,picname=""):
        connection = self.connection
        picid = picname.split('.')[0]
        pic_id = insert_img(connection,picpath,picname,picid)
        return pic_id

    
    def get_order_list(self):
        connection = self.connection
        select_all_from_MERCHAN="""
            SELECT * FROM  order_table;
        """
        result = execute_read_query(connection,select_all_from_MERCHAN)
        return result


if __name__=='__main__':
    # # merch=Merchandise(1,2,3,4)
    # # merch.toJson()
    # manager = Merchandise_Manage()
    # # print(manager.merchandise_list)
    # picpath=r"C:\Users\l\Desktop\se\img.png"
    # insert_img(manager.connection,picpath)
    # # data=manager.get_picture_data(1)
    # # print(data)
    # # fout = open('sid87873.jpg', 'wb')
    # # fout.write(data[0][1])
    exit()
    