
from ui.buttonWidget.Ui_storeManage import *
from ui.tongji import tongji
from PyQt5.QtWidgets import QWidget

class storeManage_widget(QWidget,Ui_Form):
    def __init__(self,parent=None,manager=None):
        super().__init__(parent)
        self.manager= manager
        self.setupUi(self)
        self.setup_slot()

    def setup_slot(self):
        print("setup_slot in widget")        
      

    def showINFO(self):
        print(self.sender())

    def tongji(self):
        self.window  = tongji.tongjiWindow(manager=self.manager)
        self.window.show()
