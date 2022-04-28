from storeManage_ui import Ui_storeManage
from PyQt5.QtWidgets import QWidget

class storeManage_widget(QWidget,Ui_storeManage.Ui_Form):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
