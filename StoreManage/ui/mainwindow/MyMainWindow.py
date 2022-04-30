
from ui.mainwindow.Ui_MyMainWindow import *
from ui.MerchWidget import merchWidget
from ui.buttonWidget import storeManage_widget
from PyQt5.QtWidgets import QMainWindow,QGridLayout,QVBoxLayout

class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None,merchlist=[]):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.merchWidgetlist=[]
        self.merchlist=merchlist
        self.layout = QVBoxLayout()
        self.setup_slot()
        self.addMerch()
        self.centralwidget.setLayout(self.layout)

    def setup_slot(self):
        print("setup_slot in mainwindow")
    
    def hide_storeManage(self):
        self.storeManage_widget.hide()

    def addMerch(self):
        for index,item in enumerate(self.merchlist):
            print(item.toCell())
            self.merchWidgetlist.append(merchWidget.merchWidget(parent=self,merch=item))
            self.layout.addWidget(self.merchWidgetlist[index])
            print(f"index:{index}")
            print(len(self.merchWidgetlist))