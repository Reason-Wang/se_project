from regex import D
from ui.updatePage.Ui_updatePage import *
from Merchandise import *
from PyQt5.QtWidgets import QMainWindow,QGridLayout,QVBoxLayout,QWidget,QHBoxLayout

class updatePageWidget(QWidget,Ui_Form):
    def __init__(self,parent=None,merch=None):
        super().__init__(parent)
        self.setupUi(self)
    
    def set_text(self):
        return

    def submit_Info(self):
        print("submit info")
        return