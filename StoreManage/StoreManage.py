import sys
import os
path = os.path.abspath('.')+r'\StoreManage'
sys.path.append(path)
from StoreManage import Merchandise
from ui.mainwindow import MyMainWindow

from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow


if __name__ == '__main__':
    manager = Merchandise.Merchandise_Manage()

    app = QApplication(sys.argv)
    mainwindow = MyMainWindow.MyMainWindow(parent=None,merchlist=manager.merchandise_list,manager=manager)
    mainwindow.show()
    app.exec_() 


def show_mainwindow():
    
    manager = Merchandise.Merchandise_Manage()

    app = QApplication(sys.argv)
    mainwindow = MyMainWindow.MyMainWindow(parent=None,merchlist=manager.merchandise_list,manager=manager)
    mainwindow.show()
    app.exec_() 

def set_DatabaseSlot(mainwindow):
    return
    # mainwindow.
