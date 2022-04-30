from ui_file.Ui_checkOrder import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from myUtils import *


class CheckOrder(QMainWindow,Ui_MainWindow):
    def __init__(self,cus_acc,id_dict):
        super().__init__()
        self.setupUi(self)
    def show(self):
        super().show()