
from ui.mainwindow.Ui_MyMainWindow import *
from ui.MerchWidget import merchWidget
from ui.buttonWidget import storeManage_widget
from PyQt5.QtWidgets import QMainWindow,QGridLayout,QVBoxLayout,QWidget,QHBoxLayout

class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None,merchlist=[]):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.merchWidgetlist=[]
        self.merchlist=merchlist
        self.setup_slot()
        self.init_layout()
        
    def init_layout(self):
        self.layout = QGridLayout()
        self.scrollAreaWidgetContents.setLayout(self.layout)
        self.addMerch()
        self.setMerch_slot()

    def setup_slot(self):
        print("setup_slot in mainwindow")


    def addMerch(self):
        for index,item in enumerate(self.merchlist):
            print(item.toCell())
            self.merchWidgetlist.append(merchWidget.merchWidget(parent=self,merch=item))
            self.layout.addWidget(self.merchWidgetlist[index])
            print(f"index:{index}")
            self.scrollAreaWidgetContents.resize(index*(self.merchWidgetlist[index].width()+50),index*(self.merchWidgetlist[index].height()+50))

    def setMerch_slot(self):
        print("setMerch_slot")
        for index,item in enumerate(self.merchWidgetlist):
            item.pushButtonDelete.clicked.connect(lambda index=index:self.delete_merch(index))
            item.pushButtonUpdate.clicked.connect(lambda index=index:self.delete_merch(index))

    def delete_merch(self,index):
        self.merchlist.pop(index)
        item = self.merchWidgetlist.pop(index)
        # item.delete()

        self.init_layout()