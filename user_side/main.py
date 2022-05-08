# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import PyQt5
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainwindow import MainWindow
from ui_mainwindow import Ui_MainWindow


from qt_material import apply_stylesheet
import qdarkstyle
from qdarkstyle.light.palette import LightPalette

# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    # if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    #     PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    #
    # if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    #     PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    window = MainWindow()
    # apply_stylesheet(app, theme='dark_teal.xml')
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=LightPalette()))
    window.show()

    sys.exit(app.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
