import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from customer.register_window import *
from customer.login_window import *
from customer.cus_main import *

from customer.cus_info import *
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
        cus_name = self.cus_name.text()
        phone = self.phone.text()
        addr = self.addr.text()
        if username == '' or pass1 == '' or cus_name == '' or phone == '' or addr == '':
            QMessageBox.information(self, "注册", "顾客信息不能为空", QMessageBox.Yes)
            return
        if pass1 != pass2:
            QMessageBox.information(self, "注册", "两次密码不同", QMessageBox.Yes)
            return
        data = {'id': 'customer', 'type': 'register', 'user': username,
                'passwd': pass1, 'cus_name': cus_name, 'phone': phone, 'addr': addr}
        # print(json.dumps(data))
        s = Send_data()
        recv = s.message(data)
        s.close()
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
        data = {'id': 'customer', 'type': 'login',
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


class Mainwin(QMainWindow, Ui_cus_main):
    def __init__(self, parent=None):
        super(Mainwin, self).__init__(parent)
        self.setupUi(self)

        self.cus_info.clicked.connect(self.click5)



    def click5(self):
        myWin8.load()
        myWin8.show()





class Cusinfo(QMainWindow, Ui_cus_info):
    def __init__(self, parent=None):
        super(Cusinfo, self).__init__(parent)
        self.setupUi(self)
        self.tomain.clicked.connect(self.click1)
        self.change_bt.clicked.connect(self.click2)

    def click1(self):
        self.hide()

    def click2(self):
        pass1 = self.pass1.text()
        pass2 = self.pass2.text()
        cus_name = self.cus_name.text()
        phone = self.phone.text()
        addr = self.addr.text()
        data = {'id': 'customer', 'type': 'update_cus', 'user': user,
                'passwd': pass1, 'cus_name': cus_name, 'phone': phone, 'addr': addr}
        s = Send_data()
        recv = s.message(data)
        s.close()
        if recv['result'] == 'success':
            QMessageBox.information(self, "修改顾客信息", "修改成功", QMessageBox.Yes)
        else:
            QMessageBox.information(self, "修改顾客信息", "修改失败", QMessageBox.Yes)
        self.load()

    def load(self):
        data = {'id': 'customer', 'type': 'cus_info', 'user': user}
        s = Send_data()
        recv = s.message(data)
        s.close()
        self.username.setText(recv['result'][0])
        self.username.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pass1.setText(recv['result'][1])
        self.pass2.setText(recv['result'][1])
        self.cus_name.setText(recv['result'][2])
        self.phone.setText(recv['result'][3])
        self.addr.setText(recv['result'][4])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    user = ""
    myWin1 = Register()
    myWin1.show()
    myWin2 = Login()
    myWin3 = Mainwin()

    myWin8 = Cusinfo()
    if app.exec_() == 0:
        sys.exit(0)
