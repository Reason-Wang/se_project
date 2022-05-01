from ui.preview_bar.previewBar import *
from PyQt5.QtWidgets import QWidget,QGridLayout

class previewBarWidget(QWidget,Ui_Form):
    def __init__(self,parent=None,merch=None):
        super().__init__(parent)
        self.setupUi(self)
        