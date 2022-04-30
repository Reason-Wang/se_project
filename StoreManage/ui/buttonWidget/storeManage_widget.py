from ui.buttonWidget.Ui_storeManage import *
from PyQt5.QtWidgets import QWidget

class storeManage_widget(QWidget,Ui_Form):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setup_slot()

    def setup_slot(self):
        print("setup_slot in widget")
        self.delete_pushButton.clicked.connect(self.showINFO)
        self.insert_pushButton.clicked.connect(self.showINFO)
        self.updata_pushButton.clicked.connect(self.showINFO)
        

    def showINFO(self):
        print(self.sender())


