import functools
from ui.updatePage.Ui_updatePage import *
from Merchandise import *
from PyQt5.QtWidgets import QMainWindow,QGridLayout,QVBoxLayout,QWidget,QHBoxLayout,QMessageBox
from PyQt5  import QtCore

class updatePageWidget(QWidget,Ui_Form):
    def __init__(self,parent=None,merch=None,manager=None):
        super().__init__(parent)
        self.setupUi(self)
        self.merch=merch
        self.manager=manager
        self.set_text()
        # self.set_slot()
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
    
    def set_text(self):
        self.nameEdit.setText(f"{self.merch.name}")
        self.priceEdit.setText(f"{self.merch.price}")
        self.numberEdit.setText(f"{self.merch.number}")
        
        return

    def submit_Info(self):
        if not self.check_valid("str",self.nameEdit.text()):
            self.box=QMessageBox(text="商品名称不合法,修改失败")
            self.box.setWindowTitle("警告")
            self.box.exec()
            print("flase")
            return False
        if not self.check_valid("number",self.priceEdit.text()):
            self.box=QMessageBox(text="商品价格不合法，修改失败")
            self.box.setWindowTitle("警告")        
            self.box.exec()
            print("flase")
            return False
        if not self.check_valid("number",self.numberEdit.text()):
            self.box=QMessageBox(text="商品库存量不合法，修改失败")
            self.box.setWindowTitle("警告")
            self.box.exec()
            print("flase")
            return False
        self.merch.name=self.nameEdit.text()
        self.merch.price=self.priceEdit.text()
        self.merch.number=self.numberEdit.text()

        self.manager.update_merchandise(self.merch)

        print("submit info")
        return True

    def check_valid(self,mode,str):
        print(str)
        if mode =="number":
            if not self.is_number(str):
                return False
        return True

    def is_number(self,s):
        try:
            float(s)
            return True
        except ValueError:
            pass
        return False