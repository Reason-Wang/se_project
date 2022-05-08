from ui.MerchWidget.Ui_merchWidget import *
from PyQt5.QtWidgets import QWidget,QGridLayout
from PyQt5.QtGui import QPixmap
from io import BytesIO
import os
from PIL import Image,ImageQt
from utils_for_store.db_utils import *

class merchWidget(QWidget,Ui_Form):

    pic_data_cache = {}
    def __init__(self,parent=None,merch=None,manager=None):
        super().__init__(parent)
        self.setupUi(self)
        self.manager = manager
        self.merch=merch
        self.set_content(merch)
        self.print_size()
        self.draw_picture()
    
    def set_content(self,merch):
        if merch:
            self.namelable.setText(f"商品名称：{str(merch.name)}")
            self.pricelabel.setText(f"商品价格：{str(merch.price)}")
            self.numberlabel.setText(f"商品库存：{str(merch.number)}")
            self.label_5.setText(f"商品种类：{str(merch.cat)}")

    def print_size(self):
        # print(self.width(),self.height())
        return

    def draw_picture(self):
        print(f"cache : {merchWidget.pic_data_cache}")
        if merchWidget.pic_data_cache.__contains__(self.merch.pic_id):
            print("have")
            self.path = merchWidget.pic_data_cache[self.merch.pic_id]
        else:
            print("not have")
            self.picture.setText("尚未设置图片")
            return 
        self.pixmap=QPixmap(self.path)
        print(self.merch.toCell(),self.pixmap.height(),self.pixmap.width())
        self.pixmap=self.pixmap.scaled(self.picture.width(),self.picture.height())
        print(self.merch.toCell(),self.pixmap.height(),self.pixmap.width())
        self.picture.setPixmap(self.pixmap)

        # io 模式
        # print(f"cache : {merchWidget.pic_data_cache}")
        # if merchWidget.pic_data_cache.__contains__(self.merch.pic_id):
        #     print("have")
        #     self.data = merchWidget.pic_data_cache[self.merch.pic_id]
        # else:
        #     print("not have")
        #     self.picture.setText("尚未设置图片")
        #     return 
        
        # print(len(BytesIO(self.data).getvalue()))
        # self.data=BytesIO(self.data)
        # self.pixmap=ImageQt.toqpixmap(Image.open(self.data))
        # print(self.merch.toCell(),self.pixmap.height(),self.pixmap.width())
        # # self.pixmap=self.pixmap.scaled(self.picture.width(),self.picture.height())
        # print(self.merch.toCell(),self.pixmap.height(),self.pixmap.width())
        # self.picture.setPixmap(self.pixmap)
