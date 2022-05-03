from ui.MerchWidget.Ui_merchWidget import *
from PyQt5.QtWidgets import QWidget,QGridLayout

class merchWidget(QWidget,Ui_Form):
    def __init__(self,parent=None,merch=None,manager=None):
        super().__init__(parent)
        self.setupUi(self)
        self.manager = manager
        self.set_content(merch)
        self.print_size()
    
    def set_content(self,merch):
        self.namelable.setText(str(merch.name))
        self.pricelabel.setText(str(merch.price))
        self.numberlabel.setText(str(merch.number))

    def print_size(self):
        # print(self.width(),self.height())
        return