from ui.tongji.Ui_tongji import *
from PyQt5.QtWidgets import QMainWindow,QGridLayout,QVBoxLayout,QWidget,QHBoxLayout



class tongjiWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None,merchlist=None,manager=None):
        super().__init__(parent)
        self.setupUi(self)
        self.manager = manager
        self.order_list = self.manager.get_order_list()
        self.pushButton.clicked.connect(self.tongji)

    def tongji(self):
        year = self.lineEdit.text()
        month = self.lineEdit_2.text()
        day = self.lineEdit_3.text()
        target = '-'.join([year,month,day])
        resutl = []
        total=0
        for item in self.order_list:
            if str(item[9])==target:
                resutl.append(str(item))
                if item[6]=="已付款":
                    total =total +item[8]
        self.plainTextEdit.setPlainText(f'{target}  总销售额为: {total}\n' + "\n".join(resutl))

    def info_update(self,merch):
        merch.info = self.plainTextEdit.toPlainText()
        self.manager.update_merchandise(merch)
        self.deleteLater()