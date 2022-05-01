import functools
from ui.mainwindow.Ui_MyMainWindow import *
from ui.MerchWidget import merchWidget
from ui.buttonWidget import storeManage_widget
from ui.preview_bar import previewBar
from PyQt5.QtWidgets import QMainWindow,QGridLayout,QVBoxLayout,QWidget,QHBoxLayout

class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None,merchlist=[]):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.merchlist = merchlist
        self.previewbar = previewBar.previewBarWidget(self,merchlist)
        self.initLayout()
        self.setSlot()

    def initLayout(self):
        self.previewbar.scrollArea.resize(self.previewbar.scrollAreaWidgetContents.width()+25,self.previewbar.scrollArea.height())
        self.previewbar.show()

    def setSlot(self):
        print("setslot in mainwindow")
        for index,item in enumerate(self.previewbar.merchWidgetlist):
            item.pushButtonDelete.clicked.connect(functools.partial(self.delete_item,index))
            

    def delete_item(self,index):
        print(f"delete : {index}")
        print(self.merchlist.pop(index))
        new_previewBar = previewBar.previewBarWidget(self,self.merchlist)
        self.previewbar.deleteLater()
        self.previewbar = new_previewBar
        self.initLayout()
        self.setSlot()