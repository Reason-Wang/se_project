# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import PyQt5
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainwindow import MainWindow
from ui_mainwindow import Ui_MainWindow
from StoreManage import StoreManage


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    # if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    #     PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    # if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    #     PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    # app = QApplication(sys.argv)
    # window = MainWindow()
    # window.show()

    # sys.exit(app.exec_())

    StoreManage.show_mainwindow()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
