import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from ui.register_window import *
from ui.login_window import *
from ui.shop_main_window import *

from ui.shop_info_window import *
from send_data import *
import psycopg2
import time


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

class Register(QMainWindow, Ui_register_window):
    def __init__(self, parent=None):
        super(Register, self).__init__(parent)
        self.setupUi(self)
        self.reg_bt.clicked.connect(self.click1)
        self.tologin.clicked.connect(self.click2)

    def click1(self):
        username = self.username.text()
        pass1 = self.pass1.text()
        pass2 = self.pass2.text()
        shop_name = self.shop_name.text()
        phone = self.phone.text()
        addr = self.addr.currentText()
        if username == '' or pass1 == '' or shop_name == '' or phone == '' or addr == '':
            QMessageBox.information(self, "注册", "店铺信息不能为空", QMessageBox.Yes)
            return
        if pass1 != pass2:
            QMessageBox.information(self, "注册", "两次密码不同", QMessageBox.Yes)
            return
        data = {'id': 'shop', 'type': 'register', 'user': username,
                'passwd': pass1, 'shop_name': shop_name, 'phone': phone, 'addr': addr}
        print("111")
        op1 = Shop_op()
        if op1.register(data['user'], data['passwd'], data['shop_name'], data['phone'], data['addr']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        print("111")
        if data['result'] == 'success':
            QMessageBox.information(self, "注册", "注册成功", QMessageBox.Yes)
        else:
            QMessageBox.information(self, "注册", "注册失败", QMessageBox.Yes)

    def click2(self):
        myWin1.hide()
        myWin2.show()


class Login(QMainWindow, Ui_login_window):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        self.login_bt.clicked.connect(self.click1)
        self.toreg.clicked.connect(self.click2)

    def click1(self):
        global user
        username = self.username.text()
        password = self.password.text()
        if username == '' or password == '':
            QMessageBox.information(self, "登录", "用户名和密码不能为空", QMessageBox.Yes)
            return
        data = {'id': 'shop', 'type': 'login',
                'user': username, 'passwd': password}
        op1 = Shop_op()
        if op1.login(data['user'], data['passwd']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        if data['result'] == 'success':
            QMessageBox.information(self, "登录", "登录成功", QMessageBox.Yes)
            user = username
            myWin2.hide()
            myWin3.show()
        else:
            QMessageBox.information(self, "登录", "登录失败", QMessageBox.Yes)

    def click2(self):
        myWin2.hide()
        myWin1.show()


class Mainwin(QMainWindow, Ui_shop_main):
    def __init__(self, parent=None):
        super(Mainwin, self).__init__(parent)
        self.setupUi(self)
        # self.add_goods.clicked.connect(self.click1)
        # self.view_goods.clicked.connect(self.click2)
        # self.change_goods.clicked.connect(self.click3)
        # self.view_trade.clicked.connect(self.click4)
        self.shop_info.clicked.connect(self.click5)

    # def click1(self):
    #     myWin4.show()
    #
    # def click2(self):
    #     myWin5.load()
    #     myWin5.show()
    #
    # def click3(self):
    #     myWin6.load()
    #     myWin6.show()
    #
    # def click4(self):
    #     myWin7.show()

    def click5(self):
        myWin8.load()
        myWin8.show()




class Shopinfo(QMainWindow, Ui_shop_info):
    def __init__(self, parent=None):
        super(Shopinfo, self).__init__(parent)
        self.setupUi(self)
        self.tomain.clicked.connect(self.click1)
        self.change_bt.clicked.connect(self.click2)

    def click1(self):
        self.hide()

    def click2(self):
        pass1 = self.pass1.text()
        pass2 = self.pass2.text()
        shop_name = self.shop_name.text()
        phone = self.phone.text()
        addr = self.addr.currentText()
        data = {'id': 'shop', 'type': 'update_shop', 'user': user,
                'passwd': pass1, 'shop_name': shop_name, 'phone': phone, 'addr': addr}
        op1 = Shop_op()

        if op1.update_shop(data['user'], data['passwd'], data['shop_name'], data['phone'], data['addr']):
            QMessageBox.information(self, "修改店铺信息", "修改成功", QMessageBox.Yes)
        else:
            QMessageBox.information(self, "修改店铺信息", "修改失败", QMessageBox.Yes)
        self.load()

    def load(self):
        data = {'id': 'shop', 'type': 'shop_info', 'user': user}
        op1 = Shop_op()
        data = {'result': op1.shop_info(data['user'])}
        self.username.setText(data['result'][0])
        self.username.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pass1.setText(data['result'][1])
        self.pass2.setText(data['result'][1])
        self.shop_name.setText(data['result'][2])
        self.phone.setText(data['result'][3])
        self.addr.setCurrentText(data['result'][4])
        self.shop_time.setText(data['result'][5])
        self.shop_time.setFocusPolicy(QtCore.Qt.NoFocus)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    user = ""
    myWin1 = Register()
    myWin1.show()
    myWin2 = Login()
    myWin3 = Mainwin()


    myWin8 = Shopinfo()
    # myWin8.show()

    if app.exec_() == 0:
        sys.exit(0)
