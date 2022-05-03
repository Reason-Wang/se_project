from asyncio.windows_events import NULL
import functools
from ui.mainwindow.Ui_MyMainWindow import *
from ui.MerchWidget import merchWidget
from ui.buttonWidget import storeManage_widget
from ui.preview_bar import previewBar
from ui.updatePage import updatePage
from PyQt5.QtWidgets import QMainWindow,QGridLayout,QVBoxLayout,QWidget,QHBoxLayout

class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None,merchlist=[],manager=None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.merchlist = merchlist
        self.manager= manager
        self.previewbar = previewBar.previewBarWidget(parent=self,merchlist=merchlist,manager=self.manager)
        self.buttonwidget = storeManage_widget.storeManage_widget(parent=self,manager=self.manager)
        self.layout = QHBoxLayout()
        self.centralwidget.setLayout(self.layout)
        self.mylayout=NULL
        self.initLayout()
        self.setSlot()

    def initLayout(self):
        if self.mylayout:
            self.mylayout.deleteLater()
        self.mylayout = QHBoxLayout()
        self.layout.addLayout(self.mylayout)
        print(self.layout.count())
        self.mylayout.addWidget(self.previewbar)
        self.mylayout.addWidget(self.buttonwidget)
        
        self.mylayout.setStretch(2,1)
        print(self.previewbar.size())
        print(self.buttonwidget.size())


    def setSlot(self):
        print("setslot in mainwindow")
        for index,item in enumerate(self.previewbar.merchWidgetlist):
            item.pushButtonDelete.clicked.connect(functools.partial(self.delete_item,index))
            item.pushButtonUpdate.clicked.connect(functools.partial(self.gen_updatePage,self.merchlist[index]))
            

    def delete_item(self,index):
        print(f"delete : {index}")

        self.manager.delete_merchandise_byOBJ(self.merchlist.pop(index))
        self.merchlist = self.manager.merchandise_list

        new_previewBar = previewBar.previewBarWidget(self,self.merchlist,self.manager)
        self.previewbar.deleteLater()
        self.previewbar = new_previewBar
        self.initLayout()
        self.setSlot()
    
    def gen_updatePage(self,merch):
        self.hide()
        self.page = updatePage.updatePageWidget(parent=None,merch=merch,manager=self.manager)
        self.page.OKpushButton.clicked.connect(self.page_ok)
        self.page.CancelpushButton.clicked.connect(self.page_cancel)
        self.page.show()

    def page_ok(self):
        
        self.page.submit_Info()
        self.page.deleteLater()

        self.merchlist = self.manager.merchandise_list
        new_previewBar = previewBar.previewBarWidget(self,self.merchlist)
        self.previewbar.deleteLater()
        self.previewbar = new_previewBar
        self.initLayout()
        self.setSlot()
        self.show()

    def page_cancel(self):
        self.page.deleteLater()

        new_previewBar = previewBar.previewBarWidget(self,self.merchlist)
        self.previewbar.deleteLater()
        self.previewbar = new_previewBar
        self.initLayout()
        self.setSlot()
        self.show()
        
