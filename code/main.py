import sys
from PyQt5.QtWidgets import QApplication
from lll import Cart
from mydb_utiles import *
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Cart("20191634")
    #ex=CheckOrder(1,2)
    ex.show()
    sys.exit(app.exec_())