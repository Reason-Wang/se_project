"""
Merchandise类 为商品的数据结构
使用数据库中的表MERCHAN来存储商品信息


    MERCHAN表的定义:
        CREATE TABLE MERCHAN(
            ID INT PRIMARY KEY,
            NAME VARCHAR(30),
            PRICE INT,
            NUMBER INT 
        )


todo
为新商品获取唯一标识 & 在数据库中的存储 (初步想法 ：SERIAL)
"""


import sys
sys.path.append('../utils')
import db_utils


class Merchandise:
    def __init__(self):
        self.id=-1          #商品唯一标识
        self.name=""        #商品名称
        self.price=-1       #商品价格
        self.number=-1      #商品库存量



class Merchandise_Manage:
    def __init(self):
        self.user=""
        self.db_user="lhd"
        self.passwd="123456"
        self.tablename="MERCHAN"
        merchandise_list=Get_merchandise_list()


    def toCell(self):
        return (self.name,self.price,self.number)


    def Get_merchandise_list():
        mer_list=[]
        ##todo get merchandise_list from database
        return mer_list


if __name__=='__main__':
    posts = [
        ("Happy", "I am feeling very happy today", 1),
        ("Hot Weather", "The weather is very hot today", 2),
        ("Help", "I need some help with my work", 2),
        ("Great News", "I am getting married", 1),
        ("Interesting Game", "It was a fantastic game of tennis", 5),
        ("Party", "Anyone up for a late-night party today?", 3),
    ]

    post_records = ", ".join(["%s"] * len(posts))
    print(post_records)