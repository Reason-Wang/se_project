from ui.MerchWidget.Ui_merchWidget import *
from PyQt5.QtWidgets import QWidget,QGridLayout
from io import BytesIO
from PIL import Image,ImageQt

class merchWidget(QWidget,Ui_Form):
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
            self.namelable.setText(str(merch.name))
            self.pricelabel.setText(str(merch.price))
            self.numberlabel.setText(str(merch.number))
            self.label_5.setText(str(merch.cat))

    def print_size(self):
        # print(self.width(),self.height())
        return

    def draw_picture(self):
        data = self.manager.get_picture_data(self.merch.pic_id)
        print(data)
        self.pixmap=ImageQt.toqpixmap(Image.open(BytesIO(data[0][1])))
        print(self.pixmap.height(),self.pixmap.width())
        self.pixmap.scaled(self.picture.width(),self.height())
        self.picture.setPixmap(self.pixmap)
        fout = open(f'{self.merch.name}.jpg', 'wb')
        fout.write(data[0][1])