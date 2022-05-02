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
        self.previewbar = previewBar.previewBarWidget(self,merchlist)
        self.buttonwidget = storeManage_widget.storeManage_widget(self)
        self.layout = QHBoxLayout()
        self.centralwidget.setLayout(self.layout)
        self.initLayout()
        self.setSlot()

    def initLayout(self):

        self.previewbar.scrollArea.resize(self.previewbar.scrollAreaWidgetContents.width()+25,self.previewbar.scrollArea.height())
        self.layout.addWidget(self.previewbar)
        self.layout.addWidget(self.buttonwidget)

        self.previewbar.show()

    def setSlot(self):
        print("setslot in mainwindow")
        for index,item in enumerate(self.previewbar.merchWidgetlist):
            item.pushButtonDelete.clicked.connect(functools.partial(self.delete_item,index))
            item.pushButtonUpdate.clicked.connect(functools.partial(self.gen_updatePage,self.merchlist[index]))
            

    def delete_item(self,index):
        print(f"delete : {index}")
        print(self.merchlist.pop(index))
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
        self.show()
        self.page.submit_Info()
        self.page.deleteLater()

        new_previewBar = previewBar.previewBarWidget(self,self.merchlist)
        self.previewbar.deleteLater()
        self.previewbar = new_previewBar
        self.initLayout()
        self.setSlot()

    def page_cancel(self):
        self.page.deleteLater()

        new_previewBar = previewBar.previewBarWidget(self,self.merchlist)
        self.previewbar.deleteLater()
        self.previewbar = new_previewBar
        self.initLayout()
        self.setSlot()
        self.show()
        
