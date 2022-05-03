from ui.preview_bar.Ui_previewBar import *
from ui.MerchWidget import merchWidget
from PyQt5.QtWidgets import QMainWindow,QGridLayout,QVBoxLayout,QWidget,QHBoxLayout

class previewBarWidget(QWidget,Ui_Form):
    def __init__(self,parent=None,merchlist=None,manager=None):
        super().__init__(parent)
        self.setupUi(self)
        self.merchWidgetlist=[]
        self.merchlist=merchlist
        self.manager = manager
        self.setup_slot()
        self.init_layout()
        
    def init_layout(self):
        self.layout = QGridLayout()
        self.scrollAreaWidgetContents.setLayout(self.layout)
        self.addMerch()

    def setup_slot(self):
        print("setup_slot in mainwindow")
        self.scrollArea.size

    def addMerch(self):
        for index,item in enumerate(self.merchlist):
            # print(item.toCell())
            self.merchWidgetlist.append(merchWidget.merchWidget(parent=self,merch=item))
            self.layout.addWidget(self.merchWidgetlist[index])
            # print(f"index:{index}")
            # self.scrollArea.resize((self.merchWidgetlist[index].width()+50),self.scrollArea.height())
            self.scrollAreaWidgetContents.resize((self.merchWidgetlist[index].width()+50),(index+1)*(self.merchWidgetlist[index].height()+25))


        