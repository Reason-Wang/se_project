import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from ui.register_window import *
from ui.login_window import *
from ui.shop_main_window import *

from ui.shop_info_window import *
from send_data import *


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
        s = Send_data()
        recv = s.message(data)
        s.close()
        print("111")
        if recv['result'] == 'success':
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
        s = Send_data()
        recv = s.message(data)
        s.close()
        if recv['result'] == 'success':
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
        s = Send_data()
        recv = s.message(data)
        s.close()
        if recv['result'] == 'success':
            QMessageBox.information(self, "修改店铺信息", "修改成功", QMessageBox.Yes)
        else:
            QMessageBox.information(self, "修改店铺信息", "修改失败", QMessageBox.Yes)
        self.load()

    def load(self):
        data = {'id': 'shop', 'type': 'shop_info', 'user': user}
        s = Send_data()
        recv = s.message(data)
        s.close()
        self.username.setText(recv['result'][0])
        self.username.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pass1.setText(recv['result'][1])
        self.pass2.setText(recv['result'][1])
        self.shop_name.setText(recv['result'][2])
        self.phone.setText(recv['result'][3])
        self.addr.setCurrentText(recv['result'][4])
        self.shop_time.setText(recv['result'][5])
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
