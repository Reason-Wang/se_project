from login_module.ui_login import Ui_Form
from PyQt5.QtWidgets import QDialog, QWidget
from login_module.register_panel import RegisterPanel
from login_module.login_panel import LoginPanel
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import pyqtSignal

from login_module.login_utils import get_user_info, register_user_info

class Login(QDialog, Ui_Form):
    switch_user_signal = pyqtSignal()

    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.register_panel = RegisterPanel()
        self.login_panel = LoginPanel()


        self.set_login_panel()

        # connect buttons to switch panels
        self.login_panel.pushButton_register.clicked.connect(self.set_register_panel)
        self.register_panel.pushButton_login.clicked.connect(self.set_login_panel)

        # connect button to login and register
        self.login_panel.pushButton_login.clicked.connect(self.login_user)
        self.register_panel.pushButton_register.clicked.connect(self.register_user)

        self.user_info = {}



    def set_login_panel(self):
        self.scrollArea.takeWidget()
        self.scrollArea.setWidget(self.login_panel)

    def set_register_panel(self):
        self.scrollArea.takeWidget()
        self.scrollArea.setWidget(self.register_panel)

    def login_user(self):
        name = self.login_panel.lineEdit_user_name.text()
        password = self.login_panel.lineEdit_password.text()
        # print(user_info)
        user_info = get_user_info(name)
        # print('user info: '+ str(user_info))
        if not bool(user_info): # if no user matched
            QMessageBox.warning(QWidget(), 'no user', '用户不存在')
        else:
            if password == user_info['password']:
                self.user_info = user_info
                QMessageBox.information(QWidget(), "successful", "登录成功")
                self.login_panel.lineEdit_user_name.clear()
                self.login_panel.lineEdit_password.clear()
                self.switch_user_signal.emit()
                self.hide()
            else:
                QMessageBox.warning(QWidget(), 'password incorrect', '用户名或密码不正确')

    def register_user(self):
        new_user_info = {}
        new_user_info['name'] = self.register_panel.lineEdit_user_name.text()
        new_user_info['password'] = self.register_panel.lineEdit_password.text()
        if new_user_info['name'] == '' or new_user_info['password'] == '':
            QMessageBox.warning(QWidget(), 'empty error', '用户名或密码不能为空')
            return
        password_confirm = self.register_panel.lineEdit_password_sure.text()
        if new_user_info['password'] != password_confirm:
            QMessageBox.warning(QWidget(), 'password not consistent', '密码不一致')
            return
        else:
            new_user_info['receiver'] = self.register_panel.lineEdit_receiver.text()
            new_user_info['phone'] = self.register_panel.lineEdit_phone.text()
            new_user_info['address'] = self.register_panel.lineEdit_address.text()

            user_info = get_user_info(new_user_info['name'])
            if bool(user_info):         # there is user with same name in database
                QMessageBox.warning(QWidget(), 'user exists', '用户已存在')
            else:
                register_user_info(new_user_info)
                QMessageBox.information(QWidget(), 'successful', '注册成功')
                self.register_panel.pushButton_login.click()
    # def force_login(self):
    #     self.show()

    # def get_current_username(self):
    #     return self.user_info['name']

    def get_current_user_info(self):
        return self.user_info


# from login.login import Login
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Login()
    #ex=OrderItem(20)
    ex.show()
    #print(1111)
    sys.exit(app.exec_())