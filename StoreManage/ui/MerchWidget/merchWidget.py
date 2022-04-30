from ui.MerchWidget.Ui_merchWidget import *
from PyQt5.QtWidgets import QWidget,QGridLayout

class merchWidget(QWidget,Ui_Form):
    def __init__(self,parent=None,merch=None):
        super().__init__(parent)
        self.setupUi(self)
        self.set_content(merch)
    
    def set_content(self,merch):
        print("set_content")
        print(merch.toCell())
        self.namelable.setText(str(merch.name))
        self.pricelabel.setText(str(merch.price))
        self.numberlabel.setText(str(merch.number))