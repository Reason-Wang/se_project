from ast import Delete
from ui.preview_bar.Ui_previewBar import *
from ui.MerchWidget import merchWidget
from PyQt5.QtWidgets import QMainWindow,QGridLayout,QVBoxLayout,QWidget,QHBoxLayout
from io import BytesIO
import os

class previewBarWidget(QWidget,Ui_Form):
    flag = 0
    def __init__(self,parent=None,merchlist=None,manager=None):
        super().__init__(parent)
        self.setupUi(self)
        self.merchWidgetlist=[]
        self.merchlist=merchlist
        self.manager = manager
        self.mylayout=None
        previewBarWidget.flag=0
        self.setup_slot()
        self.init_cache()
        # self.init_layout()

    def init_layout(self):
        if previewBarWidget.flag==0:
            self.pre_layout = QGridLayout()
            self.scrollAreaWidgetContents.setLayout(self.pre_layout)
            self.addMerch()
            previewBarWidget.flag=1
        else:
            self.addMerch()

    def init_cache(self):
        self.data_tmp = self.manager.get_picture_data(None)
        print(f"data_tmp  :  {self.data_tmp}")
        path = os.path.abspath('.')+r'\StoreManage\pic' + '\\'
        for item in self.data_tmp:
            filename = f'{item[2]}'
            fout = open(path+filename, 'wb')
            fout.write(item[1])
            merchWidget.merchWidget.pic_data_cache[item[0]]=path+filename

    def setup_slot(self):
        print("setup_slot in mainwindow")
        self.scrollArea.size

    def addMerch(self):
        item_list = list(range(self.pre_layout.count()))
        item_list.reverse()# 倒序删除，避免影响布局顺序
        for i in item_list:
            item = self.pre_layout.itemAt(i)
            self.pre_layout.removeItem(item)
            if item.widget():
                item.widget().deleteLater()
        self.merchlist= self.manager.merchandise_list
        self.merchWidgetlist=[]
        for index,item in enumerate(self.merchlist):
            # print(item.toCell())
            self.merchWidgetlist.append(merchWidget.merchWidget(parent=self,merch=item,manager=self.manager))
            self.pre_layout.addWidget(self.merchWidgetlist[index])
            # print(f"index:{index}")
            # self.scrollArea.resize((self.merchWidgetlist[index].width()+50),self.scrollArea.height())
            self.scrollAreaWidgetContents.resize((self.merchWidgetlist[index].width()+50),(index+1)*(self.merchWidgetlist[index].height()+25))
    
    def setMerchWidger_content(self):
        for index,item in enumerate(self.merchlist):
            self.merchWidgetlist[index].set_content(item)
            self.merchWidgetlist[index].set_content(item)
            self.merchWidgetlist[index].draw_picture()

    def serch(self):
        target = self.plainTextEdit.toPlainText()
        result = []
        for index,item in enumerate(self.merchlist):
            if item.cat.find(target) != -1:
                result.append(item)
        item_list = list(range(self.pre_layout.count()))
        item_list.reverse()# 倒序删除，避免影响布局顺序
        for i in item_list:
            item = self.pre_layout.itemAt(i)
            self.pre_layout.removeItem(item)
            if item.widget():
                item.widget().deleteLater()
        self.merchlist =  result
        if target == "":
            self.merchlist =  self.manager.merchandise_list
        self.merchWidgetlist=[]
        for index,item in enumerate(self.merchlist):
            self.merchWidgetlist.append(merchWidget.merchWidget(parent=self,merch=item,manager=self.manager))
            self.pre_layout.addWidget(self.merchWidgetlist[index])
            self.scrollAreaWidgetContents.resize((self.merchWidgetlist[index].width()+50),(index+1)*(self.merchWidgetlist[index].height()+25))
        