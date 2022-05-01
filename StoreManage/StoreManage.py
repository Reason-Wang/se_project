import sys
import Merchandise
from ui.mainwindow import MyMainWindow

from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow


if __name__ == '__main__':
    manager = Merchandise.Merchandise_Manage()

    app = QApplication(sys.argv)
    mainwindow = MyMainWindow.MyMainWindow(parent=None,merchlist=manager.merchandise_list)
    mainwindow.show()
    app.exec_() 