import functools
import os
from StoreManage.ui import MerchWidget
from ui.mainwindow.Ui_MyMainWindow import *
from ui.MerchWidget import merchWidget
from ui.buttonWidget import storeManage_widget
from ui.preview_bar import previewBar
from ui.updatePage import updatePage
from ui.tongji import tongji
from ui.dialog import dialog
from PyQt5.QtWidgets import QMainWindow,QGridLayout,QVBoxLayout,QWidget,QHBoxLayout,QMessageBox,QFileDialog

class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None,merchlist=[],manager=None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.merchlist = merchlist
        self.manager= manager
        # self.load()

    
    def load(self):
        self.previewbar = previewBar.previewBarWidget(parent=self,merchlist=self.merchlist,manager=self.manager)
        self.buttonwidget = storeManage_widget.storeManage_widget(parent=self,manager=self.manager)
        self.layout = QHBoxLayout()
        self.centralwidget.setLayout(self.layout)
        self.mylayout=None
        self.dialog = None
        self.initLayout()
        self.buttonwidget.pushButton_fresh.clicked.connect(self.refresh)

    def refresh(self):
        if previewBar.previewBarWidget.flag==0:
            self.previewbar.init_layout()
            self.buttonwidget.delete_pushButton.clicked.connect(self.delete_merch)
            self.buttonwidget.insert_pushButton.clicked.connect(self.insert_merch)
            self.buttonwidget.updata_pushButton.clicked.connect(self.update_merch)
            self.buttonwidget.tongji_pushButton.clicked.connect(self.buttonwidget.tongji)
            self.previewbar.pushButtonSerch.clicked.connect(self.serch)
            self.setSlot()
        else:
            # self.merchlist = self.manager.merchandise_list
            # new_previewBar = previewBar.previewBarWidget(self,self.merchlist,self.manager)
            # self.previewbar.deleteLater()
            # self.previewbar = new_previewBar
            # self.initLayout()
            self.previewbar.init_layout()
            self.setSlot()

    def serch(self):
        self.previewbar.serch()
        self.setSlot()

    def initLayout(self):
        if self.mylayout:
            self.mylayout.deleteLater()
        # if self.dialog:
        #     self.dialog.deleteLater()
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
            item.pushButtonDelete.clicked.connect(functools.partial(self.delete_item,index,merch_id=None))
            item.pushButtonUpdate.clicked.connect(functools.partial(self.gen_updatePage,self.merchlist[index]))
            item.pushButtonUpdatePIC.clicked.connect(functools.partial(self.file,self.merchlist[index]))
            item.pushButton.clicked.connect(functools.partial(self.show_info,self.merchlist[index]))
        # self.buttonwidget.delete_pushButton.clicked.connect(self.delete_merch)
        # self.buttonwidget.insert_pushButton.clicked.connect(self.insert_merch)
        # self.buttonwidget.updata_pushButton.clicked.connect(self.update_merch)


            

    def delete_item(self,index,merch_id=None):
        if merch_id==None:
            print(f"delete : {index}")
            self.manager.delete_merchandise_byOBJ(self.merchlist.pop(index))
        else:
            print(f"delete merch_id{merch_id}")
            self.manager.delete_merchandise(merch_id)

        self.merchlist = self.manager.merchandise_list
        self.previewbar.setMerchWidger_content()

        # self.merchlist = self.manager.merchandise_list
        # new_previewBar = previewBar.previewBarWidget(self,self.merchlist,manager=self.manager)
        # self.previewbar.deleteLater()
        # self.previewbar = new_previewBar
        self.previewbar.init_layout()
        self.setSlot()
        self.show()
    
    def gen_updatePage(self,merch):
        self.hide()
        self.page = updatePage.updatePageWidget(parent=None,merch=merch,manager=self.manager)
        self.page.OKpushButton.setText("更新")
        self.page.OKpushButton.clicked.connect(self.page_ok)
        self.page.CancelpushButton.clicked.connect(self.page_cancel)
        self.page.show()

    def page_ok(self):
        print("page_ok")
        self.page.submit_Info()
        self.page.deleteLater()

        
        
        self.merchlist = self.manager.merchandise_list
        self.previewbar.setMerchWidger_content()

        # self.merchlist = self.manager.merchandise_list
        # new_previewBar = previewBar.previewBarWidget(self,self.merchlist,manager=self.manager)
        # self.previewbar.deleteLater()
        # self.previewbar = new_previewBar
        self.previewbar.init_layout()
        self.setSlot()
        self.show()

    def page_cancel(self):
        print("page_cancel")
        self.page.deleteLater()

        # new_previewBar = previewBar.previewBarWidget(self,self.merchlist,manager=self.manager)
        # self.previewbar.deleteLater()
        # self.previewbar = new_previewBar

        self.merchlist = self.manager.merchandise_list
        self.previewbar.setMerchWidger_content()
        self.initLayout()
        # self.setSlot()
        self.show()
        
    def update_merch(self):
        print(self.dialog)
        print("update")
        self.dialog = dialog.Dialog(None,"请输入商品ID",manager=self.manager)
        self.dialog.pushButton_ok.clicked.connect(self.dialog_ok)
        self.dialog.pushButton_2.clicked.connect(self.dialog.deleteLater)
        self.dialog.show()

    def dialog_ok(self):
        merch_id = self.dialog.textEdit.toPlainText()
        if len(merch_id)==0:
            message = QMessageBox(text="商品ID不能为空")
            message.setWindowTitle("警告")
            message.exec()
        else:
            try:
                merch_id=int(merch_id)
                merchan = self.manager.serch_merchandise(merch_id)
                if(merchan):
                    self.gen_updatePage(merch=merchan)
                else:
                    message = QMessageBox(text="此商品不存在")
                    message.setWindowTitle("警告")
                    message.exec()
            except ValueError:
                message = QMessageBox(text="商品ID必须为正整数")
                message.setWindowTitle("警告")
                message.exec()


    def insert_merch(self):
        self.gen_updatePage(merch=None)
        self.page.OKpushButton.setText("上架")
        

    def delete_merch(self):
        print(self.dialog)
        print("delete")
        self.dialog = dialog.Dialog(None,"请输入要下架的商品ID",manager=self.manager)
        self.dialog.pushButton_ok.clicked.connect(self.dialog_delete_ok)
        self.dialog.pushButton_2.clicked.connect(self.dialog.deleteLater)
        self.dialog.show()

    def dialog_delete_ok(self):
        merch_id = self.dialog.textEdit.toPlainText()
        if len(merch_id)==0:
            message = QMessageBox(text="商品ID不能为空")
            message.setWindowTitle("警告")
            message.exec()
        else:
            try:
                merch_id=int(merch_id)
                if self.manager.serch_merchandise(merch_id=merch_id)==None:
                    message = QMessageBox(text="此商品不存在")
                    message.setWindowTitle("警告")
                    message.exec()
                else:
                    self.delete_item(index=-1,merch_id=merch_id)
            except ValueError:
                message = QMessageBox(text="商品ID必须为正整数")
                message.setWindowTitle("警告")
                message.exec()


    def show_info(self,merch):
        self.info = tongji.tongjiWindow(parent= self,manager=self.manager)
        self.info.label.hide()
        self.info.label_2.hide()
        self.info.label_3.hide()
        self.info.lineEdit.hide()
        self.info.lineEdit_2.hide()
        self.info.lineEdit_3.hide()
        self.info.pushButton.setText("上传")
        self.info.plainTextEdit.setPlainText(merch.info)
        self.info.pushButton.clicked.disconnect(self.info.tongji)
        self.info.pushButton.clicked.connect(functools.partial(self.info.info_update,merch))
        self.info.show()

    def file(self,merch):
        print("file")
        filename=QFileDialog.getOpenFileNames(self,'选择图像',os.getcwd(), "png Files(*.png)")
        if len(filename[0]):
            print(f"{filename[0][0]}")
            st = filename[0][0].split('/')[-1]
            print(st)
            merch.pic_id = self.manager.upload_img(filename[0][0],st)
            print(merch.pic_id)
            self.manager.update_merchandise(merch)

            # self.merchlist = self.manager.merchandise_list
            # new_previewBar = previewBar.previewBarWidget(self,self.merchlist,self.manager)
            # self.previewbar.deleteLater()
            # self.previewbar = new_previewBar
            merchWidget.merchWidget.pic_data_cache[merch.pic_id] = filename[0][0]
            self.merchlist = self.manager.merchandise_list
            self.previewbar.setMerchWidger_content()
            self.initLayout()
            # self.setSlot()