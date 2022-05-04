import math
from io import BytesIO
from PIL import Image,ImageQt
from moretag import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import functools
from mydb_utiles import*
import ast
class Cart(QMainWindow,Ui_MainWindow):#购物车页面
    button_clicked_signal2 = pyqtSignal()
    button_clicked_signal3 = pyqtSignal()
    def __init__(self,cus_acc):
        super().__init__()
        self.account=cus_acc
        self.setupUi(self)
        self.initUI()
        self.stackedWidget.setCurrentIndex(0)
        self.show()
    def initUI(self):
        self.connection = create_connection('se', 'hc', '123456', remote_host, 5432)
        self.connection.autocommit=True
        self.mycart.clicked.connect(lambda:self.toCart(self.account))
        self.mything.clicked.connect(self.toMything)
        self.homepage.clicked.connect(self.myreturn)
        self.cart_dict={}
        self.getCart(self.account)
        print(self.cart_dict)
        self.button_clicked_signal2.connect(lambda: self.mytag_clicked(1))
        self.button_clicked_signal3.connect(lambda: self.toCart(self.account))
        searchpng = QPixmap('img.png')
        self.searchlabel.setFixedSize(20, 20)
        self.searchlabel.setPixmap(searchpng)
        self.searchlabel.setScaledContents(True)
        self.searchEdit.setPlaceholderText("请输入要查询的商品名称")
        self.searchbutton.clicked.connect(self.search_clicked)
        self.shownname = [self.showbar.nameout1, self.showbar.nameout2, self.showbar.nameout3,
                             self.showbar.nameout4, self.showbar.nameout5, self.showbar.nameout6]
        self.shownmerchan = [self.showbar.imageout1, self.showbar.imageout2, self.showbar.imageout3,
                             self.showbar.imageout4, self.showbar.imageout5, self.showbar.imageout6]
        self.shownprice = [self.showbar.priceout1, self.showbar.priceout2, self.showbar.priceout3,
                             self.showbar.priceout4, self.showbar.priceout5, self.showbar.priceout6]
        self.merout=list(zip(self.shownname,self.shownmerchan,self.shownprice,range(len(self.shownprice))))
        self.showntag = [self.showbar.tag1, self.showbar.tag2, self.showbar.tag3, self.showbar.tag4, self.showbar.tag5, self.showbar.tag6]
        for i,j in zip(self.showntag,range(len(self.showntag))):
            i.connect_customized_slot(functools.partial(self.mytag_clicked,j))
        for i, j in zip(self.shownmerchan, range(len(self.shownmerchan))):
            i.connect_customized_slot(functools.partial(self.merdetail, j))
        self.alltags = ["零食", "饮料", "生活用品", "饼干", "面包", "水果", "康师傅", "桃李", "精美文具", "家具","传统","西方"]
        self.perpagenum = 6
        self.merchannum = execute_read_query(self.connection, 'SELECT COUNT(*) from hccmer')
        self.all_page = math.ceil(self.merchannum[0][0] / self.perpagenum)
        self.totalPage.setText("共 " + str(self.all_page) + " 页")
        result = execute_read_query(self.connection,"SELECT * FROM hccmer")
        self.merchandise = [[[0, "", "", 0, "",""] for i in range(self.perpagenum)] for i in range(self.all_page)]
        print(self.merchandise)
        k=0
        for i in range(self.all_page):
            for j in range(self.perpagenum):
                if (k < self.merchannum[0][0]):
                    self.merchandise[i][j] = result[k]
                    k = k + 1
        self.allmerchandise=self.merchandise
        self.maxpage=self.all_page
        self.prePage.clicked.connect(self.page_clicked)
        self.nextPage.clicked.connect(self.page_clicked)
        self.confirmSkip.clicked.connect(self.page_clicked)
        self.labellist = list()
        self.showpage()

    def page_clicked(self):
        button_text = self.sender().text()
        total_page = int(self.totalPage.text().split()[1])
        current_page = int(self.curPage.text())
        if (self.curPage.text() == '0'):
            return
        if "<上一页" == button_text:
            self.skipPage.setText('')
            current_page = current_page - 1
            if current_page <= 1:
                self.curPage.setText('1')
            else:
                self.curPage.setText(str(current_page))
        if "下一页>" == button_text:
            self.skipPage.setText('')
            current_page = current_page + 1
            if current_page <= total_page:
                self.curPage.setText(str(current_page))
        if "确定" == button_text:
            if '' == self.skipPage.text():
                return

            page = int(self.skipPage.text())
            if 1 <= page <= total_page:
                self.curPage.setText(str(page))
            if page > total_page:
                self.curPage.setText(str(total_page))
                self.skipPage.setText(str(total_page))
            if page <= 0:
                self.curPage.setText(str(1))
                self.skipPage.setText(str(1))
        self.showpage()

    def search_clicked(self):
        if '' == self.searchEdit.text():
            return
        for i in self.showntag:
            i.setStyleSheet("color:black")
        self.skipPage.setText('')
        self.curPage.setText(str(1))
        print("anccc")
        self.merchannum = execute_read_query(self.connection,
                                             "SELECT count(*) FROM hccmer WHERE hccmer.name LIKE '%%%%%s%%%%'" % self.searchEdit.text())
        self.all_page = math.ceil(self.merchannum[0][0] / self.perpagenum)
        print(self.all_page)
        if (self.merchannum[0][0] > 0):
            result = execute_read_query(self.connection,
                                        "SELECT * FROM hccmer WHERE hccmer.name LIKE '%%%%%s%%%%'" % self.searchEdit.text())
            k = 0
            self.merchandise = [[[0, "", "", 0, "",""] for i in range(self.perpagenum)] for i in range(self.all_page)]
            print(self.merchandise)
            for i in range(0, self.all_page):
                for j in range(0, self.perpagenum):
                    if (k < self.merchannum[0][0]):
                        if (result[k][1] == self.searchEdit.text()):
                            self.merchandise[i][j] = self.merchandise[0][0]
                            self.merchandise[0][0] = result[k]
                        else:
                            self.merchandise[i][j] = result[k]
                        k = k + 1
            print(self.merchandise)
        else:
            self.curPage.setText('0')
            self.merchandise = [];
        self.totalPage.setText("共 " + str(self.all_page) + " 页")
        self.showpage()

    def showpage(self):
        if (self.curPage.text() != '0'):
            for i in self.merout:
                if(self.merchandise[int(self.curPage.text()) - 1][i[3]][1]!=""):
                    i[1].setFrameShape(QFrame.Box)
                    i[1].setPixmap(ImageQt.toqpixmap(Image.open(BytesIO(self.merchandise[int(self.curPage.text()) - 1][i[3]][5]))))
                else:
                    i[1].setPixmap(QPixmap(""))
                    i[1].setFrameShape(QFrame.NoFrame)
                i[2].setText(str(self.merchandise[int(self.curPage.text()) - 1][i[3]][2]))
                i[0].setText(self.merchandise[int(self.curPage.text()) - 1][i[3]][1])
        else:
            for i in self.merout:
                print("empty！")
                i[1].setPixmap(QPixmap(""))
                i[1].setFrameShape(QFrame.NoFrame)
                i[1].setText("")
                i[2].setText("")
                i[0].setText("")
    def mytag_clicked(self,index):
        for i in self.showntag:
            i.setStyleSheet("color:black")
        self.showntag[index].setStyleSheet("color:blue")
        if(index not in (4,5)):
            self.skipPage.setText('')
            self.curPage.setText(str(1))
            self.merchannum = execute_read_query(self.connection,
                                                 "SELECT count(*) FROM hccmer WHERE hccmer.tag LIKE '%%%%%s%%%%'" % self.showntag[index].text())
            self.all_page = math.ceil(self.merchannum[0][0] / self.perpagenum)
            print(self.all_page)
            if (self.merchannum[0][0] > 0):
                result = execute_read_query(self.connection,
                                            "SELECT * FROM hccmer WHERE hccmer.tag LIKE '%%%%%s%%%%'" % self.showntag[index].text())
                k = 0
                self.merchandise = [[[0, "", "", 0, "",""] for i in range(self.perpagenum)] for i in range(self.all_page)]

                print(self.merchandise)
                for i in range(0, self.all_page):
                    for j in range(0, self.perpagenum):
                        if (k < self.merchannum[0][0]):
                            if (result[k][1] == self.searchEdit.text()):
                                self.merchandise[i][j] = self.merchandise[0][0]
                                self.merchandise[0][0] = result[k]
                            else:
                                self.merchandise[i][j] = result[k]
                            k = k + 1
                print(self.merchandise)
                self.totalPage.setText("共 " + str(self.all_page) + " 页")
                self.showpage()
            else:
                self.curPage.setText('0')
                self.merchandise=[];
                self.totalPage.setText("共 " + str(self.all_page) + " 页")
                self.showpage()

        elif index == 5:
            self.merchandise = self.allmerchandise
            self.all_page = self.maxpage
            self.curPage.setText('1')
            self.totalPage.setText("共 " + str(self.all_page) + " 页")
            self.showpage()
        else:
            colnum=5
            rownum = math.ceil(len(self.alltags) / colnum)
            positions = [(i+1, j) for i in range(rownum) for j in range(colnum)]
            for (position, name) in zip(positions, self.alltags):
                if ((position[0]-1) * colnum + position[1] > len(self.alltags)):
                    break;
                button = QPushButton(self.page_2)
                button.resize(100,80)
                button.setText(name)
                button.clicked.connect(self.choose_tag)
                self.grid.addWidget(button, *position)
                self.stackedWidget.setCurrentIndex(1)
    def choose_tag(self):
        print(self.sender().text());
        for mytag in self.showntag:
            if (mytag.text()==self.sender().text()):
                mytag.setText(self.showntag[1].text())
        self.showntag[1].setText(self.sender().text())
        self.button_clicked_signal2.emit()
        self.stackedWidget.setCurrentIndex(0)
    def getCart(self, cus_acc):
        cart_str=execute_read_query(self.connection, "select cart from acc_cart where cus_acc='%s'" % cus_acc)
        if cart_str==[]:
            print("1")
            self.cart_dict={}
            execute_query(self.connection, "insert INTO acc_cart(cus_acc,cart) values({cus},'{a}')".format(cus=cus_acc,a=str({})))
        else:
            self.cart_dict = ast.literal_eval(cart_str[0][0])
            print(self.cart_dict)

    def changeCart(self, cus_acc, cart_dict):
        execute_query(self.connection,
                      "update acc_cart set cart='{cart_dict}' where cus_acc='{cus_acc}'".format(
                          cart_dict=str(cart_dict), cus_acc=cus_acc))

    def merdetail(self, merindex):
        self.stackedWidget.setCurrentIndex(2)
        self.seemer.returnpage.clicked.connect(self.myreturn)
        self.seemer.merimage.setPixmap(ImageQt.toqpixmap(Image.open(BytesIO(self.merchandise[int(self.curPage.text()) - 1][merindex][5]))))
        self.seemer.merprice.setText(str(self.merchandise[int(self.curPage.text()) - 1][merindex][2]))
        self.seemer.mername.setText(self.merchandise[int(self.curPage.text()) - 1][merindex][1])
        self.seemer.merstorage.setText("剩余"+str(self.merchandise[int(self.curPage.text()) - 1][merindex][3])+"件本商品")
        for j in self.labellist:
            j.setText("")
        self.labellist=list()
        i=self.merchandise[int(self.curPage.text()) - 1][merindex][4].split('，')
        k=0
        for j in i:
                 print(j)
                 dettag=MyQLabel(self.page_3)
                 dettag.setGeometry(QRect(100+100*k, 590, 200, 30))
                 self.labellist.append(dettag)
                 self.labellist[k].show()
                 k=k+1
                 dettag.setText(j)
                 dettag.connect_customized_slot(self.choose_tag)
        self.seemer.addnum.setMaximum(self.merchandise[int(self.curPage.text()) - 1][merindex][3])
        self.seemer.addnum.setMinimum(0)
        self.seemer.addbutton.clicked.connect(lambda:self.add_clicked(merindex))
    def add_clicked(self,merindex):
        if (self.seemer.addnum.value() == 0):
            return
        elif (self.account != ""):
            reply1 = QMessageBox.question(self, 'Message',
                                         "Are you sure to add?", QMessageBox.Yes |
                                         QMessageBox.No, QMessageBox.No)
            if (reply1 == QMessageBox.Yes):
                a = self.merchandise[int(self.curPage.text()) - 1][merindex][0]
                if (a not in self.cart_dict.keys()):
                    self.cart_dict[a] = 0
                self.cart_dict[a] += self.seemer.addnum.value()
                self.statusBar().showMessage("已加入")
                self.seemer.addnum.setValue(0)
                return
            else:
                return
        else:
            reply = QMessageBox.question(self, 'Message',
                                         "你需要登录去使用购物车，是否跳转登录?", QMessageBox.Yes |
                                         QMessageBox.No, QMessageBox.No)
            if (reply == QMessageBox.Yes):
                return
            else:
                return
    def myreturn(self):
        self.seemer.addnum.setValue(0)
        self.mytag_clicked(5)
        self.stackedWidget.setCurrentIndex(0)
        self.statusBar().showMessage("")
    def toCart(self,cus_acc):
        self.statusBar().showMessage("")
        if(cus_acc==""):
            reply = QMessageBox.question(self, 'Message',
                                         "你需要登录去使用购物车，是否跳转登录?", QMessageBox.Yes |
                                         QMessageBox.No, QMessageBox.No)
            if (reply == QMessageBox.Yes):
                return
            else:
                return
        else:
            print(self.cart_dict)
            self.changeCart(cus_acc, self.cart_dict)
            self.getCart(cus_acc)
            print(self.cart_dict)
            return
    def toMything(self):
        return

