from login_module.ui_register_panel import Ui_Form

from PyQt5.QtWidgets import QWidget

class RegisterPanel(QWidget, Ui_Form):
    def __init__(self):
        super(RegisterPanel, self).__init__()
        self.setupUi(self)