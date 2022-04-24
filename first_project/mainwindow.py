from ui_mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from example_module.example_widget import ExampleWidget

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)

        # usage of example widget
        self.example_widget = ExampleWidget()
        self.pushButton_OK.clicked.connect(self.example_widget.show)


    def show(self):
        super(MainWindow, self).show()
