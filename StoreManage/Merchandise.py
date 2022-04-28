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



from random import random
import sys
sys.path.append('..')
from utils.db_utils import *



class Merchandise:
    def __init__(self,id,name,price,number):
        self.id=id          #商品唯一标识
        self.name=name        #商品名称
        self.price=price       #商品价格
        self.number=number      #商品库存量

    def toCell(self):
        return (self.id,self.name,self.price,self.number)


class Merchandise_Manage:
    def __init__(self):
        self.user=""
        self.db_user="lhd"
        self.passwd="123456"
        self.tablename="MERCHAN"
        self.merchandise_list=self.get_merchandise_list()


    #only for init table
    def init_MERCHAN_table(self):
        connection = create_connection(db_name='se',db_user=self.db_user,db_password=self.passwd)

        create_MERCHAN_table = """
            CREATE TABLE IF NOT EXISTS MERCHAN(
            ID INT PRIMARY KEY,
            NAME VARCHAR(30),
            PRICE INT,
            NUMBER INT 
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
            INSERT INTO MERCHAN (ID,NAME,PRICE,NUMBER)
                VALUES {item.toCell()}
            """
            execute_query(connection,insert_origin_info)
        print("insert done")

        close(connection)
    
    def get_merchandise_list(self):
        connection = create_connection(db_name='se',db_user=self.db_user,db_password=self.passwd)
        select_all_from_MERCHAN="""
            SELECT * FROM MERCHAN
        """
        result = execute_read_query(connection,select_all_from_MERCHAN)
        close(connection)
        return result

    def insert_merchandise(self,merch):
        connection = create_connection(db_name='se',db_user=self.db_user,db_password=self.passwd)
        insert_query=f"""
            INSERT INTO MERCHAN (ID,NAME,PRICE,NUMBER)
                VALUES {merch.toCell()}
        """
        execute_query(connection,insert_query)
        close(connection)
        return


    def delete_merchandise(self,merch_id):
        connection = create_connection(db_name='se',db_user=self.db_user,db_password=self.passwd)
        delete_query = f"""
            DELETE FROM MERCHAN WHERE ID = {merch_id};
        """
        execute_query(connection,delete_query)
        close(connection)
        return

    def serch_merchandise(self):
        return
    def update_merchandise(self):
        return
if __name__=='__main__':
    manager = Merchandise_Manage()
    print(manager.merchandise_list)