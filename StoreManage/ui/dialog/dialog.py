from ui.dialog.Ui_dialog import *
from PyQt5.QtWidgets import QDialog
from ui.updatePage.updatePage import * 
import functools

class Dialog(QDialog,Ui_Dialog):
    def __init__(self,parent=None,message="",manager=None):
        super().__init__(parent)
        self.setupUi(self)
        self.message=message
        self.manager=manager
        self.setContent()

    def setContent(self):
        self.label.setText(self.message)
