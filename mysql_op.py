import pymysql
import time
import datetime
import psycopg2

class Shop_op:
    def __init__(self):
        self.host = '123.57.48.49'
        self.user = 'shy'
        self.passwd = '123456'
        self.port = 5432

    def connect(self):
        self.conn = psycopg2.connect(
            host=self.host, user=self.user, password=self.passwd, dbname='se')
        # self.conn.select_db('se')
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()

    def register(self, user, passwd, shop_name, phone, addr):
        self.connect()
        self.cur.execute('select shop_acc from shop where shop_acc=%s', [user])
        data = self.cur.fetchone()
        if data is not None:
            self.close()
            return False
        value = [user, passwd, shop_name, phone, addr, time.strftime(
            '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))]
        self.cur.execute('insert into shop values(%s,%s,%s,%s,%s,%s)', value)
        self.conn.commit()
        self.close()
        return True

    def login(self, user, passwd):
        self.connect()
        value = [user, passwd]
        self.cur.execute(
            'select shop_acc,shop_pass from shop where shop_acc=%s and shop_pass=%s', value)
        data = self.cur.fetchone()
        if data is not None:
            self.close()
            return True
        self.close()
        return False

    def shop_info(self, user):
        self.connect()
        self.cur.execute(
            'select shop_acc,shop_pass,shop_name,shop_phone,shop_addr,shop_time from shop where shop_acc=%s', [user])
        data = self.cur.fetchone()
        self.close()
        return data

    def update_shop(self, user, passwd, shop_name, phone, addr):
        self.connect()
        try:
            value = [passwd, shop_name, phone, addr, user]
            self.cur.execute(
                'update shop set shop_pass=%s,shop_name=%s,shop_phone=%s,shop_addr=%s where shop_acc=%s', value)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            self.close()
            return False
        self.close()
        return True


class Customer_op:
    def __init__(self):
        self.host = '123.57.48.49'
        self.user = 'shy'
        self.passwd = '123456'
        self.port = 5432

    def connect(self):
        self.conn = psycopg2.connect(
            host=self.host, user=self.user, password=self.passwd, dbname='se')
        # self.conn.select_db('se')
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()

    def register(self, user, passwd, cus_name, phone, addr):
        self.connect()
        self.cur.execute(
            'select cus_acc from customer where cus_acc=%s', [user])
        data = self.cur.fetchone()
        if data is not None:
            self.close()
            return False
        value = [user, passwd, cus_name, phone, addr]
        self.cur.execute('insert into customer values(%s,%s,%s,%s,%s)', value)
        self.conn.commit()
        self.close()
        return True

    def login(self, user, passwd):
        self.connect()
        value = [user, passwd]
        self.cur.execute(
            'select cus_acc,cus_pass from customer where cus_acc=%s and cus_pass=%s', value)
        data = self.cur.fetchone()
        if data is not None:
            self.close()
            return True
        self.close()
        return False



    def cus_info(self, user):
        self.connect()
        self.cur.execute(
            'select cus_acc,cus_pass,cus_name,cus_phone,cus_addr from customer where cus_acc=%s', [user])
        data = self.cur.fetchone()
        self.close()
        return data

    def update_cus(self, user, passwd, cus_name, phone, addr):
        self.connect()
        try:
            value = [passwd, cus_name, phone, addr, user]
            self.cur.execute(
                'update customer set cus_pass=%s,cus_name=%s,cus_phone=%s,cus_addr=%s where cus_acc=%s', value)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            self.close()
            return False
        self.close()
        return True


if __name__ == "__main__":
    op1 = Customer_op()

