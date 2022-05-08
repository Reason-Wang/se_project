from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QApplication,QPushButton,QFileDialog
import sys
import os

class File_Select(QtWidgets.QMainWindow,QtWidgets.QWidget):
    def __init__(self):
        super(File_Select, self).__init__()
        QtWidgets.QWidget.__init__(self)
    def initUi(self):
        self.setGeometry(30,30,700,500)
        self.setWindowTitle('选择图像')
        self.button=QPushButton('上传图像',self)
        self.button.setGeometry(550,220,100,30)
        self.button.clicked.connect(self.file)
    def file(self):
        filename=QFileDialog.getOpenFileNames(self,'选择图像',os.getcwd(), "All Files(*);;Text Files(*.txt)")
        print(f"{filename[0][0]}")

    #重写关闭Mmainwindow窗口
    # def closeEvent(self, event):
    #     replp=QtWidgets.QMessageBox.question(self,u'警告',u'确认退出?',QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
    #     if replp==QtWidgets.QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()

if __name__=='__main__':
    app=QApplication(sys.argv)
    file_select=File_Select()
    file_select.initUi()
    file_select.show()
    sys.exit(app.exec_())
