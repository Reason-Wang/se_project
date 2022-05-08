from ui_mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from example_module.example_widget import ExampleWidget
from StoreManage import StoreManage
from order_module.order_screen import orderScreen

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)

        # usage of example widget

        # self.example_widget = ExampleWidget()
        # self.pushButton_OK.clicked.connect(self.example_widget.show)

        self.order_screen = orderScreen()
        self.pushButton_order.clicked.connect(self.setScroolArea_order)


        # self.<name> = Class_name
        # self.pushButton_kyn.clicked.connect(self.class_name.show)
        #
        # self. < name > = Class_name
        # self.pushButton_lhd.clicked.connect(self.class_name.show)
        #
        # self. < name > = Class_name
        # self.pushButton_shy.clicked.connect(self.class_name.show)
        self.storemanage = StoreManage.Storemanage()
        self.pushButton_management.clicked.connect(self.setScroolArea_management)

    def show(self):
        super(MainWindow, self).show()

    def setScroolArea_order(self):
        self.scrollArea.takeWidget()
        self.scrollArea.setWidget(self.order_screen)

    def setScroolArea_management(self):
        self.storemanage.set()
        self.scrollArea.takeWidget()
        self.scrollArea.setWidget(self.storemanage.mainwindow)