import sys
from PyQt5.QtWidgets import QApplication
from usershow.lll import Cart
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Cart("20191234")
    #ex=CheckOrder(1,2)
    ex.show()
    sys.exit(app.exec_())