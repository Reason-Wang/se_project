from ui_mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from example_module.example_widget import ExampleWidget
from orderManage_module.cart import Cart
from usershow.setUsershow import myusershow
from login_module.login import Login
from PyQt5 import QtCore


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)

        # usage of example widget
        # self.example_widget = ExampleWidget()
        # self.pushButton_OK.clicked.connect(self.example_widget.show)

        self.login = Login()
        self.pushButton_login.clicked.connect(self.login.show)
        self.login.exec_()
        self.login.switch_user_signal.connect(self.switch_user)


        self.set_display_info()
        user_info = self.login.get_current_user_info()

        print(user_info)
        # user_name = '20191234'


        self.display = myusershow()
        self.display.change_account(user_info['name'])
        self.scrollArea_display.setWidget(self.display)

        self.cart_order=Cart()
        self.cart_order.changeAccount(user_info['name'])
        self.pushButton_cart.clicked.connect(self.cart_order.show)

    def set_display_info(self):
        user_info = self.login.get_current_user_info()
        self.label_user.setText(user_info['name'])
        self.label_phone.setText(user_info['phone'])
        self.label_address.setText(user_info['address'])

    def switch_user(self):
        self.set_display_info()
        user_info = self.login.get_current_user_info()
        self.display.change_account(user_info['name'])
        self.cart_order.changeAccount(user_info['name'])

    def show(self):
        super(MainWindow, self).show()
