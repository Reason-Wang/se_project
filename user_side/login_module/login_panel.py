from login_module.ui_login_panel import Ui_Form

from PyQt5.QtWidgets import QWidget

class LoginPanel(QWidget, Ui_Form):
    def __init__(self):
        super(LoginPanel, self).__init__()
        self.setupUi(self)