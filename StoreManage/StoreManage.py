import sys
import Merchandise
from storeManage_ui import storeManage_widget
import storeManage_ui.storeManage_widget
from PyQt5.QtWidgets import QApplication,QWidget


if __name__ == '__main__':
    manager = Merchandise.Merchandise_Manage()



    app = QApplication(sys.argv)
    w = storeManage_widget.storeManage_widget()
    w.show()
    app.exec_() 