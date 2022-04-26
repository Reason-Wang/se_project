import threading
import time
import queue
import socket
import json
from mysql_op import *


class Shop:
    def __init__(self, conn):
        self.conn = conn

    def register(self, recv):
        op1 = Shop_op()
        if op1.register(recv['user'], recv['passwd'], recv['shop_name'], recv['phone'], recv['addr']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def login(self, recv):
        op1 = Shop_op()
        if op1.login(recv['user'], recv['passwd']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def shopinfo(self, recv):
        op1 = Shop_op()
        data = {'result': op1.shop_info(recv['user'])}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def updateshop(self, recv):
        op1 = Shop_op()
        if op1.update_shop(recv['user'], recv['passwd'], recv['shop_name'], recv['phone'], recv['addr']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()


class Customer:
    def __init__(self, conn):
        self.conn = conn

    def register(self, recv):
        op1 = Customer_op()
        if op1.register(recv['user'], recv['passwd'], recv['cus_name'], recv['phone'], recv['addr']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def login(self, recv):
        op1 = Customer_op()
        if op1.login(recv['user'], recv['passwd']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()


    def cusinfo(self, recv):
        op1 = Customer_op()
        data = {'result': op1.cus_info(recv['user'])}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def updatecus(self, recv):
        op1 = Customer_op()
        if op1.update_cus(recv['user'], recv['passwd'], recv['cus_name'], recv['phone'], recv['addr']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 5000))
    s.listen(20)
    while True:
        conn, addr = s.accept()
        recv = json.loads(conn.recv(1024).decode())
        # print(json.dumps(recv))
        if recv['id'] == 'shop':
            Shop1 = Shop(conn)
            if recv['type'] == 'register':
                Shop1.register(recv)
            elif recv['type'] == 'login':
                Shop1.login(recv)
            elif recv['type'] == 'shop_info':
                Shop1.shopinfo(recv)
            elif recv['type'] == 'update_shop':
                Shop1.updateshop(recv)
        else:
            Cus1 = Customer(conn)
            if recv['type'] == 'register':
                Cus1.register(recv)
            elif recv['type'] == 'login':
                Cus1.login(recv)

            elif recv['type'] == 'cus_info':
                Cus1.cusinfo(recv)
            elif recv['type'] == 'update_cus':
                Cus1.updatecus(recv)
